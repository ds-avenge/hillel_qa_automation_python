from db_app import (
    create_table,
    insert_student,
    get_student,
    update_student,
    delete_student
)
import pytest

@pytest.fixture(scope="module", autouse=True)
def prepare_database():
    create_table()

def test_insert_and_select_student():
    student_id = insert_student(
        "Dmytro",
        "dmytro@example.com"
    )

    student = get_student(student_id)

    assert student[0] == student_id
    assert student[1] == "Dmytro"
    assert student[2] == "dmytro@example.com"


def test_update_student():
    student_id = insert_student(
        "Dmytro",
        "dmytro@example.com"
    )

    update_student(
        student_id,
        "Dmytro Updated",
        "updated@example.com"
    )

    student = get_student(student_id)

    assert student[1] == "Dmytro Updated"
    assert student[2] == "updated@example.com"


def test_delete_student():
    student_id = insert_student(
        "Dmytro",
        "dmytro@example.com"
    )

    delete_student(student_id)
    student = get_student(student_id)

    assert student is None
