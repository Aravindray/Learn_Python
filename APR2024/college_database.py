'''Let's learn how to create database using python'''
import sqlite3

def main():
    '''This function create sqlite database'''

    # Establish database connection
    conn = sqlite3.connect('COLLEGE.db')
    print('Database Created Successfully')

    # Create a cursor
    cur = conn.cursor()

    # Delete table STUDENT
    cur.execute("DROP TABLE STUDENT;")

    # Create a table
    cur.execute("CREATE TABLE STUDENT(\
                RollNum INT CHECK(TYPEOF(RollNum) = 'integer') PRIMARY KEY,\
                Name VARCHAR(20) CHECK(TYPEOF(Name) = 'text') NOT NULL,\
                Percentage INT CHECK(TYPEOF(Percentage) = 'integer') NOT NULL);")
    print('Table created successfully')

    # Inserting data into table
    cur.execute("INSERT INTO STUDENT VALUES (1, 'Raj', 89);")
    cur.execute("INSERT INTO STUDENT VALUES (2, 'Aravind', 99);")
    cur.execute("INSERT INTO STUDENT VALUES (3, 'James', 98);")
    cur.execute("INSERT INTO STUDENT VALUES (4, 'Williams', 48);")
    cur.execute("INSERT INTO STUDENT VALUES (5, 'Aravindraj', 80);")
    print('Data Inserted Successfully')

    conn.commit()

    # Retrieving data from list
    print('Retrieving RollNum, Name, and Percentage of students')
    cur.execute("SELECT RollNum, Name, Percentage FROM STUDENT;")
    print(cur.fetchall())

    print('Retrieving all attribute values of a student')
    cur.execute("SELECT * FROM STUDENT;")
    print(cur.fetchall())

    print('Retrieving RollNum, Name of the students')
    cur.execute("SELECT RollNum, Name FROM STUDENT;")
    print(cur.fetchall())

    print('Retrieving all the attribute of students with percentage greater than 80')
    cur.execute("SELECT * FROM STUDENT WHERE Percentage > 80;")
    print(cur.fetchall())

    # Updating data in a table
    cur.execute("UPDATE STUDENT \
                SET Percentage = Percentage + 2 \
                WHERE Percentage < 50;")
    
    cur.execute("UPDATE STUDENT \
                SET Name = 'Not Raj' \
                WHERE RollNum = 1;")
    
    conn.commit()
    
    # Retrieving data after update
    print('Retrieving data after update')
    cur.execute("SELECT * FROM STUDENT;")
    print(cur.fetchall())

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
