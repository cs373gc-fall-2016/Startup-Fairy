.DEFAULT_GOAL := test

#TODO uncoment file checks
#startupfairy/tests.out		\
#IDB2.pdf					\

FILES :=						\
	IDB2.html					\
	IDB2.log					\
	startupfairy/models.py		\
	startupfairy/tests.py 		\
	.gitignore					\
	.travis.yml					\
	makefile					\
	README.md 										

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

config:
	git config -l
	
.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

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

#TODO where will __pycache__ be ??
clean:
	rm -f .coverage
	rm -f .pylintrc
	rm -f *.pyc
	rm -f IDB2.html
	rm -f IDB2.log
	rm -r startupfairy/__pycache__

#$(AUTOPEP8) -i startup/__init__.py
format:
	$(AUTOPEP8) -i startupfairy/run.py
	$(AUTOPEP8) -i startupfairy/models.py
	$(AUTOPEP8) -i startupfairy/tests.py
	$(AUTOPEP8) -i startupfairy/views.py
	

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

# TODO test output? coverage??
#$(COVERAGE) run    --branch test.py >  test.tmp 2>&1
#$(COVERAGE) report -m                      >> test.tmp
#cat test.tmp
TestApp:
	$(PYTHON) startupfairy/tests.py

IDB2.log:
	git log > IDB2.log

IDB2.html:
	PYDOC startupfairy/views.py >> IDB2.html

#__init__.py removed?
pylint: .pylintrc 
	-$(PYLINT) startupfairy/models.py
	-$(PYLINT) startupfairy/run.py
	-$(PYLINT) startupfairy/test.py
	-$(PYLINT) startupfairy/views.py


#TODO add make check back in and make TestApp
test:	IDB2.log IDB2.html check pylint TestApp
	


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