from graphene import ObjectType as _otype
from graphene import List as _list
from data import get_course_data
from schemes import Course

class CourseQuery(_otype):
    courses = _list(Course)
    
    def resolve_courses(self, info):
        return get_course_data()