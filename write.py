from read import *


def change_quantity_after_sales(input_identity, input_lap):
    '''change the quantity of the laptop after selected for sales'''
    laptop_dict = file_read()
    laptop_dict[input_identity][3] = int(laptop_dict[input_identity][3]) - input_lap
    laptop_dict[input_identity][3] = " " + str(laptop_dict[input_identity][3])
    file1 = open("Inventory.txt", "w")
    for values in laptop_dict.values():
            
        file1.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file1.write("\n")
    file1.close()



def change_quantity_after_purchase(input_identity, input_lap):
    '''change the quantity of laptops after purchase'''
    laptop_dict = file_read()
    laptop_dict[input_identity][3] = int(laptop_dict[input_identity][3]) + input_lap
    laptop_dict[input_identity][3] = " " + str(laptop_dict[input_identity][3])
    file1 = open("Inventory.txt", "w")
    for values in laptop_dict.values():
            
        file1.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file1.write("\n")
    file1.close()






def text_invoice(name, phone_number, date_time, laptops_sales, total, shipping_cost, total_with_shipping_cost):


    '''Produces a txt file for the invoice after sales'''

    sales = open("sales_" + str(name) + "_" + str(phone_number) + ".txt" , "w")


    
    sales.write("\n")
    sales.write("\t\t\t\t\t TechZone Invoice")
    sales.write("\n")
    sales.write("\t\t\t Phone Number : 980000000 | Putalisadak Kamal Marg, Street 5")
    sales.write("\n")
    sales.write("-"*90)
    sales.write("\n")
    sales.write("\t\t\t PURCHASE INFO \n")
    sales.write("Name of Buyer             : " + str(name) + "\n")
    sales.write("Buyers Contact Number     : " + str(phone_number) + "\n")
    sales.write("Date and Time of Purchase : " + str(date_time) + "\n")
    sales.write("-"*95)
    sales.write("\n")
    sales.write("-"*95)
    sales.write("\n")
    sales.write("Sn \t Item Name \t\t Manufacturer \t    Quantity \t Unit Price \t Total\n")
    sales.write("-"*95)
    sales.write("\n")
    S_no = 1
    for laptops in laptops_sales:
        
        sales.write(str(S_no) + " \t  " + str(laptops[0]) + " \t   " + str(laptops[1])  + " \t        " + str(laptops[2]) + " \t         " + str(laptops[3]) + " \t\t" + str(laptops[4]) +  "\n")
        S_no += 1
        
    sales.write("\n")
    sales.write("-"*95)
    sales.write("\n")
    sales.write("Gross Amount     : " + "$" + str(total) + "\n")
    sales.write("Shipping Cost    : " + "$" + str(shipping_cost) + "\n")
    sales.write("Net Total        : " + "$" + str(total_with_shipping_cost))
    sales.write("\n")
    sales.write("-"*95)
    sales.write("\n")
    sales.write("\t\t WELCOME TO GREAT SHOPPING EXPERIENCE WITH TECHZONE LAPTOPS PVT. LTD.\n")
    sales.write("\t\t EXCHABGE IN 7 DAYS WITH INVOICE BETWEEN 10-8\n")
    sales.write("\t\t\t\t **CONDITIONS APPLY**\n")
    sales.write("-"*95)
    sales.write("\n\t\t\t\t HAVE A NICE DAY :-)\n")
    sales.write("-"*95)
    sales.close()





def text_invoice_after_purchase(name, date_time, laptops_purchased, total, vat_amount, total_with_vat):
    '''generate a txt file of purchased items'''

    
    purchase = open("purchase" + "_" + str(name) + ".txt" , "w")


    
    purchase.write("\n")
    purchase.write("\t\t\t East or west we are best Suppliers")
    purchase.write("\n")
    purchase.write("\t\t\t\tThamel, street 5")
    purchase.write("\t\t\t\tVat No : 30780000\n")
    purchase.write("-"*90)
    purchase.write("\n")
    purchase.write("\t\t\t PURCHASE INFO \n")
    purchase.write("Name of Buyer             : " + "TechZone Laptops Pvt. ltd." + "\n")
    purchase.write("Buyers Contact Number     : " +"980000000" + "\n")
    purchase.write("Date and Time of Purchase : " + str(date_time) + "\n")
    purchase.write("VAT no.                   : " + "30789564" +  "\n")
    purchase.write("-"*95)
    purchase.write("\n")
    purchase.write("-"*95)
    purchase.write("\n")
    purchase.write("Sn \t Item Name \t\t Manufacturer \t    Quantity \t Unit Price \t Total\n")
    purchase.write("-"*95)
    purchase.write("\n")
    S_no = 1
    for laptops in laptops_purchased:
        
        purchase.write(str(S_no) + " \t  " + str(laptops[0]) + " \t   " + str(laptops[1])  + " \t        " + str(laptops[2]) + " \t         " + str(laptops[3]) + " \t\t" + str(laptops[4]) +  "\n")
        S_no += 1
        
    purchase.write("\n")
    purchase.write("-"*95)
    purchase.write("\n")
    purchase.write("Gross Amount     : " + "$" + str(total) + "\n")
    purchase.write("VAT Amount       : " + "$" + str(vat_amount) + "\n")
    purchase.write("Net Total        : " + "$" + str(total_with_vat))
    purchase.write("\n")
    purchase.write("-"*95)
    purchase.write("\n")
    purchase.write("\t\t WELCOME TO GREAT SHOPPING EXPERIENCE WITH East or west we are best Suppliers\n")
    purchase.write("\t\t EXCHABGE IN 7 DAYS WITH INVOICE BETWEEN 10-8\n")
    purchase.write("\t\t\t\t **CONDITIONS APPLY**\n")
    purchase.write("-"*95)
    purchase.write("\n\t\t\t\t HAVE A NICE DAY :-)\n")
    purchase.write("-"*95)
    purchase.close()
    
