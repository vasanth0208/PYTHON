import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="bank_mangement"

)

      

def dep():
    am=int(input('\nENTER THE DEPOSIT AMOUNT: '))
    pin=int(input('\nENTER THE ATN PIN NO: '))
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
        print("------------------------------------------------------------------------------------------------------------------------")
   
        print("\nAMOUNT DEPOSIT YOUR ACCCOUNT")
        b="select * from amount where ATM_No=%s"
        mycursor=mydb.cursor()
        mycursor.execute(b,data)
        result=mycursor.fetchone()
        print("\n YOUR ACCOUNT BALANCE IS:",result[-1])
        print("------------------------------------------------------------------------------------------------------------------------")
   
        con()
    except TypeError:
        print("\n WRONG PIN NO TRY AGAIN")
    
def wid():
    am=int(input('\nENTER THE WITHDRAWAL AMOUNT: '))
    pin=int(input('\nENTER THE ATN PIN NO: '))
    a="select Balance from amount where ATM_No=%s"
    data=(pin,)
    try:
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        t=result[0]-am
        if (t>= am) or (t==0):
            sql=("update amount set Balance=%s where ATM_No=%s")
            d=(t,pin)
            mycursor.execute(sql,d)
            mydb.commit()
            print("------------------------------------------------------------------------------------------------------------------------")
   
            print("\nAMOUNT WITHDRAWAL SUCCESSFULLY COLLECT YOUR CASH")
            b="select * from amount where ATM_No=%s"
            mycursor=mydb.cursor()
            mycursor.execute(b,data)
            result=mycursor.fetchone()
            print("\nYOUR ACCOUNT BALANCE IS:",result[-1])
            print("------------------------------------------------------------------------------------------------------------------------")
   
            con()
        else:
            print("\nINSUFFICIANT BALANCE")
    except TypeError:
        print("\nWRONG PIN NO TRY AGAIN")
    
     
    
def bal():
    pin=int(input('\nENTER THE ATN PIN NO: '))
    a="select * from amount where ATM_No=%s"
    data=(pin,)
    try:
        print("------------------------------------------------------------------------------------------------------------------------")
        mycursor=mydb.cursor()
        mycursor.execute(a,data)
        result=mycursor.fetchone()
        print("\nYOUR ACCOUNT BALANCE IS:",result[-1])
        print("------------------------------------------------------------------------------------------------------------------------")
   
        con()
    except TypeError:
        print("\nWRONG PIN NO TRY AGAIN")
   
def main():
    print("------------------------------------------------------------------------------------------------------------------------")
   
    print("\n1.DEPOSIT AMOUNT")
    print("\n2.BALANCE ENQUIRY") 
    print("\n3.WITHDRAWAL")
    print("------------------------------------------------------------------------------------------------------------------------")
   
    try:
        trans=int(input("\nPLEASE ENTER THE TRANSACTION :"))

        if trans==1:
            dep()
        elif trans==2:
            bal()

        elif trans==3:
            wid()

        else:
            print("INVALID TRANSACTION TRY AGAIN")
    except ValueError:
        print("INVALID TRANSACTION TRY AGAIN")



def ins():
    a="y"
    b="n"
    try:
        ch=input('\n PLEASE INSERT YOUR ATM CARD Y OR N :')
        if ch in a:
            main()
        elif ch in b :
            print("------------------------------------------------------------------------------------------------------------------------")
            print("                                      THANK YOU FOR VIST  KV BANK "                                                     )
            print("------------------------------------------------------------------------------------------------------------------------")
   
        else:
            print("\nINVALID INPUT TRY AGAIN")
    except ValueError:
        print("\nINVALID INPUT TRY AGAIN")


def con():
    c="c"
    d="n"
    try:
        co=input("\nCONITINUE THE TRANSACTION ENTER 'C' OR N:")
        if co in c:
            main()
        elif co in d:
            print("------------------------------------------------------------------------------------------------------------------------")
            print("                                      THANK YOU FOR VIST KV BANK"                                                     )
            print("------------------------------------------------------------------------------------------------------------------------")
   
        else:
            print("INVALID INPUT TRY AGAIN")
    except ValueError:
        print("INVALID INPUT TRY AGAIN")    
    
print("------------------------------------------------------------------------------------------------------------------------")
print("                                                  WELCOME KV BANK"                                         ) 
print("------------------------------------------------------------------------------------------------------------------------")
   
ins()