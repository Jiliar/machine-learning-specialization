import random
import json

course_names = ['Python Programming', 'Data Science Basics', 'Web Development', 'Machine Learning', 'Cloud Computing', 'Cybersecurity', 'UI/UX Design', 'Project Management', 'Blockchain', 'DevOps']
instructors = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Eve Green', 'Oscar White', 'Grace Blue', 'Mallory Black', 'Trent Grey', 'Walter Silver']
levels = ['Beginner', 'Intermediate', 'Advanced']
categories = ['Technology', 'Business', 'Design', 'Marketing', 'Data Science', 'Development']

# Generar 10 elementos aleatorios
courses_data = [
    {
        'course_name': random.choice(course_names),
        'instructor': random.choice(instructors),
        'duration_weeks': random.randint(4, 52),
        'level': random.choice(levels),
        'rating': round(random.uniform(1.0, 5.0), 2),
        'price_usd': round(random.uniform(50, 500), 2),
        'students_enrolled': random.randint(100, 2000),
        'category': random.choice(categories),
        'is_certified': random.choice([True, False]),
        'year_created': random.randint(2015, 2024),
    }
    for _ in range(3)
]

print(json.dumps(courses_data, sort_keys=True, indent=4))

print(courses_data[0]['category'])
print(json.dumps(courses_data, sort_keys=True, indent=4))

courses_data1 = [
    {
        1: random.choice(course_names),
        2: random.choice(instructors),
        3: random.randint(4, 52),
        4: random.choice(levels),
    }
    for _ in range(3)
]
courses_data1[0][100] = 'Testing 123'
print(json.dumps(courses_data1, sort_keys=True, indent=4))

# Methods:

print(courses_data[0].keys())
# output: dict_keys(['course_name', 'instructor', 'duration_weeks', 'level', 'rating', 'price_usd', 'students_enrolled', 'category', 'is_certified', 'year_created'])
print(type(courses_data[0].keys()))
# output: <class 'dict_keys'> (type answer: list)

print(courses_data[0].values())
print(type(courses_data[0].values()))
# output: <class 'dict_values'> (type answer: list)

print(courses_data[0].items())
print(type(courses_data[0].items()))
# output: <class 'dict_items'> (type answer: list<tuple>)