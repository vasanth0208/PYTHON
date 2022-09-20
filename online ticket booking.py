
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="travel_booking"

)
def pasdetail():
    
    from_=input("\nENTER THE FROM CITY :\t")
    to=input("\nENTER THE TO CITY :\t")
    mycursor=mydb.cursor()
    sql="select ID, ARRIVAL_TIME, TRAVELS_NAME, FROM_, TO__, PRICE, AC_BUS from bus_list where FROM_=%s  and TO__=%s"
    val=(from_,to)
    mycursor.execute(sql,val)
    result=mycursor.fetchall()
    if (result is result) and(result is  result):
        columns=("ID", "ARRIVAL_TIME", "TRAVELS_NAME", "FROM_", "TO__", "PRICE",  "AC_BUS" )
        print("\n")
        print(" \nAVAILABLE BUSES :\n")
        print("-------------------------------------------------------------------------------------------------------------------------")
        import pandas as pd
        a=pd.DataFrame(result,columns=columns)     
        print(a)
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        bus_id=input("\n ENTER THE BUS ID NO :\t")
        print(" \n YOUR BUS DETAILS IS:\n")
        my_column=("ID", "ARRIVAL_TIME", "TRAVELS_NAME", "FROM_", "TO__", "PRICE",  "AC_BUS" )
        sql4="select ID, ARRIVAL_TIME, TRAVELS_NAME, FROM_, TO__, PRICE, AC_BUS from bus_list where  ID=%s"
        val4=(bus_id,)
        mycursor.execute(sql4,val4)
        my_result=mycursor.fetchall()
        print("-------------------------------------------------------------------------------------------------------------------------")
        import pandas as pd
        a=pd.DataFrame(my_result,columns=my_column)     
        print(a)
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("\n1 AC IS ENTER :")
        print(" \n 2 NON AC IS ENTER :\n")
        print("-------------------------------------------------------------------------------------------------------------------------")
        
        ac_bus=int(input("ENTER AC BUS OR NON AC:\t"))
        
    
        if (ac_bus==1) and (ac_bus!=2):
            total=int(input("\n ENTER THE NO OF SEAT:\t"))
            adult=int(input("\nENTER THE NO OF ADULT:\t"))
            child=int(input("\nENTER THE NO OF  CHILD:\t"))
            date=input("\nENTER THE DATE:\t" )
            name=input("\nENTER THE NAME:\t")
            Ad_no=input("\nENTER THE AADHAR NO:\t")
            add=input("\nENTER THE ADDRESS:\t")
            mycursor=mydb.cursor()
            sql="insert into pass_detail( NAME_, AADHAR_NO, NO_OF_CHILD, NO_OF_ADULT, ADDRESS) values (%s,%s,%s,%s,%s)"
            val=(name,Ad_no,child,adult,add)
            mycursor.execute(sql,val)
            mydb.commit()    
            mycursor=mydb.cursor()
            sql1="select ARRIVAL_TIME from bus_list where ID=%s"
            val1=(bus_id,)
            mycursor.execute(sql1,val1)
            arrival=mycursor.fetchone()
            str1=" ".join(arrival)
            sql2="select TRAVELS_NAME from bus_list where ID=%s"
            val2=(bus_id,)
            mycursor.execute(sql2,val2)
            travels=mycursor.fetchone()
            str=" ".join(travels)
            sql3="select PRICE from bus_list where  ID=%s"
            val3=(bus_id,)
            mycursor.execute(sql3,val3)
            result=mycursor.fetchone()
            t=result[0]*total
            sql= "insert into booking_history(id, date_, arrival_time, travels_name, from_, to_, adult_charge, childran_charge, total_charge) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"                
            val=(bus_id,date,str1,str,from_,to,adult,child,t)
            mycursor.execute(sql,val)
            mydb.commit()
            final()
            query1="select id, date_, arrival_time, travels_name, from_, to_, adult_charge, childran_charge, total_charge  from booking_history where date_ =%s"
            valq1=(date,)
            mycursor=mydb.cursor()
            mycursor.execute(query1,valq1)
            bok=mycursor.fetchall()
            print("\n BOOKING RECIPT")
            print("-------------------------------------------------------------------------------------------------------------------------")
            column=('D', 'DATE', 'ARRIVAL TIME','TRAVELS NAME',' FROM','TO ','ADULT COUNT','CHILD COUNT','TOTAL')
            import pandas as pd
            a=pd.DataFrame(bok,columns=column)     
            print(a)
            print("-------------------------------------------------------------------------------------------------------------------------")
            
    
        if (ac_bus==2) and (ac_bus!=1):
            total=int(input("\n ENTER THE NO OF SEAT:\t"))
            adult=int(input("\nENTER THE NO OF ADULT:\t"))
            child=int(input("\nENTER THE NO OF  CHILD:\t"))
            date=input("\nENTER THE DATE:\t" )
            name=input("\nENTER THE NAME:\t")
            Ad_no=input("\nENTER THE AADHAR NO:\t")
            add=input("\nENTER THE ADDRESS:\t")
            mycursor=mydb.cursor()
            sql="insert into pass_detail( NAME_, AADHAR_NO, NO_OF_CHILD, NO_OF_ADULT, ADDRESS) values (%s,%s,%s,%s,%s)"
            val=(name,Ad_no,child,adult,add)
            mycursor.execute(sql,val)
            mydb.commit()    
            mycursor=mydb.cursor()
            sql1="select ARRIVAL_TIME from bus_list where ID=%s"
            val1=(bus_id,)
            mycursor.execute(sql1,val1)
            arrival=mycursor.fetchone()
            str1=" ".join(arrival)
            sql2="select TRAVELS_NAME from bus_list where ID=%s"
            val2=(bus_id,)
            mycursor.execute(sql2,val2)
            travels=mycursor.fetchone()
            str=" ".join(travels)
            sql3="select PRICE from bus_list where  ID=%s"
            val3=(bus_id,)
            mycursor.execute(sql3,val3)
            result=mycursor.fetchone()
            t=result[0]*total
            sql= "insert into booking_history(id, date_, arrival_time, travels_name, from_, to_, adult_charge, childran_charge, total_charge) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"                
            val=(bus_id,date,str1,str,from_,to,adult,child,t)
            mycursor.execute(sql,val)
            mydb.commit()
            final()
            query1="select id, date_, arrival_time, travels_name, from_, to_, adult_charge, childran_charge, total_charge from booking_history where date_ =%s"
            valq1=(date,)
            mycursor=mydb.cursor()
            mycursor.execute(query1,valq1)
            bok=mycursor.fetchall()
            print("\n BOOKING RECIPT")
            print("-------------------------------------------------------------------------------------------------------------------------")
            column=('D', 'DATE', 'ARRIVAL TIME','TRAVELS NAME',' FROM','TO ','ADULT COUNT','CHILD COUNT','TOTAL')
            import pandas as pd
            a=pd.DataFrame(bok,columns=column)     
            print(a)
            print("-------------------------------------------------------------------------------------------------------------------------")
    else:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("                                             NO RESULT                                                                            ")
        print("------------------------------------------------------------------------------------------------------------------------")       
    
    
def status():
    t=(input("\nENTER THE AADHAR NO :\t"))
    d=input("\nENTER THE BOOKING DATE :\t")
    query="select ID, NAME_, AADHAR_NO, NO_OF_CHILD, NO_OF_ADULT, ADDRESS from pass_detail where  AADHAR_NO=%s"
    valq=(t,)
    mycursor=mydb.cursor()
    mycursor.execute(query,valq)
    pasd=mycursor.fetchall()
    query1="select id, date_, arrival_time, travels_name, from_, to_, adult_charge, childran_charge, total_charge from booking_history where date_ =%s"
    valq1=(d,)
    mycursor=mydb.cursor()
    mycursor.execute(query1,valq1)
    bok=mycursor.fetchall()
    
    print("-------------------------------------------------------------------------------------------------------------------------")    
    if (pasd==pasd) and (bok==bok ):
        print("\n BUS DETAILS")
        print("------------------------------------------------------------------------------------------------------------------------")
        import pandas as pd
        column=('ID','DATE','ARRIVAL TIME','TRAVEL NAME', 'FROM ','TO','ADULT CHARGE', 'CHILD CHARGE','TOTAL AMOUNT')
        a=pd.DataFrame(bok,columns=column)     
        print(a)
       
        print("\n PASSANGER DETAILS")
        print("------------------------------------------------------------------------------------------------------------------------")
        import pandas as pd
        column=('ID',' NAME', 'AADHAR NO',' NO OF CHILD ',' NO OF ADULT ',' ADDRESS')
        a=pd.DataFrame(pasd,columns=column)     
        print(a)
        print("-------------------------------------------------------------------------------------------------------------------------")
      
    else:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("                                             NO RESULT                                                                            ")
        print("------------------------------------------------------------------------------------------------------------------------")
        
def cancel():
    name=(input("\nENTER THE NAME:\t"))
    d=input("\nENTER THE BOOKING DATE :\t")
    try:
        mycursor=mydb.cursor()
        query4="delete from pass_detail  where NAME_ =%s"
        valq4=(name,)
        query3="delete from booking_history where date_ =%s"
        valq3=(d,)
        mycursor.execute(query4,valq4)
        mycursor.execute(query3,valq3)
        mydb.commit()
 
        
        print("-------------------------------------------------------------------------------------------------------------------------")
        print("                                             CANCELATION SUCCESFULLY                                                                           ")
        print("------------------------------------------------------------------------------------------------------------------------")
   
    except:
        print("------------------------------------------------------------------------------------------------------------------------")
        print("                                             NO RESULT                                                                            ")
        print("------------------------------------------------------------------------------------------------------------------------")
   


def sel():
    print("-------------------------------------------------------------------------------------------------------------------------")
    print('                                               WELCOME TO LIIZA TICKET BOOKING                                                                           ')
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("\n 1 TICKET BOOKING \n"
          "\n 2 CHECK BOOKING DETAILS\n"
          "\n 3 TICKET CANCELATION"                    )
    print("-------------------------------------------------------------------------------------------------------------------------")
    try:
        cho=int(input("\nCHOOSE THE OPTIONS :"))
  
        if cho==1:
            pasdetail()
        elif cho==2:   
            status()
        elif cho==3:
            cancel()
        else:
            print("\n ENTER VALID INPUT")
    except ValueError:
        print("\n ENTER THE VALID INPUT")
def final():
        print("-------------------------------------------------------------------------------------------------------------------------")
        print('                                               BOOKING SUCCESFULLY                                                                          ')
        c
sel()
