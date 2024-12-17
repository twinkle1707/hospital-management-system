
import mysql.connector

def create_table():
    conn=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root#17',
        database='hospital'
    )

    cursor = conn.cursor()

    #patient table
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients(
                   id int AUTO_INCREMENT PRIMARY KEY,
                   name varchar(35),
                   age INT,
                   gender VARCHAR(10),
                   disease VARCHAR(255))''')
    #DOCTOR TABLE
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors
                   (id INT AUTO_INCREMENT PRIMARY KEY,
                   name varchar(35),
                   age INT,
                   gender varchar(10),
                   specialization VARCHAR(255)


                   )''')
    conn.commit()
    cursor.close()
    conn.close()

def add_patient_to_db(name,age,gender,disease):
    conn= mysql.connector.connect(
        host='localhost',
        user='root',
        password='root#17',
        database='hospital'
        )
    cursor=conn.cursor()
    cursor.execute('INSERT INTO patients(name,age,gender,disease) VALUES(%s, %s, %s, %s)',(name,age,gender,disease))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_patients():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root#17',
        database='hospital'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    patients = cursor.fetchall()
    cursor.close()
    conn.close()
    return patients

            


        
