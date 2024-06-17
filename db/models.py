from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///snippet_manager.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String(255))
    location = Column(String(255))
    manager_id = Column(Integer, ForeignKey('employee.employee_id'))

class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    department_id = Column(Integer, ForeignKey('department.department_id'))

    managed_department_id = Column(Integer, ForeignKey('department.department_id'))

    department = relationship('Department', backref='employees', foreign_keys=[department_id])
    managed_department = relationship('Department', foreign_keys=[managed_department_id])

class Project(Base):
    __tablename__ = 'project'

    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(255))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50))
    department_id = Column(Integer, ForeignKey('department.department_id'))

class Employee_Project(Base):
    __tablename__ = 'employee_project'

    employee_id = Column(Integer, ForeignKey('employee.employee_id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), primary_key=True)
    role = Column(String(100))
    hours_worked = Column(DECIMAL(6, 2))

class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(64))  # Storing hashed passwords

class Admin(Base):
    __tablename__ = 'admin'

    admin_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(64))  # Storing hashed passwords

Base.metadata.create_all(engine)
