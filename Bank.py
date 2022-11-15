accounts = []


# Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("User Details")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


# Child Class (This inherits the User class attributes and functions)
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = 0

    def deposits(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Account balance has been updated: {self.balance}")

    def withraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= self.amount
            print(f"Account balance has been updated: {self.balance}")

    def show_balance(self):
        print(f"Account balance is: {self.balance}")


class Admin(Bank):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.num = None
        self.value = None

    def steal(self, num, value):
        self.value = value
        self.num = num
        if self.value > accounts[num].balance:
            print("Insufficient Balance!")
        else:
            self.balance += self.value
            accounts[num].balance -= self.value


def create_user(c):
    name1 = input("What is your name? ")
    age1 = input("What is your age? ")
    gender1 = input("What is your gender? ")
    user = Bank(name1, age1, gender1)
    accounts.append(user)
    print(f"Your user number is : {c}")


adname = "Admin"
adage = 22
adgender = "Male"
admin = Admin(adage, adname, adgender)

# user1 = Bank("Brandon", 12, "Male")
# user1.show_details()
# user1.deposits(200)
# user1.deposits(200)
# user1.withraw(100)
# user1.withraw(500)
# user1.show_balance()

while True:
    option1 = input("Press 1 to start moderating your bank, 2 for project spec or anything else to exit! ")
    if option1 == "1":
        count = 0
        while True:
            option2 = input(
                "\nPress 1 to make a new user, 2 to view the current users, 3 to login, 4 to view account details, 5 if your admin or anything else to exit! ")
            # Create Users
            if option2 == "1":
                create_user(count)
                count += 1
            # Show Users
            elif option2 == "2":
                if len(accounts) == 0:
                    print("No accounts in the system!")
                else:
                    for i in accounts:
                        print(i.name)
            # User Login
            elif option2 == "3":
                if len(accounts) == 0:
                    print("No accounts in the system!")
                    continue
                while True:
                    login = input("\nEnter the user number you want to login to: ")
                    if len(accounts) > int(login):
                        break
                    else:
                        print("invalid input")

                while True:
                    login_choice = input(
                        "\nWould you like to deposit (1), withraw (2), check balance (3) or logout (4): ")
                    if login_choice == "1":
                        dinp = input("How much would u like to deposit: ")
                        accounts[int(login)].deposits(int(dinp))
                    elif login_choice == "2":
                        winp = input("How much would u like to withraw: ")
                        accounts[int(login)].withraw(int(winp))
                    elif login_choice == "3":
                        accounts[int(login)].show_balance()
                    elif login_choice == "4":
                        break
                    else:
                        print("Invalid Input!")
            # View User Information
            elif option2 == "4":
                if len(accounts) == 0:
                    print("No accounts in the system!")
                    continue
                while True:
                    account_show = input("\nEnter the user number you want to see the account info of: ")
                    if len(accounts) > int(account_show):
                        accounts[int(account_show)].show_details()
                        break
                    else:
                        print("invalid input")
            # Admin Login
            elif option2 == "5":
                print("\nBank accounts and their account balance")
                print(f"Admin Account Balance: {admin.balance}")
                for i, val in enumerate(accounts):
                    print(f"UserNumber: {i}       Name: {accounts[i].name}        Balance: {accounts[i].balance}")
                option3 = input("Would you like to steal? {1 for yes, 2 for no}: ")
                if option3 == "1":
                    pass
                else:
                    continue
                while True:
                    steal = input("Enter the user number you want to steal from! ")
                    if steal.isnumeric():
                        break
                    else:
                        print("Invalid Input")
                while True:
                    amount = input("Enter how much you want to steal! ")
                    if steal.isnumeric() and amount.isnumeric():
                        break
                    else:
                        print("Invalid Input")
                admin.steal(int(steal), int(amount))
                print(f"New Admin Balance: {admin.balance}")
            else:
                exit(0)
    elif option1 == "2":
        print('''Project Idea:
* User can make new accounts
* Bank accounts can be viewed and names will be saved somewhere
* User deposit/withraw from account of choice
* Admin can use functions that normal users cant''')
    else:
        exit(0)
