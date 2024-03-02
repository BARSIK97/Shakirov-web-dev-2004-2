def show_employee(name, salary=100000):
  return f"{name}: {salary} ₽"

employee_name = input()
employee_salary = int(input())
if employee_salary == 0:
  print(show_employee(employee_name))
if employee_salary > 0:
   (print(show_employee(employee_name, employee_salary)))


