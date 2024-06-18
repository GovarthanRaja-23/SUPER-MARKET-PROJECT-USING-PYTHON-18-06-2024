import re
import datetime
water=30
pepsi=40
cocacola=40
coldcoffee=60
fruitjuice=50
all_products=open("products.txt","r")
prod=all_products.read()
def prod_present():
    gst_rate=30
    discount=15
    beverage_products=input("\nEnter the product You want to buy : ")
    find_product=re.search(beverage_products,prod)
    if find_product:
        print(f"The Stock of the Product {beverage_products} you have requested is Here")
        if beverage_products=="water":
            quantity=int(input("Enter how many bottle's of Water you want : "))
            original_amt=water*quantity
            gst_amt=(original_amt*gst_rate)/100
            discount_amt=(discount*original_amt)/100
            total_amt=original_amt+gst_amt-discount_amt
            print(f"You have ordered {quantity} bottle's of {beverage_products} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
            with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {beverage_products}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif beverage_products=="pepsi":
             quantity=int(input("Enter how many bottle's of Pepsi you want : "))
             original_amt=pepsi*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} bottle's of {beverage_products} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {beverage_products}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif beverage_products=="cocacola":
             quantity=int(input("Enter how many bottle's of Cocacola you want : "))
             original_amt=cocacola*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} bottle's of {beverage_products} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {beverage_products}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif beverage_products=="coldcoffee":
             quantity=int(input("Enter how many tin's of Coldcoffee's you want : "))
             original_amt=coldcoffee*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} tin's of {beverage_products} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {beverage_products}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif beverage_products=="fruitjuice":
             quantity=int(input("Enter how many bottle's of fruitjuice's you want : "))
             original_amt=fruitjuice*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} bottle's of {beverage_products} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {beverage_products}\n")
                bill_file.write(f"Quantity: {quantity}\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")

    else:
        print(f"The Stock of the Product{beverage_products}you have requested is Finished")