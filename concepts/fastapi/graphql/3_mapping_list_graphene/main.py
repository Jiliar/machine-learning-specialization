from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
import graphene
from queries import CourseQuery as course_query

app = FastAPI()
app.add_route('/courses', GraphQLApp(schema= graphene.Schema(query= course_query)))
print(graphene.Schema(query= course_query))

#uvicorn main:app --reload --port 8081