import json
import logging
from pathlib import Path

# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# Результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
base_path = Path(__file__).parent
log_file = base_path / "json_semkov.log"

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logger = logging.getLogger("json_validator")

def validate_json_files(folder_path: Path):
    for json_file in folder_path.glob("*.json"):
        try:
            with open(json_file, 'r', encoding="utf-8") as file:
                json.load(file)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {json_file.name}: {e}")

validate_json_files(base_path)
