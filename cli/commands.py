# commands.py - Implement CLI commands
# import hashlib
from contextlib import contextmanager
from db.models import Department, Employee, Project, Employee_Project, Session, Client, Admin

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def register_client(username, password):
#     with session_scope() as session:
#         if session.query(Client).filter(Client.username == username).first():
#             print("Username already exists.")
#         else:
#             client = Client(username=username, password=hash_password(password))
#             session.add(client)
#             print("Client registered successfully!")

# def register_admin(username, password):
#     with session_scope() as session:
#         if session.query(Admin).filter(Admin.username == username).first():
#             print("Username already exists.")
#         else:
#             admin = Admin(username=username, password=hash_password(password))
#             session.add(admin)
#             print("Admin registered successfully!")

# def login_client(username, password):
#     with session_scope() as session:
#         client = session.query(Client).filter(Client.username == username, Client.password == hash_password(password)).first()
#         if client:
#             print("Client logged in successfully!")
#             return True
#         else:
#             print("Invalid username or password.")
#             return False

# def login_admin(username, password):
#     with session_scope() as session:
#         admin = session.query(Admin).filter(Admin.username == username, Admin.password == hash_password(password)).first()
#         if admin:
#             print("Admin logged in successfully!")
#             return True
#         else:
#             print("Invalid username or password.")
#             return False

def add_department(department_name, location, manager_id):
    with session_scope() as session:
        try:
            department = Department(department_name=department_name, location=location, manager_id=manager_id)
            session.add(department)
            print("Department added successfully!")
        except Exception as e:
            print(f"Error adding department: {e}")

def add_employee(first_name, last_name, email, department_id):
    with session_scope() as session:
        try:
            employee = Employee(first_name=first_name, last_name=last_name, email=email, department_id=department_id)
            session.add(employee)
            print("Employee added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")

def add_project(project_name, start_date, end_date, department_id):
    with session_scope() as session:
        try:
            project = Project(project_name=project_name, start_date=start_date, end_date=end_date, department_id=department_id)
            session.add(project)
            print("Project added successfully!")
        except Exception as e:
            print(f"Error adding project: {e}")

def add_employee_project(employee_id, project_id, role, hours_worked):
    with session_scope() as session:
        try:
            employee_project = Employee_Project(employee_id=employee_id, project_id=project_id, role=role, hours_worked=hours_worked)
            session.add(employee_project)
            print("Employee-Project association added successfully!")
        except Exception as e:
            print(f"Error adding employee-project association: {e}")

def edit_department(department_id, name=None, location=None, manager_id=None):
    with session_scope() as session:
        try:
            department = session.query(Department).filter(Department.department_id == department_id).first()
            if department:
                if name:
                    department.department_name = name
                if location:
                    department.location = location
                if manager_id:
                    department.manager_id = manager_id
                print("Department details updated successfully!")
            else:
                print("Department not found.")
        except Exception as e:
            print(f"Error updating department: {e}")

def edit_employee(employee_id, first_name=None, last_name=None, email=None, department_id=None):
    with session_scope() as session:
        try:
            employee = session.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee:
                if first_name:
                    employee.first_name = first_name
                if last_name:
                    employee.last_name = last_name
                if email:
                    employee.email = email
                if department_id:
                    employee.department_id = department_id
                print("Employee details updated successfully!")
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error updating employee: {e}")

def edit_project(project_id, name=None, start_date=None, end_date=None, department_id=None):
    with session_scope() as session:
        try:
            project = session.query(Project).filter(Project.project_id == project_id).first()
            if project:
                if name:
                    project.project_name = name
                if start_date:
                    project.start_date = start_date
                if end_date:
                    project.end_date = end_date
                if department_id:
                    project.department_id = department_id
                print("Project details updated successfully!")
            else:
                print("Project not found.")
        except Exception as e:
            print(f"Error updating project: {e}")

def edit_employee_project(employee_id, project_id, role=None, hours_worked=None):
    with session_scope() as session:
        try:
            employee_project = session.query(Employee_Project).filter(Employee_Project.employee_id == employee_id, Employee_Project.project_id == project_id).first()
            if employee_project:
                if role:
                    employee_project.role = role
                if hours_worked:
                    employee_project.hours_worked = hours_worked
                print("Employee-Project association updated successfully!")
            else:
                print("Employee-Project association not found.")
        except Exception as e:
            print(f"Error updating employee-project association: {e}")

def delete_department(department_id):
    with session_scope() as session:
        try:
            department = session.query(Department).filter(Department.department_id == department_id).first()
            if department:
                session.delete(department)
                print("Department deleted successfully!")
            else:
                print("Department not found.")
        except Exception as e:
            print(f"Error deleting department: {e}")

def delete_employee(employee_id):
    with session_scope() as session:
        try:
            employee = session.query(Employee).filter(Employee.employee_id == employee_id).first()
            if employee:
                session.delete(employee)
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error deleting employee: {e}")

def delete_project(project_id):
    with session_scope() as session:
        try:
            project = session.query(Project).filter(Project.project_id == project_id).first()
            if project:
                session.delete(project)
                print("Project deleted successfully!")
            else:
                print("Project not found.")
        except Exception as e:
            print(f"Error deleting project: {e}")

def delete_employee_project(employee_id, project_id):
    with session_scope() as session:
        try:
            employee_project = session.query(Employee_Project).filter(Employee_Project.employee_id == employee_id, Employee_Project.project_id == project_id).first()
            if employee_project:
                session.delete(employee_project)
                print("Employee-Project association deleted successfully!")
            else:
                print("Employee-Project association not found.")
        except Exception as e:
            print(f"Error deleting employee-project association: {e}")
def display_departments():
    with session_scope() as session:
        try:
            departments = session.query(Department).all()
            if departments:
                print("Departments:")
                for department in departments:
                    print(f"ID: {department.department_id}, Name: {department.department_name}, Location: {department.location}")
            else:
                print("No departments found.")
        except Exception as e:
            print(f"Error displaying departments: {e}")



def display_employees():
    with session_scope() as session:
        try:
            employees = session.query(Employee).all()
            if employees:
                print("Employees:")
                for employee in employees:
                    print(f"ID: {employee.employee_id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}")
            else:
                print("No employees found.")
        except Exception as e:
            print(f"Error displaying employees: {e}")

def display_projects():
    with session_scope() as session:
        try:
            projects = session.query(Project).all()
            if projects:
                print("Projects:")
                for project in projects:
                    print(f"ID: {project.project_id}, Name: {project.project_name}, Start Date: {project.start_date}, End Date: {project.end_date}")
            else:
                print("No projects found.")
        except Exception as e:
            print(f"Error displaying projects: {e}")





