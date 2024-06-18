import re
import datetime
bread=40
cookies=20
pizza=90
burger=110
donuts=50
all_products=open("products.txt","r")
prod=all_products.read()
def prod_present():
    gst_rate=15
    discount=10
    bake_product=input("\nEnter the product You want to buy : ")
    find_product=re.search(bake_product,prod)
    if find_product:
        print(f"The Stock of the Bakery Product - {bake_product} you have requested is Here")
        if bake_product=="bread":
            quantity=int(input("Enter how many packs of bread you want : "))
            original_amt=bread*quantity
            gst_amt=(original_amt*gst_rate)/100
            discount_amt=(discount*original_amt)/100
            total_amt=original_amt+gst_amt-discount_amt
            print(f"You have ordered {bake_product} of {quantity} packs with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
            with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {bake_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif bake_product=="cookies":
             quantity=int(input("Enter how many packs of cookies you want : "))
             original_amt=cookies*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {bake_product} of {quantity} packs with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {bake_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif bake_product=="pizza":
             quantity=int(input("Enter how many Pizza's you want : "))
             original_amt=pizza*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {bake_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {bake_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif bake_product=="burger":
             quantity=int(input("Enter how many Burger's you want : "))
             original_amt=burger*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {bake_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {bake_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif bake_product=="donut":
             quantity=int(input("Enter how many Donut's you want : "))
             original_amt=donuts*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {bake_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {bake_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")

    else:
        print(f"The Stock of the Product{bake_product}you have requested is Finished")