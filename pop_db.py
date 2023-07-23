import mysql.connector

#Calculating Federal tax on gross income
def calc_fed_tax(gross_income):

    if gross_income <= 50197:
        fed_tax = gross_income * .15

    elif gross_income <= 100392:
        fed_tax = 2761 + .205 * (gross_income-50197)

    elif gross_income <= 155625:
        fed_tax = 8282 + .26 * (gross_income - 100392)

    elif gross_income <= 221708:
        fed_tax = 12951 + .29 * (gross_income - 155625)

    else:
        fed_tax = 21819 + .33 * (gross_income - 221708)
    return fed_tax


#Calculating Ontario TAax on gross income
def calc_on_tax(gross_income):

    if gross_income <= 46226:
        on_tax= gross_income * .0505

    elif gross_income <= 92454:
        on_tax = 1895 + .0915 * (gross_income-46226)

    elif gross_income <= 150000:
        on_tax= 3754 + .1116 * (gross_income - 92454)

    elif gross_income <= 220000:
        on_tax = 5254 + .1216 * (gross_income - 150000)

    else:
        on_tax = 74543 + .1316 * (gross_income - 220000)
    return on_tax


#Calculating EI Premium on gross income
def calc_ei(gross_income):
    if gross_income <= 60300:
        ei = gross_income * .0158
    else:
        ei = 952.74

    return ei


#Calculating CCP on gross income
def calc_cpp(gross_income):
    if gross_income <= 61400:
        cpp = gross_income * .057
    else:
        cpp = 3499.8

    return cpp


# fed_tax = calc_fed_tax(gross_income)
# print("Federal tax for "+str(gross_income)+" is "+str(fed_tax))
# on_tax = calc_on_tax(gross_income)
# print("Ontario tax for "+str(gross_income)+" is "+str(on_tax))
# cpp = calc_cpp(gross_income)
# print("CPP for "+str(gross_income)+" is "+str(cpp))
# ei = calc_ei(gross_income)
# print("EI for "+str(gross_income)+" is "+str(ei))

# net_income = gross_income - fed_tax - on_tax - cpp - ei
# print("NetIncome for "+str(gross_income)+" is "+str(net_income))



# Populate the employees table using the contents of employee_data.txt .
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
            id, Fname, Lname, email, password, gross_income, fed_tax, on_tax, cpp, ei,net_income) 
            VALUES (%s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s);""",
                           (id, first_name, last_name, email, password, gross_income, fed_tax, on_tax, cpp, ei, net_income))

            #USING try and except to do have the first life of data.txt which is string and kept on crushing codes
        except:
            pass
    file.close()
    connection.commit()
    connection.close()
populate_employee_data()





# print('your federal tax is ${fed}'.format(fed=fed_tax))
# print("you left with ${netInc}".format(netInc=netIncome))
# print('you have ${inc}'.format(inc=gross_income), "in income taxes\n")

