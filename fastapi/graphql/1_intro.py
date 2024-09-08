from fastapi import FastAPI
import graphene
from starlette_graphene3 import GraphQLApp

class Calculator(graphene.ObjectType):
    
    concat = graphene.String(a =  graphene.String(), b = graphene.String())
    add = graphene.String(a =  graphene.Int(), b= graphene.Int())
    
    def resolve_concat(self, info, a, b):
        return f'this is concatenation {a} and {b}'
    
    def resolve_add(self, info, a, b):
        return f'this is addition {a} + {b} = {a + b}'

app = FastAPI()
app.add_route('/calculator', GraphQLApp(schema=graphene.Schema(query = Calculator)))

# uvicorn 1_intro:app --reload --port 8081