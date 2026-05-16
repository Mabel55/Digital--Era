from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Student(Base):
    # This is the actual name the table will have inside PostgreSQL
    __tablename__ = "students"

    # These are the columns inside our table
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    grade_level = Column(String)

class Teacher(Base):
    # The name of the table in PostgreSQL
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subject = Column(String) # What subject do they teach?

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # This is the magic link! It forces this column to strictly match an ID in the teachers table
    teacher_id = Column(Integer, ForeignKey("teachers.id"))