#bank
#create_account
#deposit()
#withdraw()
#balance_enquiry()
import datetime


class Bank:
    bank_name="sbk"
    print("**************** WELCOME   TO    S B K ***********************\n")
    def __init__(self,acno,person_name,balance):
        self.acno = acno
        self.person_name = person_name
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        print("\nYour account",self.acno,"has been credited with amount of",amount,"\nYour available balance is",self.balance,"\nDate",datetime.date.today())
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient amount in you account\n Transaction denied")
        else:
            self.balance-=amount
            print("\nyour account", self.acno,"has been credited with amount of", amount,"\nYour available balance is",
                  self.balance)
    def balance(self):
        print("\nYour current balance is",self.balance)

obj=Bank(1000,"reji",3000)
obj.deposit(5000)
obj.withdraw(0)



#different types of variables
    #instance variables
        #self.acno,self.person_name,self.balance
    #static variables
        #efficient memory utilization
        #bank_name is an example
        #access by using class name.static variable name
