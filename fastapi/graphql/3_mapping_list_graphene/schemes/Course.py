from graphene import ObjectType as _otype
from graphene import String as _str
from graphene import Int as _int
from graphene import Float as _float
from graphene import Boolean as _bool

class Course(_otype):
    course_name = _str()
    instructor = _str()
    duration_weeks = _int()
    level = _str()
    rating = _float()
    price_usd = _float()
    students_enrolled = _int()
    category = _str()
    is_certified = _bool()
    year_created = _int()