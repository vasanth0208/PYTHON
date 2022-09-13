import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="bank_mangement"

)

      

def dep():
    am=int(input('Enter the deposit Amount: '))
    pin=int(input('Enter the ATM Pin: '))
    a="select Balance from amount where ATM_No=%s"
    data=(pin,)
    try:
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        t=result[0]+am
        sql=("update amount set Balance=%s where ATM_No=%s")
        d=(t,pin)
        mycursor.execute(sql,d)
        mydb.commit()
        print("amount deposit succesfully")
        b="select * from amount where ATM_No=%s"
        mycursor=mydb.cursor()
        mycursor.execute(b,data)
        result=mycursor.fetchone()
        print("your account balance is :",result[-1])
        main()
    except TypeError:
        print("invalid pin try again")
    
def wid():
    am=int(input('Enter the withrawal Amount: '))
    pin=int(input('Enter the ATM Pin: '))
    a="select Balance from amount where ATM_No=%s"
    data=(pin,)
    
    try:
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        t=result[0]-am
        sql=("update amount set Balance=%s where ATM_No=%s")
        d=(t,pin)
        mycursor.execute(sql,d)
        mydb.commit()
        print("amount withdrawal succesfully")
        b="select * from amount where ATM_No=%s"
        mycursor=mydb.cursor()
        mycursor.execute(b,data)
        result=mycursor.fetchone()
        print("your account balance is :",result[-1])
        main()
    except TypeError:
        print("invalid pin try again")
    
def bal():
    pin=int(input('Enter the ATM Pin: '))
    a="select * from amount where ATM_No=%s"
    data=(pin,)
    try:
        
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        print("your account balance is :",result[-1])
        main()
    except TypeError:
        print("invalid pin try again")
    
def main():
    print("1.DEPOSIT AMOUNT")
    print("2.BALANCE ENQUIRY") 
    print("3.WITHDRAWAL")
    try:
        trans=int(input("Enter the transection :"))

        if trans==1:
            dep()
        elif trans==2:
            bal()

        elif trans==3:
            wid()

        else:
            print("invalid taransection , try again")
    except ValueError:
        print("invalid tansection try again")


    
main()
