## will be replaced with proper command line build later
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
UI_ROOT = PROJECT_ROOT / "frontend" / "ui"
OUT_DIR = PROJECT_ROOT / "frontend" / "src" / "ui" / "ui_generated"

if not UI_ROOT.exists():
    raise FileNotFoundError(f"UI_ROOT not found: {UI_ROOT}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "__init__.py").touch(exist_ok=True)

ui_files = list(UI_ROOT.rglob("*.ui"))
if not ui_files:
    print(f"No .ui files found in {UI_ROOT}")

for ui_file in ui_files:
    out_file = OUT_DIR / f"ui_{ui_file.stem}.py"
    print(f"Compiling {ui_file} -> {out_file}")
    subprocess.run(["pyside6-uic", str(ui_file), "-o", str(out_file)], check=True)