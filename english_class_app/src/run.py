from models.student import *
from server.database import Base,engine,SessionLocal


Base.metadata.create_all(engine)
session = SessionLocal()

aron = Student(enrollment =1,name ='Aron Freire')
beatriz = Student(enrollment = 2, name = 'Beatriz Santana')

advanced_english_course = Activity(date ='2025-10-31', description ='Advanced english C1')
basic_english_course = Activity(date = '2025-10-30',description = 'Basic english B1')

class_1 = SchoolClass(year_semester ='2025.1')
class_2 = SchoolClass(year_semester ='2025.2')

term_1 = Term(level='BASIC',level_number=1)
term_2 = Term(level='ADVANCED',level_number=2)
term_3 = Term(level='ADVANCED',level_number=3)

test_1 = Test(score=9.9)
test_2 = Test(score=6.5)
test_3 = Test(score=7)



aron.activities.append(advanced_english_course)
aron.activities.append(basic_english_course)
beatriz.activities.append(basic_english_course)

aron.tests.append(test_1)
aron.tests.append(test_3)

class_2.tests.append(test_3)
class_1.tests.append(test_1)

session.add_all([
    aron,beatriz,advanced_english_course,basic_english_course,
    class_1,class_2,
    test_1,test_2,test_3,
    term_1,term_2,term_3
    ])
session.commit()

