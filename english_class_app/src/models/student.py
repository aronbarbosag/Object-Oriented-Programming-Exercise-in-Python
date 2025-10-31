from sqlalchemy import create_engine,Column,Table,MetaData,Integer,String,Float,ForeignKey,DateTime,Time
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from server.database import Base
from datetime import datetime,timedelta



student_activities = Table('student_activities',Base.metadata,
                           Column('student_id',Integer,ForeignKey('students.id'),primary_key=True),
                           Column('activity_id',Integer,ForeignKey('activities.id'),primary_key=True)
                           )
                          

class Activity(Base):
    
    __tablename__ = 'activities'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    date = Column(String(10))
    description = Column(String(255))

    students = relationship("Student",
                            secondary=student_activities,
                            back_populates="activities")
    
    def __str__(self):
        return f'{self.description}'


class Student(Base):
    
    __tablename__ = 'students'
    
    id = Column(Integer,primary_key=True,autoincrement=True)
    enrollment = Column(Integer,unique=True)
    name = Column(String(40))
    
    
    activities = relationship("Activity",
                              secondary=student_activities,
                              back_populates="students")
   
    tests = relationship("Test",back_populates='student')
    
    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'Student(id={self.id},enrollment={self.enrollment},name={self.name})'
    
    
class SchoolClass(Base):
        
        __tablename__ = 'school_class'
        
        id = Column(Integer, primary_key=True,autoincrement=True)
        year_semester = Column(String(6))
        time = Column(Time,nullable=True)
        
        term_id = Column(Integer,ForeignKey('term.id'))
        
        tests = relationship("Test",back_populates='school_class')
        term = relationship("Term",back_populates='school_class')
        
        def __init__(self,**kwargs)-> None:
            super().__init__(**kwargs)
            self.set_time()
        
        def set_time(self)-> None:
            self.time =  datetime.now().time()
            
            
    
class Test(Base):
        __tablename__ = 'test'
        id = Column(Integer, primary_key=True,autoincrement=True)
        school_class_id = Column(Integer,ForeignKey('school_class.id'))
        student_id = Column(Integer,ForeignKey('students.id'))
        score = Column(Float)
        
        student = relationship('Student',back_populates='tests')
        school_class = relationship('SchoolClass',back_populates='tests')
        
        
    
class Term(Base):
        __tablename__ = 'term'
        id = Column(Integer, primary_key=True,autoincrement=True)
        level= Column(String(8))
        level_number= Column(Integer)
        
        school_class = relationship('SchoolClass',back_populates='term')
        
    
    # Para criar a tabela a partir da classe -> Base.metadata.create_all(engine)