from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
from graphene import ObjectType as _otype
from graphene import String as _str
from graphene import Int as _int
from graphene import Float as _float
from graphene import Boolean as _bool
from graphene import List as _list
import graphene
import random

names = ['Charlie', 'Alice', 'Bob', 'Eve', 'Oscar', 'Grace', 'Mallory', 'Trent', 'Walter', 'Judy']
cities = ['London', 'Paris', 'Berlin', 'Madrid', 'New York', 'Tokyo', 'Moscow', 'Rome', 'Sydney', 'Cairo']


data = [
    {
        'name': random.choice(names),
        'city': random.choice(cities),
        'age': random.randint(18, 65),
        'score': round(random.uniform(0, 100), 2),
        'email': f"user{random.randint(1, 100)}@example.com",
        'registered': random.choice([True, False]),
        'height': round(random.uniform(1.5, 2.0), 2),
        'weight': random.randint(50, 100),
        'member_since': random.randint(2010, 2024),
        'country': random.choice(['UK', 'USA', 'Germany', 'Spain', 'Japan', 'Russia', 'Italy', 'Australia', 'Egypt']),
        'grade': random.randint(1, 11)
    }
    for _ in range(10)
]

class Student(_otype):
    name = _str()
    city = _str()
    age = _int()
    score = _float()
    email = _str()
    registered = _bool()
    height = _float()
    weight = _float()
    member_since = _int()
    country = _str()
    grade = _int()

class Grade(_otype):
    student = _list(Student)
    def resolve_student(self, info):
        return data
    

app = FastAPI()
app.add_route('/grades', GraphQLApp(schema= graphene.Schema(query= Grade)))
print(graphene.Schema(query= Grade))

#uvicorn 2_2_discovery_object_types:app --reload --port 8081