import pytest
from db_config import get_session
from models import User, Subject, Student, Teacher


# Фикстура для создания и закрытия сессии
@pytest.fixture
def session():
    session = get_session()
    yield session
    session.rollback()  # Откат изменений после теста
    session.close()


# Тест для таблицы users
def test_user_operations(session):
    # Добавление
    user = User(user_email="olegqa@gmail.com")
    session.add(user)
    session.commit()
    assert (session.query(User).filter_by(user_email="olegqa@gmail.com").
            first() is not None)

    # Изменение
    user.user_email = "updated_olegqa@gmail.com"
    session.commit()
    assert (session.query(User).filter_by
            (user_email="updated_olegqa@gmail.com").first() is not None)

    # Удаление
    session.delete(user)
    session.commit()
    assert (session.query(User).filter_by
            (user_email="updated_olegqa@gmail.com").first() is None)


# Тест для таблицы teacher
def test_teacher_operations(session):
    # Добавление
    teacher = Teacher(email="teachers@gmail.com", group_id=1)
    session.add(teacher)
    session.commit()
    assert (session.query(Teacher).filter_by(email="teachers@gmail.com").
            first() is not None)

    # Изменение
    teacher.email = "updated_teachers@gmail.com"
    session.commit()
    assert (session.query(Teacher).filter_by
            (email="updated_teachers@gmail.com").first() is not None)

    # Удаление
    session.delete(teacher)
    session.commit()
    assert (session.query(Teacher).filter_by
            (email="updated_teachers@gmail.com").first() is None)


# Тест для таблицы subject
def test_subject_operations(session):
    # Добавление
    subject = Subject(subject_title="handmade")
    session.add(subject)
    session.commit()
    assert (session.query(Subject).filter_by(subject_title="handmade").
            first() is not None)

    # Изменение
    subject.subject_title = "updated_handmade"
    session.commit()
    assert (session.query(Subject).filter_by(subject_title="updated_handmade").
            first() is not None)

    # Удаление
    session.delete(subject)
    session.commit()
    assert (session.query(Subject).filter_by(subject_title="updated_handmade").
            first() is None)


# Тест для таблицы student
def test_student_operations(session):
    # Добавление
    student = Student(level="highest")
    session.add(student)
    session.commit()
    assert (session.query(Student).filter_by(level="highest").
            first() is not None)

    # Изменение
    student.level = "updated_highest"
    session.commit()
    assert (session.query(Student).filter_by(level="updated_highest").
            first() is not None)

    # Удаление
    session.delete(student)
    session.commit()
    assert (session.query(Student).filter_by(level="updated_highest")
            .first() is None)
