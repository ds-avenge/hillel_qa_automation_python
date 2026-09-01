"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
from pathlib import Path

log_file = Path(__file__).parent / "login_system.log"

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        force = True
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

class TestLogEvent:

    def test_success_log(self):
        log_event("Dmytro", "success")

        with open(log_file, "r") as file:
            logs = file.read()

        assert "Login event - Username: Dmytro, Status: success" in logs

    def test_expired_log(self):
        log_event("Dmytro", "expired")

        with open(log_file, "r") as file:
            logs = file.read()

        assert "Login event - Username: Dmytro, Status: expired" in logs

    def test_failed_log(self):
        log_event("Dmytro", "failed")

        with open(log_file, "r") as file:
            logs = file.read()

        assert "Login event - Username: Dmytro, Status: failed" in logs
