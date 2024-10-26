import random

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
    for _ in range(10)
]


def get_course_data():
    return courses_data