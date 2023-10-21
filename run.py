from pathlib import Path
from subprocess import run

PROJ_DIR = Path(__file__).parents[0]
main = PROJ_DIR.joinpath("src", "check_sizes.py")
python = PROJ_DIR.joinpath(".venv", "Scripts", "python.exe")
run([python, main])
