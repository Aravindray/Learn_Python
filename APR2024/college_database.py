'''Let's learn how to create database using python'''
import sqlite3

def main():
    '''This function create sqlite database'''

    # Establish Database Connection
    conn = sqlite3.connect('COLLEGE.db')
    print('Database Created Successfully')

    # Create a cursor
    cur = conn.cursor()

    # Create a table
    cur.execute("CREATE TABLE STUDENT(\
                RollNum INT CHECK(TYPEOF(RollNum) = 'Integer') PRIMARY KEY,\
                Name VARCHAR(20) CHECK(TYPEOF(Name) = 'text') NOT NULL,\
                Percentage INT CHECK(TYPEOF(Percentage) = 'Integer') NOT NULL);")
    print('Table created successfully')

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
