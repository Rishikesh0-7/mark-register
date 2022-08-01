import sqlite3

con = sqlite3.connect("marklist.db")
cur = con.cursor()

#cur.execute('''CREATE TABLE mark
#               (rollnum int , name text , mark int)''' )
#First run the code with this then close it and delete this code
                
start = input('''What would you like to do? "Insert" or "Update" or "Get" : ''')
if start.lower() == 'insert':

    name = input("Enter the name of Student : ")
    rollnum = input(f"Enter {name}'s Roll No. : ")
    mark = input(f"Enter the mark scored by {name} : ")

    cur.execute(f"INSERT INTO mark VALUES ({int(rollnum)} , '{name.capitalize()}' , {int(mark)})")
    print("Mark Successfully Inserted!")
elif start.lower() == 'get':
    rollnum = input("Enter the students's Roll No. : ")
    cur.execute(f"SELECT * FROM mark WHERE rollnum = {int(rollnum)}")
    data = cur.fetchall()
    if len(data) == 0:
        print("Student not found! Try Again Later.")
    else:
        print(f"Roll No. : {data[0][0]}\nName : {data[0][1]}\nMark : {data[0][2]}")
elif start.lower() == 'update':
    op = input('What would you like to change? "Roll Number" or "Name" or "Mark" : ')
    if op.lower() == 'roll number':
        name = input("Enter the name of student : ")
        cur.execute(f"SELECT * FROM mark WHERE name = '{name.lower().capitalize()}'")
        data = cur.fetchall()
        if len(data) == 0:
            print("Student not found! Try Again Later.")
        else:
            rollnum = input("Enter the new Roll Numner : ")
            cur.execute(f"UPDATE mark SET rollnum = {int(rollnum)} WHERE name = '{name.lower().capitalize()}'")
            print("Data updated!")
    elif op.lower() == 'name':
        rollnum = input("Enter the Roll Number of student : ")
        cur.execute(f"SELECT * FROM mark WHERE rollnum = {int(rollnum)}")
        data = cur.fetchall()
        if len(data) == 0:
            print("Student not found! Try Again Later.")
        else:
            name = input("Enter the correct name of Student : ")
            cur.execute(f"UPDATE mark SET name = '{name.lower().capitalize()}' WHERE rollnum = {int(rollnum)}")
            print("Data updated!")
    elif op.lower() == 'mark':
        rollnum = input("Enter the Roll Number of student : ")
        cur.execute(f"SELECT * FROM mark WHERE rollnum = {int(rollnum)}")
        data = cur.fetchall()
        if len(data) == 0:
            print("Student not found! Try Again Later.")
        else:
            mark = input("Enter the new mark : ")
            cur.execute(f"UPDATE mark SET mark = {int(mark)} WHERE rollnum = {int(rollnum)}")
            print("Data updated!")
    else:
        print("Try again!")
else:
    print("Try Again!")

con.commit()
con.close()
