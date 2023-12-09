from abc import ABC ,abstractmethod
import random

class Bank:
    def __init__(self,name) -> None:
        self.name=name
        self.__account=[]
        self.__admin=[]
        self.__totalbalance=0
        self.Total_loan=0
    def balance(self,bal):
        self.__totalbalance +=bal
        
    @property
    def Total_balance(self):
        return self.__totalbalance
    
    def add_account(self,account):
        self.__account.append(account)
    
    def remove_account(self,use,psw):
        for user in self.__account:
            if user.name==use and user.password==psw:
                self.__account.remove(user)
    
    def employe(self,account):
        self.__admin.append(account)
    @property  
    def get(self):
        return self.__account
    @property
    def get1(self):
        return self.__admin

class Account(ABC):
    def __init__(self,name,email,address,password,type) -> None:
        super().__init__()
        self.name=name
        self.email=email
        self.address=address
        self.password=password
        self.type=type
        self.__balance=0
        self.accountNo=random.randint(100000,999999)
        self.loane=0
        self.loan_balance=0
        self.Trshistry=[]
        
    def deposit(self,amount):
        if amount >= 0:
            self.__balance += amount
            print("After deposit {} New balance is {}".format(amount,self.__balance))
        else:
            print("Invail deposit")
            
            
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print('You Withdraw {} New balance is {}'.format(amount,self.__balance))
            
        else:
            print('Withdrawal amount exceeded')
    @property       
    def available_balance(self):
        return self.__balance
    
    def loan(self,amount):
        self.loane +=1
        if self.loane >2:
            print("You Can not apply for loan")
            return
        if amount <= self.__balance*10:
            self.__balance += amount
            self.loan_balance += amount
            
            print('You can get loan {} New balance is {}'.format(amount,self.__balance))
        else:
            print("You get loan only {} taka,please apply in this limit".format(self.__balance*10))
            
                
        
    def __repr__(self) -> str:
        return f'1) Name: {self.name} /n 2)Current Balance: {self.__balance} /n 3) Account Number: {self.accountNo} /n 4) loan: {self.loane} /n 5)Passwoard: {self.password} /n 6) Tranjection Histry: {self.Trshistry}'
    
          
class Savings(Account):
    def __init__(self, name, email, address, password) -> None:
        super().__init__(name, email, address, password, 'Savings')
        
        
class Current(Account):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address, password, 'Current')
        
        
class Admin(ABC):
    def __init__(self,Name,post,password) -> None:
        super().__init__()
        self.name=Name
        self.post=post
        self.password=password
        

dvbl=Bank('DVBL')
person2=Savings('Default','Nothing','Nothing',1236)
dvbl.add_account(person2)
person=Admin('Suvomita','Senior Officer',123)
dvbl.employe(person)
parson1=Admin('Susmita','Manager',1234)
dvbl.employe(parson1)
print('1: Admin ')
print("2: User")
print("3: Exit")
loan_f=0
while True:
    a=int(input())

    if a==1:
        name=input("Enter Your Name(admin): ")
        cnt=0
        for use in dvbl.get1:
            if use.name==name:
                cnt=1
                pasw=int(input("Passward "))
                if use.password==pasw:
                    print("You Logged in")
                    print("1: Create New Bank Account")
                    print("2: Delete Bank account")
                    print("3: All Bank account")
                    print("4: Cheak Balance")
                    print("5: Total Loan balance ")
                    print("6: Loan Feateare ")
                    print("7: logged Out")
                    while True:
                        t=int(input())
                        if t==1:
                            print('if You want to Create a Savings account press 1')
                            print("if You want to create a Current account press 2")
                            s=int(input())
                            if s==1 or s==2:
                                name=input("Account Name: ")
                                for user in dvbl.get:
                                    if user.name == name:
                                        print('This Name is already exist')
                                        break
                                    else:
                                        person=Account(name,input('Email: '),input("Address "),input("Password "),'Savings')
                                        print (" New account is created . Account Number is: {}".format(person.accountNo))
                                        dvbl.add_account(person)  
                                        break
                            
                        if t==2:
                            name=input("Enter account Name: ")
                            for use in dvbl.get:
                                if use.name==name:
                                    passw=input("Password:")
                                    if use.password==passw:
                                        dvbl.remove_account(name,passw)
                                        print("Account is deleted")
                                        break
                                    
                                
                        
                        if t==3:
                            for use in dvbl.get:
                                print(use)
                        if t==4:
                            for use in dvbl.get:
                                dvbl.balance(use.available_balance)
                        
                            print(dvbl.Total_balance)
                        if t==5:
                            for use in dvbl.get:
                                dvbl.Total_loan +=use.loan_balance
                            
                            print("Total Lone: {}".format(dvbl.Total_loan))
                        if t==6:
                            loan_f=int(input('1: loanfeature On '))
                            loan_f=int(input('0: loanfeature Off '))
                            
                        if t==7:
                            break
                else:
                    print("Invalid Password and try again")
            if cnt==1:
                break        
        if cnt==0:
            print("Invalid Account")  


    if a==2:
        print("user Interface")
        print("0: Create New Bank account")
        print('1: Login ')
        print('2: Exit ')
        while True:
            n=int(input("Enter Option: "))
            if n==0:
                print('if You want to Create a Savings account press 1')
                print("if You want to create a Current account press 2")
                s=int(input())
                if s==1 or s==2:
                    name=input("Account Name: ")
                    for user in dvbl.get:
                        if user.name == name:
                            print('This Name is already exist')
                            break
                        else:
                            person=Account(name,input('Email: '),input("Address "),input("Password "),'Savings')
                            print (" New account is created . Account Number is: {}".format(person.accountNo))
                            dvbl.add_account(person)  
                            break
            if n==1:
                count=0
                name=input("Enter Your name(user): ")
                for user in dvbl.get:
                    if name==user.name:
                        count=1
                        print(user.password)
                        passw=input("Enter your password: ")
                        if user.password == passw:
                            n=random.randint(1000,9999)
                            print("Your OTP is {}".format(n))
                    
                            p=int(input())
                            if n==p:
                                print("You Logged in")
                                print('0: Account Info')
                                print("1: Deposite ")
                                print("2: Withdraw  ")
                                print("3: Available Balance ")
                                print("4: Transiction ")
                                print("5: Loan")
                                print("6: See Tranjection Histry")
                                print("7: Logg out")
                                while True:
                                    f=int(input("Enter opption: "))
                                    if f==0:
                                        print(user.accountNo)
                                    if f==1:
                                        user.deposit(int(input("Deposit Amount: ")))
                                    elif f==2:
                                        user.withdraw(int(input("Withdraw Amount: ")))
                                    elif f==3:
                                        print(user.available_balance)
                                    elif f==4:
                                        send=user.name
                                        receive=input("Name: ")
                                        amount=int(input("Amount: "))
                                        t=(send,receive,amount)
                                        count=0
                                        for use in dvbl.get:
                                            if use.name ==receive:
                                                count=1
                                                use.deposit(amount)
                                                use.Trshistry.append(t)
                                                break
                                        if count ==0:
                                            print("Account Does Not Exist ")
                                        if count==1:    
                                            user.withdraw(amount)
                                            user.Trshistry.append(t)
                                            
                                    elif f==5:
                                        if loan_f==0:
                                            print("Loan Sceame off")
                                        if loan_f==1:
                                            user.loan(int(input("Apply Loan amount: ")))
                                    elif f==6:
                                        for use in dvbl.get:
                                            if use.name==user.name:
                                                for i in use.Trshistry:
                                                    print(i)
                                                break
                                    elif f==7:
                                        break
                            else:
                                print("Invalid OTP")
                        else:
                            print("Incorrect Password")
                    if count==1:
                        break
                if count ==0:
                    print('Invalid account')
            
    
             
            if n==2:
                break
    if a==3:
        break
            
            
        


    
        
        
        