import sys
from os.path import abspath
from os.path import dirname

root_dir = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(root_dir)


pytest_plugins = [
    
]
