
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#Using readlines()
requirements_file = open('requirements.txt', 'r')
required_modules = requirements_file.readlines()
 

for module in required_modules:
    install(module)


input("Press Enter to continue...")
