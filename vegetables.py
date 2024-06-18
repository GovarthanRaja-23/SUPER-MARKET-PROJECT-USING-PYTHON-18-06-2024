import re
import datetime
potato=70
tomato=40
cabbage=25
carrot=50
cauliflower=30
all_products=open("products.txt","r")
prod=all_products.read()
def prod_present():
    gst_rate=20
    discount=8
    vegetable_product=input("\nEnter the Vegetable You want to buy : ")
    find_product=re.search(vegetable_product,prod)
    if find_product:
        print(f"The Stock of the Vegetable - {vegetable_product} you have requested is Here")
        if vegetable_product=="potato":
            quantity=int(input("Enter how many Kilos of Potato you want : "))
            original_amt=potato*quantity
            gst_amt=(original_amt*gst_rate)/100
            discount_amt=(discount*original_amt)/100
            total_amt=original_amt+gst_amt-discount_amt
            print(f"You have ordered {vegetable_product} of {quantity} Kilos with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
            with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {vegetable_product}\n")
                bill_file.write(f"Quantity: {quantity}Kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif vegetable_product=="tomato":
             quantity=int(input("Enter how many Kilos of Tomato you want : "))
             original_amt=tomato*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {vegetable_product} of {quantity} Kilos with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {vegetable_product}\n")
                bill_file.write(f"Quantity: {quantity}Kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif vegetable_product=="cabbage":
             quantity=int(input("Enter how many Kilos of Cabbage you want : "))
             original_amt=cabbage*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {vegetable_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {vegetable_product}\n")
                bill_file.write(f"Quantity: {quantity}kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif vegetable_product=="carrot":
             quantity=int(input("Enter how many Kilos of Carrot you want : "))
             original_amt=carrot*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {vegetable_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {vegetable_product}\n")
                bill_file.write(f"Quantity: {quantity}Kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")
        elif vegetable_product=="cauliflower":
             quantity=int(input("Enter how many Kilos of cauliflower you want : "))
             original_amt=cauliflower*quantity
             gst_amt=(original_amt*gst_rate)/100
             discount_amt=(discount*original_amt)/100
             total_amt=original_amt+gst_amt-discount_amt
             print(f"You have ordered {quantity} {vegetable_product} with Gst is {gst_rate}% and the Discount of {discount}%, the Total amount of your purchase is ${total_amt}")
             with open('bill.txt', 'a') as bill_file:
                bill_file.write(f"\nDate and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                bill_file.write(f"Item: {vegetable_product}\n")
                bill_file.write(f"Quantity: {quantity}Kg\n")
                bill_file.write(f"Price: ${total_amt:.2f}\n")
                bill_file.write(f"GST: ${gst_amt:.2f}\n")
                bill_file.write(f"Discount: -${discount_amt:.2f}\n")
                bill_file.write(f"Total Price: ${total_amt:.2f}\n")

    else:
        print(f"The Stock of the Product{vegetable_product}you have requested is Finished")