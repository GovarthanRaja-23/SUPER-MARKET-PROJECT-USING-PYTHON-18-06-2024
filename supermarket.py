import re
import datetime
import bakery,vegetables,dairy,beverage
def market():
    print("------>WELCOME TO MR.BEAST SUPERMARKET<------")
    all_products=open("products.txt","r")
    prod=all_products.read()
    print("\nTHE SECTIONS IN THIS SUPERMARKET ARE:")
    print("\nBakery -> 1\nVegetables -> 2\nDairy products -> 3\nBeverages -> 4")
    with open('bill.txt', 'w') as bill_file:
        bill_file.write("")
    def enter():
        try:
            section=int(input("\nENTER WHICH SECTION YOU WANT TO ENTER : "))
            if section==1:
                print("\n==> WELCOME TO THE BAKERY SECTION <==")
                print("THE PRODUCTS PRESENT HERE ARE ==>")
                print("\nBread=40\nCookies=20\nPizza=90\nBurger=110\nDonuts=50")
                bakery.prod_present()
                again=input("\nDO YOU WANT TO PURCHASE AGAIN [yes] (OR) FINISH THE PURCHASE [no] : ")
                if again=="yes":
                    enter()
                elif again=="no":
                    import smtplib
                    def mail():
                        try:                       
                            your_mail=input("PLEASE ...Enter your Mail I'D SIR/MAM to recieve your bill to your Mail : ")
                            op=smtplib.SMTP("smtp.gmail.com",587)
                            op.starttls()
                            #please enter Mail I'D and app password to run this code
                            op.login("","")
                            bill_file=open("bill.txt","r")
                            bill_content = bill_file.read()
                            subject = "Your Purchase Bill from Mr. Beast Supermarket"
                            body = f"Subject: {subject}\n\n{bill_content}\n\nTHANKS FOR COMING TO THE MR.BEAST SUPERMARKET"
                            #Enter the mail I'D you provided above to run this code
                            op.sendmail("",your_mail,body)
                            op.quit()
                            print("------>MAIL IS SENT TO THE CUSTOMER<------")
                        except Exception as e:
                            print("MAIL IS NOT SENT TO THE CUSTOMER DUE TO WRONG MAIL I'D (OR) SOME ERRORS")
                    mail()
                    print("\n------>THANKS FOR COMING TO THE MR.BEAST SUPERMARKET<------")
            elif section==2:
                print("\n==> WELCOME TO THE VEGETABLE SECTION <==")
                print("THE PRODUCTS PRESENT HERE ARE ==>")
                print("\nPotato=70\nTomato=40\nCabbage=25\nCarrot=50\nCauliflower=30")
                vegetables.prod_present()
                again=input("\nDO YOU WANT TO PURCHASE AGAIN [yes] (OR) FINISH THE PURCHASE [no] : ")
                if again=="yes":                 
                    enter()
                elif again=="no":
                    import smtplib
                    def mail():
                        try:                       
                            your_mail=input("PLEASE ...Enter your Mail I'D SIR/MAM to recieve your bill to your Mail : ")
                            op=smtplib.SMTP("smtp.gmail.com",587)
                            op.starttls()
                            #please enter Mail I'D and app password to run this code
                            op.login("","")
                            bill_file=open("bill.txt","r")
                            bill_content = bill_file.read()
                            subject = "Your Purchase Bill from Mr. Beast Supermarket"
                            body = f"Subject: {subject}\n\n{bill_content}\n\nTHANKS FOR COMING TO THE MR.BEAST SUPERMARKET"
                            #Enter the mail I'D you provided above to run this code
                            op.sendmail("",your_mail,body)
                            op.quit()
                            print("------>MAIL IS SENT TO THE CUSTOMER<------")
                        except Exception as e:
                            print("MAIL IS NOT SENT TO THE CUSTOMER DUE TO WRONG MAIL I'D (OR) SOME ERRORS")
                    mail()
                    print("\n------>THANKS FOR COMING TO THE MR.BEAST SUPERMARKET<------")
            elif section==3:
                print("\n==> WELCOME TO THE DAIRY PRODUCTS SECTION <==")
                print("THE PRODUCTS PRESENT HERE ARE ==>")
                print("\nMilk=40\nCurd=25\nYogurt=35\nCheese=100\nButtermilk=20")
                dairy.prod_present()
                again=input("\nDO YOU WANT TO PURCHASE AGAIN [yes] (OR) FINISH THE PURCHASE [no] : ")
                if again=="yes":
                    enter()
                elif again=="no":
                    import smtplib
                    def mail():
                        try:                       
                            your_mail=input("PLEASE ...Enter your Mail I'D SIR/MAM to recieve your bill to your Mail : ")
                            op=smtplib.SMTP("smtp.gmail.com",587)
                            op.starttls()
                            #please enter Mail I'D and app password to run this code
                            op.login("","")
                            bill_file=open("bill.txt","r")
                            bill_content = bill_file.read()
                            subject = "Your Purchase Bill from Mr. Beast Supermarket"
                            body = f"Subject: {subject}\n\n{bill_content}\n\nTHANKS FOR COMING TO THE MR.BEAST SUPERMARKET"
                            #Enter the mail I'D you provided above to run this code
                            op.sendmail("",your_mail,body)
                            op.quit()
                            print("------>MAIL IS SENT TO THE CUSTOMER<------")
                        except Exception as e:
                            print("MAIL IS NOT SENT TO THE CUSTOMER DUE TO WRONG MAIL I'D (OR) SOME ERRORS")
                    mail()
                    print("\n------>THANKS FOR COMING TO THE MR.BEAST SUPERMARKET<------")
            elif section==4:
                print("\n==> WELCOME TO THE BEVERAGES SECTION <==")
                print("THE PRODUCTS PRESENT HERE ARE ==>")
                print("\nWater=30\nPepsi=40\nCocacola=40\nColdcoffeee=60\nFruitjuice=50")
                beverage.prod_present()
                again=input("\nDO YOU WANT TO PURCHASE AGAIN [yes] (OR) FINISH THE PURCHASE [no] : ")
                if again=="yes":
                    enter()
                elif again=="no":
                    import smtplib
                    def mail():
                        try:                       
                            your_mail=input("PLEASE ...Enter your Mail I'D SIR/MAM to recieve your bill to your Mail : ")
                            op=smtplib.SMTP("smtp.gmail.com",587)
                            op.starttls()
                            #please enter Mail I'D and app password to run this code
                            op.login("","")
                            bill_file=open("bill.txt","r")
                            bill_content = bill_file.read()
                            subject = "Your Purchase Bill from Mr. Beast Supermarket"
                            body = f"Subject: {subject}\n\n{bill_content}\n\nTHANKS FOR COMING TO THE MR.BEAST SUPERMARKET"
                            #Enter the mail I'D you provided above to run this code
                            op.sendmail("",your_mail,body)
                            op.quit()
                            print("------>MAIL IS SENT TO THE CUSTOMER<------")
                        except Exception as e:
                            print("MAIL IS NOT SENT TO THE CUSTOMER DUE TO WRONG MAIL I'D (OR) SOME ERRORS")
                    mail()
                    print("\n------>THANKS FOR COMING TO THE MR.BEAST SUPERMARKET<------")
            else:
                print("\nEnter Section Number from the provided Options only...")
        except ValueError:
            print("\nPlease...! Enter Only Section Numbers...")
            enter()
    enter()
market()