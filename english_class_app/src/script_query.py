from sqlalchemy import create_engine,Table,MetaData,select,inspect,delete

engine = create_engine('sqlite:///db_course.sqlite')
metadata = MetaData()

inspector = inspect(engine)
print(inspector.get_table_names())

students = Table('students', metadata, autoload_with=engine)
activities = Table('activities', metadata, autoload_with=engine)
student_activities = Table('student_activities', metadata, autoload_with=engine)



stmt_ex = 'SELECT s.name, a.description FROM students as s, activities as a,student_activities as sa\
    WHERE s.id = sa.student_id AND a.id = sa.activity_id AND s.name = "Aron Freire"'

stmt = select(
    students.c.name,
    activities.c.description
).select_from(
    students.join(student_activities,students.c.id == student_activities.c.student_id)
            .join(activities,activities.c.id == student_activities.c.activity_id)
).where(
    students.c.name == 'Aron Freire'
)       



with engine.connect() as connection:
    results = connection.execute(stmt).fetchall()
    print('Querying... \n',results)





