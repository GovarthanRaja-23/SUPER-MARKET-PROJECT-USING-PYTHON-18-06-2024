import re
import datetime
milk=40
curd=25
yogurt=35
cheese=100
buttermilk=20
all_products=open("products.txt","r")
prod=all_products.read()
def prod_present():
    gst_rate=25
    discount=7
    dairy_product=input("\nEnter the product You want to buy : ")
    find_product=re.search(dairy_product,prod)
    if find_product:
        print(f"The Stock of the Product {dairy_product} you have requested is Here")
        if dairy_product=="milk":
            quantity=int(input("Enter how many Litres of Milk you want : "))
            original_amt=milk*quantity
            gst_amt=(original_amt*gst_rate)/100
            discount_amt=(discount*original_amt)/100
            total_amt=original_amt+gst_amt-discount_amt
            print(f"You have ordered {dairy_product} of {quantity} litre with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
            with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {dairy_product}\n")
                bill_file.write(f"Quantity: {quantity}Lts\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif dairy_product=="curd":
             quantity=int(input("Enter how many packs of Curd you want : "))
             original_amt=curd*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {dairy_product} packs with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {dairy_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif dairy_product=="yogurt":
             quantity=int(input("Enter how many packs of Yogurt you want : "))
             original_amt=yogurt*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {dairy_product} packs with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {dairy_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif dairy_product=="cheese":
             quantity=int(input("Enter how many kilos of Cheese's you want : "))
             original_amt=cheese*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} Kilo's of {dairy_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {dairy_product}\n")
                bill_file.write(f"Quantity: {quantity}Kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif dairy_product=="buttermilk":
             quantity=int(input("Enter how many packs of Buttermilk's you want : "))
             original_amt=buttermilk*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {dairy_product} packs with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {dairy_product}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")

    else:
        print(f"The Stock of the Product{dairy_product}you have requested is Finished")