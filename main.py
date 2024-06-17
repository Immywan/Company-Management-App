import click

from cli.commands import (
    # register_client,
    # register_admin,
    # login_client,
    # login_admin,
    add_department,
    add_employee,
    add_project,
    add_employee_project,
    edit_department,
    edit_employee,
    edit_project,
    edit_employee_project,
    delete_department,
    delete_employee,
    delete_project,
    delete_employee_project,
    display_departments,
    display_employees,
    display_projects
)

@click.command()
def main():
    while True:
        menu()
        try:
            command = int(input("Enter a command number to execute: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # if command == 1:
        #     username = input("Enter username: ")
        #     password = input("Enter password: ")
        #     register_client(username, password)
        # elif command == 2:
        #     username = input("Enter username: ")
        #     password = input("Enter password: ")
        #     register_admin(username, password)
        # elif command == 3:
        #     username = input("Enter username: ")
        #     password = input("Enter password: ")
        #     login_client(username, password)
        # elif command == 4:
        #     username = input("Enter username: ")
        #     password = input("Enter password: ")
        #     login_admin(username, password)
        if command == 5:
            department_name = input("Enter department name: ")
            location = input("Enter location: ")
            manager_id = int(input("Enter manager ID: "))
            add_department(department_name, location, manager_id)
        elif command == 6:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            department_id = int(input("Enter department ID: "))
            add_employee(first_name, last_name, email, department_id)
        elif command == 7:
            project_name = input("Enter project name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            department_id = int(input("Enter department ID: "))
            add_project(project_name, start_date, end_date, department_id)
        elif command == 8:
            employee_id = int(input("Enter employee ID: "))
            project_id = int(input("Enter project ID: "))
            role = input("Enter role: ")
            hours_worked = float(input("Enter hours worked: "))
            add_employee_project(employee_id, project_id, role, hours_worked)
        elif command == 9:
            department_id = int(input("Enter department ID: "))
            name = input("Enter new name (leave blank to skip): ")
            location = input("Enter new location (leave blank to skip): ")
            manager_id = input("Enter new manager ID (leave blank to skip): ")
            edit_department(department_id, name or None, location or None, int(manager_id) if manager_id else None)
        elif command == 10:
            employee_id = int(input("Enter employee ID: "))
            first_name = input("Enter new first name (leave blank to skip): ")
            last_name = input("Enter new last name (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            department_id = input("Enter new department ID (leave blank to skip): ")
            edit_employee(employee_id, first_name or None, last_name or None, email or None, int(department_id) if department_id else None)
        elif command == 11:
            project_id = int(input("Enter project ID: "))
            name = input("Enter new project name (leave blank to skip): ")
            start_date = input("Enter new start date (YYYY-MM-DD, leave blank to skip): ")
            end_date = input("Enter new end date (YYYY-MM-DD, leave blank to skip): ")
            department_id = input("Enter new department ID (leave blank to skip): ")
            edit_project(project_id, name or None, start_date or None, end_date or None, int(department_id) if department_id else None)
        elif command == 12:
            employee_id = int(input("Enter employee ID: "))
            project_id = int(input("Enter project ID: "))
            role = input("Enter new role (leave blank to skip): ")
            hours_worked = input("Enter new hours worked (leave blank to skip): ")
            edit_employee_project(employee_id, project_id, role or None, float(hours_worked) if hours_worked else None)
        elif command == 13:
            department_id = int(input("Enter department ID: "))
            delete_department(department_id)
        elif command == 14:
            employee_id = int(input("Enter employee ID: "))
            delete_employee(employee_id)
        elif command == 15:
            project_id = int(input("Enter project ID: "))
            delete_project(project_id)
        elif command == 16:
            employee_id = int(input("Enter employee ID: "))
            project_id = int(input("Enter project ID: "))
            delete_employee_project(employee_id, project_id)
        elif command == 17:
            display_departments()
        elif command == 18:
            display_employees()
        elif command == 19:
            display_projects()
        else:
            print("Invalid command number. Please try again.")

def menu():
    print("Menu:")
    # print("1. Register as a client")
    # print("2. Register as an admin")
    # print("3. Login as a client")
    # print("4. Login as an admin")
    print("5. Add a department")
    print("6. Add an employee")
    print("7. Add a project")
    print("8. Add an employee to a project")
    print("9. Edit a department")
    print("10. Edit an employee")
    print("11. Edit a project")
    print("12. Edit an employee's project assignment")
    print("13. Delete a department")
    print("14. Delete an employee")
    print("15. Delete a project")
    print("16. Remove an employee from a project")
    print("17. Display all departments")
    print("18. Display all employees")
    print("19. Display all projects")

if __name__ == "__main__":
    main()
