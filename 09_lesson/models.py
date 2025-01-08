from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Модель users
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_email = Column(String, unique=True, nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


# Модель subject
class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String, unique=True, nullable=False)
    # добавлено unique=True


# Модель student
class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True)
    level = Column(String, unique=True, nullable=False)
    education_form = Column(String, unique=True, nullable=True)
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


# Модель teacher
class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    group_id = Column(Integer, nullable=False)
