import os
import time

import psycopg2

#1
def get_connection():
    return psycopg2.connect(
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=5432
    )


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()

def insert_student(name, email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, email)
        VALUES (%s, %s)
        RETURNING id
        """,
        (name, email)
    )

    student_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return student_id

def get_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, email
        FROM students
        WHERE id = %s
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return student

def update_student(student_id, new_name, new_email):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = %s,
            email = %s
        WHERE id = %s
        """,
        (new_name, new_email, student_id)
    )

    connection.commit()
    cursor.close()
    connection.close()

def delete_student(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id = %s
        """,
        (student_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    time.sleep(3)

    create_table()

    print("Connected to PostgreSQL successfully")
    print("Table 'students' created successfully")
