from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp

course_name = 'Computer Science'
course_duration_year = 1

class Course(graphene.ObjectType):
    name = graphene.String()
    duration = graphene.Int()
    
    def resolve_name(self, info):
        return course_name
    
    def resolve_duration(self, info):
        return course_duration_year
    
app = FastAPI()
app.add_route('/courses', GraphQLApp(schema=graphene.Schema(query=Course)))
print(graphene.Schema(query=Course))

#uvicorn 2_1_intro_object_types:app --reload --port 8081