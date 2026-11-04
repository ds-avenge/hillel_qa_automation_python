from db_app import (
    create_table,
    insert_student,
    get_student,
    update_student,
    delete_student
)
from allure_commons.types import Severity
import pytest, allure

HOMEWORK_URL = (
    "https://lms.ithillel.ua/groups/69f1acc4f9879ecbe3a13f01/"
    "homeworks/6ae8b8cee4bf4f9903f2225c"
)

@pytest.fixture(scope="module", autouse=True)
def prepare_database():
    create_table()

@allure.suite("Homework 29 - Docker PostgreSQL CRUD")
@allure.epic("Database Testing")
@allure.feature("Student CRUD")
@allure.story("Create and Read Student")
@allure.title("Create student and verify saved data")
@allure.severity(Severity.CRITICAL)
@allure.link(HOMEWORK_URL, name="Homework 29")
def test_insert_and_select_student():
    with allure.step("Insert a new student into the database"):
        student_id = insert_student(
            "Dmytro",
            "dmytro@example.com"
        )

    with allure.step(f"Get student by id={student_id}"):
        student = get_student(student_id)

    with allure.step("Verify student data"):
        assert student[0] == student_id
        assert student[1] == "Dmytro"
        assert student[2] == "dmytro@example.com"

@allure.suite("Homework 29 - Docker PostgreSQL CRUD")
@allure.epic("Database Testing")
@allure.feature("Student CRUD")
@allure.story("Update Student")
@allure.title("Update student and verify changed data")
@allure.severity(Severity.NORMAL)
@allure.link(HOMEWORK_URL, name="Homework 29")
def test_update_student():
    with allure.step("Create student for update test"):
        student_id = insert_student(
            "Dmytro",
            "dmytro@example.com"
        )

    with allure.step(f"Update student with id={student_id}"):
        update_student(
            student_id,
            "Dmytro Updated",
            "updated@example.com"
        )

    with allure.step(f"Get updated student from database"):
        student = get_student(student_id)

    with allure.step("Verify updated student data"):
        assert student[1] == "Dmytro Updated"
        assert student[2] == "updated@example.com"

@allure.suite("Homework 29 - Docker PostgreSQL CRUD")
@allure.epic("Database Testing")
@allure.feature("Student CRUD")
@allure.story("Delete student")
@allure.title("Delete student and verify record is absent")
@allure.severity(Severity.NORMAL)
@allure.link(HOMEWORK_URL, name="Homework 29")
def test_delete_student():
    with allure.step("Create student for delete test"):
        student_id = insert_student(
            "Dmytro",
            "dmytro@example.com"
        )

    with allure.step(f"Delete student with id={student_id}"):
        delete_student(student_id)

    with allure.step("Try to get deleted student"):
        student = get_student(student_id)

    with allure.step("Verify student was deleted"):
        assert student is None
