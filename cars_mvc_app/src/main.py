import sys
from pathlib import Path


src_path = Path(__file__).resolve().parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from controllers.automovel_controlle import automovel_controller

def main():
  if __name__ == '__main__':
    automovel_controller()
  
main()    