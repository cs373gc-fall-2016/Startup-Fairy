.DEFAULT_GOAL := test


FILES :=						\
	IDB2.html					\
	IDB2.log					\
	IDB2.pdf					\
	startupfairy/models.py		\
	startupfairy/tests.py 		\
	startupfairy/tests.out		\
	.gitignore					\
	.travis.yml					\
	makefile					\
	README.md 										

ifeq ($(shell uname), Darwin)          # Apple
	PYTHON   := python3.5
	PIP      := pip3.5
	PYLINT   := pylint
	PYLINTFLAGS := --generated-members=String,Column,query, add, delete, commit
	COVERAGE := coverage-3.5
	PYDOC    := pydoc3.5
	AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
	PYTHON   := python3.5
	PIP      := pip3.5
	PYLINT   := pylint
	PYLINTFLAGS := --generated-members=String,Column,query
	COVERAGE := coverage-3.5
	PYDOC    := pydoc
	AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
	PYTHON   := python3.5
	PIP      := pip3.5
	PYLINT   := pylint
	PYLINTFLAGS := --generated-members=String,Column,query
	COVERAGE := coverage-3.5
	PYDOC    := pydoc3.5
	AUTOPEP8 := autopep8
else                                   # UTCS
	PYTHON   := python3.5
	PIP      := pip3.5
	PYLINT   := pylint3.5
	PYLINTFLAGS := --generated-members=String,Column,query
	COVERAGE := coverage-3.5
	PYDOC    := pydoc3.4
	AUTOPEP8 := autopep8
endif

config:
	git config -l
	
.pylintrc:
	$(PYLINT) $(PYLINTFLAGS) --disable=locally-disabled --reports=no --generate-rcfile > $@

check:
	@not_found=0;                                 \
	for i in $(FILES);                            \
	do                                            \
		if [ -e $$i ];                            \
		then                                      \
			echo "$$i found";                     \
		else                                      \
			echo "$$i NOT FOUND";                 \
			not_found=`expr "$$not_found" + "1"`; \
		fi                                        \
	done;                                         \
	if [ $$not_found -ne 0 ];                     \
	then                                          \
		echo "$$not_found failures";              \
		exit 1;                                   \
	fi;                                           \
	echo "success";

clean:
	rm -f .coverage
	rm -f .pylintrc
	rm -f *.pyc
	rm -r startupfairy/__pycache__

format:
	$(AUTOPEP8) -i startupfairy/models.py
	$(AUTOPEP8) -i startupfairy/tests.py
	$(AUTOPEP8) -i startupfairy/views.py
	

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

TestApp:	startupfairy/tests.py
	-$(COVERAGE) run    --branch startupfairy/tests.py >  startupfairy/tests.out 2>&1
	-$(COVERAGE) report -m                      >> startupfairy/tests.out
	cat startupfairy/tests.out

log:
	git log > IDB2.log

docs:

	cd startupfairy/ && $(PYDOC) -w views > ../IDB2.html
	cd startupfairy/ && $(PYDOC) -w models >> ../IDB2.html
	cat startupfairy/views.html > IDB2.html
	cat startupfairy/models.html >> IDB2.html
	rm -f startupfairy/views.html
	rm -f startupfairy/models.html

pylint: .pylintrc 
	-$(PYLINT) startupfairy/models.py
	-$(PYLINT) startupfairy/tests.py
	-$(PYLINT) startupfairy/views.py

test:	log docs check pylint TestApp

db:
	$(PYTHON) startupfairy/create_db.py
	$(PYTHON) startupfairy/populate_db.py
	$(PYTHON) startupfairy/populate_index.py

dropdb:
	$(PYTHON) startupfairy/drop_db.py

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --versio
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which $(PYDOC)
	$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list