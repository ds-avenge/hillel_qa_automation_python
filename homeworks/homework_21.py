from sqlalchemy import create_engine, text, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import random

DATABASE_URL = "postgresql+psycopg2://avenger@localhost:5432/hillel_it_school"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    # price: Mapped[float] = mapped_column()
    # student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))

class StudentCourse(Base):
    __tablename__ = "student_courses"

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)

students_data = [
    ("Anna", "Brown", "anna.brown@example.com"),
    ("John", "Smith", "john.smith@example.com"),
    ("Kate", "Wilson", "kate.wilson@example.com"),
    ("Mark", "Taylor", "mark.taylor@example.com"),
    ("Emily", "Davis", "emily.davis@example.com"),
    ("Chris", "Miller", "chris.miller@example.com"),
    ("Olivia", "Moore", "olivia.moore@example.com"),
    ("James", "Anderson", "james.anderson@example.com"),
    ("Sophia", "Thomas", "sophia.thomas@example.com"),
    ("Daniel", "Jackson", "daniel.jackson@example.com"),
    ("Emma", "White", "emma.white@example.com"),
    ("Michael", "Harris", "michael.harris@example.com"),
    ("Mia", "Martin", "mia.martin@example.com"),
    ("David", "Thompson", "david.thompson@example.com"),
    ("Charlotte", "Garcia", "charlotte.garcia@example.com"),
    ("Robert", "Martinez", "robert.martinez@example.com"),
    ("Amelia", "Robinson", "amelia.robinson@example.com"),
    ("William", "Clark", "william.clark@example.com"),
    ("Evelyn", "Lewis", "evelyn.lewis@example.com"),
    ("Thomas", "Walker", "thomas.walker@example.com"),
]

def add_student_to_course(first_name, last_name, email, course_name):
    with Session(engine) as session:
        course = session.scalar(select(Product).where(Product.name == course_name))
        if course is None:
            raise ValueError("Course not found")
        student = session.scalar(select(Student).where(Student.email == email))

        student_created = False

        if student is None:
            student = Student(first_name=first_name, last_name=last_name, email=email)

            session.add(student)
            session.flush()
            student_created = True

        existing_student_course = session.scalar(
            select(StudentCourse).where(
                StudentCourse.student_id == student.id,
                            StudentCourse.course_id == course.id
            )
        )

        if existing_student_course is not None:
            print(f"Student {student.first_name} {student.last_name} is already enrolled in {course.name}")
            return

        student_course = StudentCourse(student_id=student.id, course_id=course.id)

        session.add(student_course)
        session.commit()

        if student_created:
            print(f"New student {student.first_name} {student.last_name} was created and enrolled in {course.name}")
        else:
            print(f"Existing student {student.first_name} {student.last_name} was enrolled in {course.name}")

def get_students_by_course(course_name):
    with Session(engine) as session:
        course = session.scalar(select(Product).where(Product.name == course_name))
        if course is None:
            raise ValueError("Course not found")
        students = session.scalars(
            select(Student)
            .join(StudentCourse, Student.id == StudentCourse.student_id)
            .join(Product, Product.id == StudentCourse.course_id)
            .where(Product.name == course_name)
        ).all()
        if not students:
            raise ValueError("No students found for this course")
        for student in students:
            print(student.first_name, student.last_name, student.email)

def get_courses_by_student(email):
    with Session(engine) as session:
        courses = session.scalars(
            select(Product)
            .join(StudentCourse, Product.id == StudentCourse.course_id)
            .join(Student, Student.id == StudentCourse.student_id)
            .where(Student.email == email)
        ).all()
        if not courses:
            raise ValueError("No courses found for this student")
        for course in courses:
            print(course.name)

def update_student_email(old_email, new_email):
    with Session(engine) as session:
        student = session.scalar(select(Student).where(Student.email == old_email))
        if student is None:
            raise ValueError("Student not found")
        if old_email == new_email:
            raise ValueError("New email is the same as the old email")
        existing_student = session.scalar(select(Student).where(Student.email == new_email))
        if existing_student is not None:
            raise ValueError("New email already exists for another student")
        student.email = new_email
        session.commit()
        print(f"Student {student.first_name} {student.last_name} email updated from {old_email} to {new_email}")

def delete_student(email):
    with Session(engine) as session:
        student = session.scalar(select(Student).where(Student.email == email))
        if student is None:
            raise ValueError("Student not found")
        student_courses = session.scalars(select(StudentCourse).where(StudentCourse.student_id == student.id)).all()
        for student_course in student_courses:
            session.delete(student_course)
        session.flush()
        session.delete(student)
        session.commit()
        print(f"Student {student.first_name} {student.last_name} with email {email} has been deleted")

with Session(engine) as session:
    # new_student = Student(first_name="Dmytro", last_name="Test", email="dmytro.test@example.com")
    # session.add(new_student)
    # session.commit()
    # student_course = StudentCourse(student_id=1, course_id=1)
    # session.add(student_course)
    # session.commit()
    # student = session.scalar(select(Student).where(Student.email == "dmytro.test@example.com"))
    # course = session.scalar(select(Product).where(Product.name == "QA Automation – Python"))
    # if student is None:
    #     raise ValueError("Student not found")
    # if course is None:
    #     raise ValueError("Course not found")
    # student_course = StudentCourse(student_id=student.id, course_id=course.id)
    courses = session.scalars(select(Product)).all()
    for first_name, last_name, email in students_data:
        student = Student(first_name=first_name, last_name=last_name, email=email)
        session.add(student)
        session.flush()

        selected_courses = random.sample(courses, random.randint(1, 3))
        for course in selected_courses:
            student_course = StudentCourse(student_id=student.id, course_id=course.id)
            session.add(student_course)
    session.commit()

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT current_database();"))
#     print(result.scalar())

add_student_to_course(
    "Denys",
    "Test",
    "denys.test@example.com",
    "QA Automation – Python"
)
get_students_by_course("QA Automation – Python")
get_courses_by_student("denys.test@example.com")
update_student_email(
    "denys.test@example.com",
    "denys.final@example.com"
)
delete_student("denys.final@example.com")

# --------------------------------------------------------
#SQL запити нижче:
# CREATE DATABASE hillel_it_school;
#
# CREATE TABLE categories (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL
# );
#
# create table products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     description TEXT,
#     price DECIMAL(10, 2) NOT NULL,
#     teacher VARCHAR(150),
#     category_id INT NOT NULL REFERENCES categories(id)
# );
#
# INSERT INTO categories (name) VALUES
#     ('Testing'),
#     ('Programming'),
#     ('Management'),
#     ('Design'),
#     ('Artificial Intelligence');
#
# SELECT * FROM categories;
# SELECT * FROM products;
#
# INSERT INTO products (name, description, price, teacher, category_id) VALUES
#     ('QA Manual with AI', 'A comprehensive course on manual testing with AI integration.', 19310.00, 'Alice Brown', 1),
#     ('QA Technical Pro', 'Advanced techniques in QA testing for professionals.', 17510.00, 'Charlie Davis', 1),
#     ('QA Automation – Python', 'Learn automation testing using Python.', 19850.00, 'Eve Wilson', 1),
#     ('QA Automation — JavaScript with AI', 'Master automation testing with JavaScript and AI tools.', 19850.00, 'Frank Miller', 1),
#     ('Introduction to Python', 'A beginner-friendly course on Python programming.', 25610.00, 'John Doe', 2),
#     ('Java Basic', 'An introduction to Java programming.', 8600.00, 'Jane Smith', 2),
#     ('Front-end Basic', 'Learn the basics of front-end web development.', 12740.00, 'Bob Johnson', 2),
#     ('AI-Powered Full-Stack JavaScript Developer', 'Become a full-stack developer with AI-powered JavaScript skills.', 33440.00, 'Alice Brown', 2),
#     ('Project Management with AI', 'Learn project management techniques enhanced with AI tools.', 16610.00, 'Charlie Davis', 3),
#     ('Project Management Pro', 'Advanced project management strategies for professionals.', 11210.00, 'Eve Wilson', 3),
#     ('Бізнес-аналіз with AI', 'Learn business analysis techniques with AI integration.', 13910.00, 'Frank Miller', 3),
#     ('Product Management with AI', 'Master product management skills with AI tools.', 11880.00, 'John Doe', 3),
#     ('Графічний дизайн with AI', 'Learn graphic design techniques enhanced with AI.', 19850.00, 'Jane Smith', 4),
#     ('Основи Web дизайну', 'A beginner-friendly course on web design fundamentals.', 12110.00, 'Bob Johnson', 4),
#     ('UI/UX Design Pro', 'Advanced UI/UX design techniques for professionals.', 20210.00, 'Alice Brown', 4),
#     ('3D моделювання', 'Learn 3D modeling techniques with AI tools.', 20210.00, 'Charlie Davis', 4),
#     ('Штучний інтелект для бізнесу та роботи', 'Learn how to leverage AI for business and work applications.', 13010.00, 'Eve Wilson', 5),
#     ('AI Agents з нуля: створення та автоматизація', 'Master AI agent creation and automation from scratch.', 14810.00, 'Frank Miller', 5),
#     ('AI Agents for Developers', 'Learn to develop AI agents for various applications.', 14810.00, 'John Doe', 5),
#     ('AI Agents for QA', 'Learn to create AI agents specifically for QA testing.', 14810.00, 'Jane Smith', 5);
#
# SELECT
#     products.name AS course,
#     products.price,
#     products.teacher,
#     categories.name AS category
# FROM products
# JOIN categories ON products.category_id = categories.id;
#
# CREATE TABLE students (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(100) NOT NULL,
#     last_name VARCHAR(100) NOT NULL,
#     email VARCHAR(150) UNIQUE NOT NULL
# );
#
# CREATE TABLE student_courses (
#     student_id INT NOT NULL REFERENCES students(id),
#     course_id INT NOT NULL REFERENCES products(id),
#     PRIMARY KEY (student_id, course_id)
# );


