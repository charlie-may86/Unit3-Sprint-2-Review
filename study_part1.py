import sqlite3

connection = sqlite3.connect('study_part1.sqlite3')
cursor = connection.cursor()

# Drop the table if it already exist
cursor.execute('DROP TABLE IF EXISTS students')

create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student VARCHAR (80),
    studied TEXT,
    grade INT,
    age INT,
    sex TEXT)
'''

cursor.execute(create_table_query)

sample_data = [
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male')
]

for row in sample_data:
    insert_data_query = f'''
    INSERT INTO students (student, studied, grade, age, sex)
        VALUES {row}
    '''
    cursor.execute(insert_data_query)

connection.commit()


# What is the average age? Expected Result - 48.8
query1 = 'SELECT AVG(age) FROM students'
result = cursor.execute(query1).fetchone()
print(f'What is the average age? {result[0]}')

query2 = "SELECT student FROM students WHERE(sex = 'Female')"
result2 = cursor.execute(query2).fetchall()
print(f'Which students are female? {result2[0]}')

query3 = 'SELECT COUNT(studied) FROM students WHERE (studied = "True")'
result3 = cursor.execute(query3).fetchone()
print(f'{result3[0]} students studied')

query4 = 'SELECT * FROM students ORDER BY student'
result4 = cursor.execute(query4).fetchall()
print(result4)

