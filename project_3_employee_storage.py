def save_employee_data():
    employees = {}
    for i in range(2):
      emp_id = input(f"Enter ID for employee {i+1}: ")
      emp_name = input(f"Enter Name for employee {i+1}: ")
      employees[emp_id] = emp_name
  with open("employees.txt", "w") as file:
      file.write("--- Authorized Employees List ---\n")
      for emp_id, emp_name in employees.items():
           file.write(f"ID: {emp_id} | Name: {emp_name}\n")
      print("[+] Success: Employee registry has been saved to 'employees.txt'.")
