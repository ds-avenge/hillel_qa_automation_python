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
