import logging
import xml.etree.ElementTree as ET
from pathlib import Path

# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення
# timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
base_path = Path(__file__).parent
xml_file = base_path / "groups.xml"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
)

logger = logging.getLogger("xml_logger")

def get_incoming_by_group_number(file_path: Path, group_number: str):
    """
    Функція для пошуку значення timingExbytes/incoming по group/number у XML файлі.

    :param group_number: Номер групи для пошуку
    :return: Значення timingExbytes/incoming або повідомлення про відсутність
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == group_number:
                incoming = group.find("timingExbytes/incoming")
                if incoming is not None:
                    return incoming.text
                return None
        return None
    except ET.ParseError as e:
        logger.error(f"Error parsing XML file: {e}")
        return None

result = get_incoming_by_group_number(xml_file, group_number="2")
logger.info(f"Incoming value for group number 2: {result}")
