import subprocess
import requests
import json

def run_tests():
    # output = subprocess.getoutput("python tests.py")
    return json.dumps({'output': 'hllo'})

run_tests()
