s#STEFI SHOBIKA SUKUMAR
# URK24CS1067

class Card:
    def __init__(me, c_no, c_bank, c_type, cus_name, exp_date, cvv):
        me.c_no=c_no
        me.c_bank=c_bank
        me. c_type= c_type
        me.cus_name=cus_name
        me.exp_date=exp_date
        me.cvv=cvv
    def print_card(me):
        print("THE CARD DETAILS ARE:")
        print("CARD NUMBER:",me.c_no)
        print("BANK:",me.c_bank)
        print("TYPE:",me. c_type)
        print("CUSTOMER NAME:",me.cus_name)
        print("EXPIRY DATE:",me.exp_date)
        print("CVV NUMBER:",me.cvv)

class DebitCard(Card):
    def __init__(self,c_no, c_bank, c_type, cus_name, exp_date, cvv,bal):
        super().__init__(c_no, c_bank, c_type, cus_name, exp_date, cvv)
        self.bal=int(bal)
    def withdraw(self,amt):
        try:
            amt=int(input("Enter withdrawel amount:"))
            if amt>=100000:
                print("Sorry you have to visit the bank and provide some documents to withdraw this amount.")
            
            self.bal-=int(amt)
        except:
            print("SOMETHING IS WRONG")
        
    def deposit(self,amt):
        try:
            amt=int(input("Enter amount to be deposited:")) 
            if amt>=100000:
                raise ValueError("You have to visit the branch to deposit huge amount")
            self.bal+=int(amt)
        except:
            print("SOMETIHING IS WRONG")
    def check_bal(self):
        print("Balance:",self.bal)

class CreditCard(Card):
    def __init__(self,c_no, c_bank, c_type, cus_name, exp_date, cvv, credit_amt):
        super().__init__(c_no, c_bank, c_type, cus_name, exp_date, cvv)
        self.credit_amt=0
    def Credit_use(self,amt):
        try:
            amt=int(input("enter the amount which is already used"))
            if amt>=500000:
                raise ValueError("ou crossed your credit limit")
            self.credit_amt+=amt
        except:
            print("SOMETING IS WRONG")

    def pay_back(self,amt):
        amt=int(input("enter the amount you paid:"))
        self.credit_amt-=amt
    def bill_amt(self):
        print("The bill is:",self.credit_amt)

a=Card("1001","SBI","SAVINGS","SUKU","20-09-2035","987")
a.print_card()

b=DebitCard("1001","SBI","SAVINGS","SUKU","20-09-2035","987","10000")
b.withdraw("5000")
b.deposit("900")
b.check_bal()

c=CreditCard("1001","SBI","SAVINGS","SUKU","20-09-2035","987")
c.Credit_use("5000")
c.pay_back("2500")
c.bill_amt()