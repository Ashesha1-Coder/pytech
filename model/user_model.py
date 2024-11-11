import mysql.connector
from mysql.connector import Error
class user_model():
    
    def __init__(self):
        # Connection establishment code
        try:
             
            
            self.con=mysql.connector.connect(host="localhost",user="root",passwords="",database="flask_learning")
            self.cur=self.con.cursor(dictionary=True)
            print("Connection sucessful")
        except Error as e:
            print("An error occured:",e)
 
    def user_getall_model(self):
        # Connection establishment code
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        print(result)
        # Query execution code
        return "This is user_signup_model"