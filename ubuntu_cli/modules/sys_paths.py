import os
from pathlib import Path

ubuntu_cli_dir: str = str(Path(__file__).resolve().parent.parent)

home_dir: str = os.path.expanduser("~")
