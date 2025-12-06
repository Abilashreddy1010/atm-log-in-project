'''
MINI ATM PROJECT

requirments : credit , debit , mini statement , exit

'''


name="abilash"
password="abilash123"
user_name=input("enter the user name:")
passwords=input("enter the password:")
a='''
 1.credit
 2.debit
 3.mini statement
 4.exit
'''
amount=1000
if name==user_name and password==passwords:
    while True:
        print(a)
        
        option=int(input("enter the option:"))
        if option==1:
           credit_amount=float(input("enter the amount:"))
           print("amount after credit:",amount+credit_amount)
        elif option==2:
           debit_amount=float(input("enter the amount:"))
           print("amount after debit:",amount-debit_amount)
        elif option==3:
           print("##MINI STATEMENT AMOUNT##:",amount)
        elif option==4:
           print("break")      
else:
    print("incorrect")
    
    
'''   
enter the user name:abilash
enter the password:abilash321
incorrect
''' 
   
'''
enter the user name:abilash
enter the password:abilash123

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:1
enter the amount:100
amount after credit: 1100.0

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:2
enter the amount:1000
amount after debit: 0.0

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:3
##MINI STATEMENT AMOUNT##: 1000

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:4
break

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:
'''
  
    
    
    
    
    
    
    
    
    
    
    
    