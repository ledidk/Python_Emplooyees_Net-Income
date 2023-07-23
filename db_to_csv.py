#
import mysql.connector
def output_data_into_csv():
    file = open("employees_db.csv", 'wt')
    connection = mysql.connector.connect(user='pi', password='1DieudonneP', host='localhost', database='payroll')
    cursor = connection.cursor()
    cursor.execute("select* from employees;")



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

        textrow = ''+str(id) + "," + first_name + "," + last_name + "," + email + "," + password + "," + str(gross_income) + "," + str(fed_tax) + "," + str(on_tax) + "," + str(cpp) + "," + str(ei) + "," + str(net_income)+"\n"

        file.write(textrow)





    file.close()
    connection.close()

output_data_into_csv()


