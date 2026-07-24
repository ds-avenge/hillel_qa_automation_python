# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
#-----
print("Original list of people records:")
print(people_records)

new_record = ('Dmytro', 'Semkov', 27, 'QA Engineer', 'Kyiv')
people_records.insert(0, new_record)

print("\nNew record was added at index 0:")
print(f"Added record: {people_records[0]}")
print(f"Updated list: {people_records}")

people_records[1], people_records[5] = people_records[5], people_records[1]
print("\nRecords at indexes 1 and 5 were swapped:")
print(f"Index 1 now contains: {people_records[1]}")
print(f"Index 5 now contains: {people_records[5]}")

indexes_to_check = (6, 10, 13)

print("\nChecking ages for records at indexes 6, 10, and 13:")
for index in indexes_to_check:
    print(f"Index {index}: {people_records[index]}")

all_ages = all(
  people_records[index][2] >= 30
  for index in indexes_to_check
)

print("\nAge validation result:")
if all_ages:
    print("Passed: all selected people are 30 years old or older.")
else:
    print("Failed: at least one selected person is younger than 30.")
