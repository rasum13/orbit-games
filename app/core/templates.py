from pathlib import Path
from fastapi.templating import Jinja2Templates


CORE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = CORE_DIR.parent / "templates"

templates = Jinja2Templates(directory=TEMPLATES_DIR)
