class bank:
    def __init__(self,acno,person_name,balance,bank_name):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        self.bank_name=bank_name
    def deposite(self,amount): #already ulla accountikyu amount pass cheyanm
        self.balance+=amount
        print("your account",self.acno,"has been credited with amount",amount,"your available balance",self.balance)
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient amount in your account transaction failed")
        else:
            self.balance-=amount
            print("your account", self.acno, "has been debited with amount", amount, "your available",self.balance)
    def balance_enq(self):
        print("your current account balance is",self.balance)

obj=bank(123,"ramji",1234,"sbi")
obj.deposite(5000)
obj.withdraw(100)


