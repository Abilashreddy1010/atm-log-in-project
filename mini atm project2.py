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
    print(a)
    option=int(input("enter the option:"))
    if option==1:
        credit_amount=float(input("enter the amount:"))
        print("amount after credit:",amount+credit_amount)
        
else:
    print("incorrect")
    


'''
enter the user name:abilash
enter the password:abilash123

 1.credit
 2.debit
 3.mini statement
 4.exit

enter the option:1
enter the amount:11
amount after credit: 1011.0
'''   
    
    
    
    
    
    
    