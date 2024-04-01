import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(id integer Primary Key,name text,desig text,salary text,email text,gender text,contact text,address text);
        """
        self.cur.execute(sql)
        self.con.commit()

    #insert function
    def insert(self,name,desig,salary,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name,desig,salary,email,gender,contact,address))
        self.con.commit()

    #fetch all data from db
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        return rows
    #delete a record in db
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

    #Update a record in db
    def update(self,name,desig,salary,email,gender,contact,address):
        self.cur.execute("update employees set name=?, desig=?, salary=?, email=?, gender=?, contacts=?, address=? where id=?",(name,desig,salary,email,gender,contact,address),id)
        self.con.commit()

o=Database("Employee.db")
