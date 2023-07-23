# Python_Emplooyes_Net-Income

# Lab Project: Python File - db_to_csv and pop_db 

## Description

This lab project consists of three Python scripts: `db_to_csv.py` , `pop_db.py` and output `employees_db.csv` . The purpose of these scripts is to interact with a MySQL database named `payroll`, perform calculations related to taxes and net income, and populate the `employees` table using data from a text file named `employee_data.txt`. Additionally, the `db_to_csv.py` script exports data from the `employees` table to a CSV file named `employees_db.csv`.

## db_to_csv.py

The `db_to_csv.py` script contains a function `output_data_into_csv()` that connects to the `payroll` database, retrieves data from the `employees` table, and exports it into a CSV file. The columns included in the CSV file are `id`, `first_name`, `last_name`, `email`, `password`, `gross_income`, `fed_tax`, `on_tax`, `cpp`, `ei`, and `net_income`. Each row represents a record from the `employees` table.

```python
import mysql.connector

def output_data_into_csv():
    file = open("employees_db.csv", 'wt')
    connection = mysql.connector.connect(user='pi', password='1DieudonneP', host='localhost', database='payroll')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees;")

    textrow = "id, first_name, last_name, email, password, gross_income, fed_tax, on_tax, cpp, ei, net_income\n"
    file.write(textrow)

    for x in cursor:
        data = x
        id = int(data[0])
        first_name = data[1]
        last_name = data[2]
        email = data[3]
        password = data[4]
        gross_income = data[5]
        on_tax = data[6]
        fed_tax = data[7]
        cpp = data[8]
        ei = data[9]
        net_income = data[10]

        textrow = f"{id},{first_name},{last_name},{email},{password},{gross_income},{fed_tax},{on_tax},{cpp},{ei},{net_income}\n"
        file.write(textrow)

    file.close()
    connection.close()

output_data_into_csv()
```

## pop_db.py

The `pop_db.py` script contains several functions for calculating different taxes (`calc_fed_tax`, `calc_on_tax`, `calc_ei`, `calc_cpp`) based on the given `gross_income`. Additionally, there is a function `populate_employee_data()` that reads data from the `employee_data.txt` file, calculates taxes and net income using the above functions, and inserts the records into the `employees` table in the `payroll` database.

```python
import mysql.connector

# Calculating Federal tax on gross income
def calc_fed_tax(gross_income):
    # Tax calculation logic

# Calculating Ontario Tax on gross income
def calc_on_tax(gross_income):
    # Tax calculation logic

# Calculating EI Premium on gross income
def calc_ei(gross_income):
    # Premium calculation logic

# Calculating CPP on gross income
def calc_cpp(gross_income):
    # CPP calculation logic

# Populate the employees table using the contents of employee_data.txt
def populate_employee_data():
    file = open("employee_data.txt", 'rt')
    connection = mysql.connector.connect(user='pi', password='MypasswdP', host='localhost', database='payroll')
    cursor = connection.cursor()

    for x in file:
        try:
            data = x.split('\t')
            id = int(data[0])
            first_name = data[1]
            last_name = data[2]
            email = data[3]
            password = data[4]
            gross_income = float(data[5].strip())
            on_tax = calc_on_tax(gross_income)
            fed_tax = calc_fed_tax(gross_income)
            cpp = calc_cpp(gross_income)
            ei = calc_ei(gross_income)
            net_income = gross_income - fed_tax - on_tax - cpp - ei

            cursor.execute("""INSERT INTO employees (
            id, Fname, Lname, email, password, gross_income, fed_tax, on_tax, cpp, ei, net_income) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                           (id, first_name, last_name, email, password, gross_income, fed_tax, on_tax, cpp, ei, net_income))
        except:
            pass

    file.close()
    connection.commit()
    connection.close()

populate_employee_data()
```

