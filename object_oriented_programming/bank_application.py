#bank
#create_account()
#deposite()
#withdraw()
#balance_enq()



class bank:
    bank_name="SBI"
    def __init__(self):
        print("mai")

    def create_account(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        #self.bank_name=bank_name


    def deposite(self,amount):
        self.balance+=amount
        print(bank.bank_name,"your account",self.acno,"has been credited with amount",amount,"your available balance is",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient amount in your account transaction failed")
        else:
            self.balance-=amount
            print(self.bank_name,"your account",self.acno,"has been debited with amount",amount,"your available balance",self.balance)

    def balance_enq(self):
        print("your current balance =",self.balance)

obj=bank()
obj.create_account(1002,"ramji",3000)
obj.deposite(5000)
obj.withdraw(25000)

obj1=bank()
obj.create_account(1032,"sam",4000)
obj.deposite(10000)


print(obj.acno) #accessing outside class

#different types of variable-->static and instance variable
#instance variabe are always prepended with self key word
#self.acno,self.person_name,self.balance,self.bank_name


#we can access instance variabe outside class with referncename(objname).instance variable

#static variable(bank_name)---->efficient memory utilization
#we can access using self./class_name.static variable name -->self.bank_name/bank.bank_name

#different types of methods(self arg)
#1.accessing instance method reference.method-->instance method

#2.static method:
#@staticmethod