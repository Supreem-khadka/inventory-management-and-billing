from read import *
from write import *
from datetime import *


def validate_id_quantity_add_more( name_buyer, phone_buyer):
    '''take user input to produce bill, validate and produce a bill'''
    item_added = False # to check if items are added
    
    name = name_buyer
    phone_number = phone_buyer
    
       
    
    laptops_sales = [] #creating a list to store the  laptops sales info 
    sales_loop = True #to let the user more items

    
    while sales_loop:
        #validating the id
        while True:
            try:
                
                input_id = int(input("Provide the Id of the laptop you will like to purchase: "))


                my_laptop_dictionary = file_read()#calling the function to get the dictionary
                        
                while input_id <= 0 or input_id > len(my_laptop_dictionary):
                    print("Invalid!!! Enter a valid id\n")
                    input_id = int(input("Provide the id of the laptop you will like to purchase: "))
                    
                break
            
            except ValueError:
                print("Invalid\nPlease enter a valid laptop id") 

                

        
        
        

                  #validate quantity        
        while True:
            try:
                
                input_quantity = int(input("Enter the quantity of laptop you would like to purchase: "))

                get_selected_laptops_quantity = int(my_laptop_dictionary[input_id][3])
                    
                while input_quantity <= 0 or input_quantity > get_selected_laptops_quantity:

                    #checking if the laptop quantity is zero
                    if get_selected_laptops_quantity == 0:
                        print("Sorry the selected laptop " + my_laptop_dictionary[input_id][0] + " is out of stock" )
                        break       
                                    

                    #for the user doesnot enter 0 as a quantity         
                    elif input_quantity <= 0:
                        print("The quantity ",input_quantity,"is invalid!!. Minimum quantity is 1")
                        input_quantity = int(input("Enter the quantity of laptop you would like to purchase: "))
                    # so user doesnot add more than available laptops
                    elif input_quantity > get_selected_laptops_quantity:
                        print("The quantity ",input_quantity,"is invalid!!!. Maximum quantity available is",get_selected_laptops_quantity)
                        input_quantity = int(input("Enter the quantity of laptop you would like to purchase: "))

                        
                break

            except ValueError:
                print("Invalid \nThe quantity should be a number") 
                
                    

      
        
        print("\n")
        


               
        if get_selected_laptops_quantity >= input_quantity and get_selected_laptops_quantity != 0:
                        
            change_quantity_after_sales(input_id, input_quantity)# reduce the quantity of the laptops purchased

           
            name_of_product = my_laptop_dictionary[input_id][0]
            selected_quantity = input_quantity
            manufacturer = my_laptop_dictionary[input_id][1]
            price_per_unit = my_laptop_dictionary[input_id][2]
            price_per_unit_without_string = price_per_unit.replace("$","")
            total_price = int(price_per_unit_without_string)*int(selected_quantity)
            total_price_with_string = "$"+str(total_price)

            
            same = False  #to check same purchased laptops doesnot get added seperately 
            for laptops in laptops_sales:
                if laptops[0] == my_laptop_dictionary[input_id][0]:
                    laptops[2] = laptops[2] + selected_quantity #increasing the quantity if the name matches
                    #changing the total
                    total = laptops[4].replace("$","")
                    int_total = int(total)
                    new_total = int_total + total_price
                    laptops[4] = "$"+str(new_total)
                    print("Your order",name_of_product,"of quantity", selected_quantity,"has been successfully placed in the cart")
                    same = True
                    break
                
            if same == False:
                laptops_sales.append([name_of_product, manufacturer, selected_quantity, price_per_unit,  total_price_with_string])
                print("Your order",name_of_product,"of quantity", selected_quantity,"has been successfully placed in the cart")
                item_added = True
                

            
            
            


        #checks if the inventory in out of stock and stops from a infinte loop because if there is item you can not generate a bill and without a bill you cannot exit a system
        quantity_sum = 0
        for id in my_laptop_dictionary:
            quantity_sum += int(my_laptop_dictionary[id][3])

        if quantity_sum == 0 and item_added == False:  #only gets executed if there is no laptops purchased because if the there is no laptop in the stock we will be stuck in a infinte loop because the bill will not be generated unless their is atleast 1 item 
            print("\t\t SORRY FOR THE INCONVINIENCE!!!!\n\t\t WE ARE CURRENTLY OUT OF STOCK\n\n")
            break
          
       
        
               
        

        
        while True:           
            more = input("Would you like to purchase more(y/n): ")
            if more.lower() == "y":
                print("\n")
                break
            elif more.lower() == "n":
                if item_added == True: # to make sure that the bill only gets generated if there is atleast one items that has been purchased

                    
                    generate_bill(laptops_sales, name, phone_number)

                    
                    
                    


                    

                    
                    sales_loop = False
                    break



                else:
                    print("\t\t YOU HAVE NO ITEMS IN THE CART YET\n\t\t YOU MUST HAVE ATLEAST ONE ITEM TO GENERATE A BILL")
                    
                
            else:
                print("Invalid!!!")




    
    
def generate_bill(laptops_sales, name_buyer, phone_number_buyer):
    '''to generate a bill for all the selected items with shipping cost'''
    name = name_buyer
    phone_number = phone_number_buyer
    total = 0
    cost_shipping = 60
    laptops_sale = laptops_sales
    for laptops in laptops_sale:
        total += int(laptops[4].replace("$",""))
    total_with_cost_shipping = total + cost_shipping
    date_time = datetime.now()
    

                        
    print("\n")
    print("-"*90)
    print("\t\t\t   TechZone Laptops PVT. LTD.\n")
    print("\t\t\tPutalisadak, Kamal Marg, street 5")
    print("\t\t\t\tVat No : 30789564")
    print("\t\t\t     ABBREVIATED TAX INVOICE\n\n")
    print("Transaction Date : " + str(date_time))
    print("Invoice Date     : " + str(date_time))
    print("Bill To          : " + str(name))
    print("Contact number   : " + str(phone_number))
    print("Payment Mode     : Cash\n")
    print("-"*90)
                        
    print("Sn \t Item Name \t\t Manufacturer \t    Quantity \t Unit Price \t Total")
    print("-"*90)
    S_no = 1
    for laptops in laptops_sale:
        print(S_no,"\t",laptops[0],"\t  ",laptops[1],"\t       ",laptops[2],"\t   ",laptops[3], "\t ", laptops[4])
        S_no += 1
                            
    print("\t\t\t\t\t","-"*49)
    print("\t\t\t\t\t\t\t      Gross Amount       :" , "$" + str(total))
    print("\t\t\t\t\t\t\t      Shipping Cost      :" , "$" + str(cost_shipping))
    print("\t\t\t\t\t\t" + "-"*42)
    print("\t\t\t\t\t\t\t      Net Total          :" , "$" + str(total_with_cost_shipping))
    print("\n")
    print("-"*90)
    print("\t\t WELCOME TO GREAT SHOPPING EXPERIENCE WITH TECHZONE LAPTOPS PVT. LTD.")
    print("\t\t EXCHABGE IN 7 DAYS WITH INVOICE BETWEEN 10-8")
    print("\t\t\t\t **CONDITIONS APPLY**\n")
    print("-"*90)
    print("\t\t\t\t HAVE A NICE DAY :-)")
    print("-"*90)
    print("\n")

    # to generate a text file 
    text_invoice(name, phone_number, date_time, laptops_sale, total, cost_shipping, total_with_cost_shipping)





def purchase(name_purchase):
    '''take user input related to purchase and add to the list'''
    name = name_purchase
     
    purchase_loop = True

    laptops_purchased = [] # to keep record of purchased laptops
    while purchase_loop:
        while True:
            try:
                
                purchase_id = int(input("Provide the Id of the laptop you will like to purchase: "))

                        #validating the id
                laptop_purchase_dictionary = file_read()#calling the function to get the dictionary
                        
                while purchase_id <= 0 or purchase_id > len(laptop_purchase_dictionary):
                    print("Invalid!!! Enter a valid id\n")
                    purchase_id = int(input("Provide the id of the laptop you will like to purchase: "))

                break
            
            
            except ValueError:
                print("Invalid\nPlease enter a valid laptop id")
                



        #Quantity
        while True:
            try:
                
                purchase_quantity = int(input("Enter the quantity of laptop you would like to purchase: "))

                if purchase_quantity <= 0:
                    print("Invalid!!!!\n Minimum quantity is 1")
                    
                
                if purchase_quantity > 0:
                    change_quantity_after_purchase(purchase_id, purchase_quantity)
                    break
                

            except ValueError:
                print("Invalid!!!\nThe quantity should be a number")



        
        
        name_of_product = laptop_purchase_dictionary[purchase_id][0]
        selected_quantity = purchase_quantity
        manufacturer = laptop_purchase_dictionary[purchase_id][1]
        price_per_unit = laptop_purchase_dictionary[purchase_id][2]
        price_per_unit_without_string = price_per_unit.replace("$","")
        total_price = int(price_per_unit_without_string)*int(selected_quantity)
        total_price_with_string = "$"+str(total_price)


        


        same = False #to check same purchased laptops doesnot get added seperately 
        for laptops in laptops_purchased:
            if laptops[0] == laptop_purchase_dictionary[purchase_id][0]:
                #change the quantity
                laptops[2] = laptops[2] + selected_quantity
                #change the total
                laptop_total = laptops[4].replace("$","")
                int_laptop_total = int(laptop_total)
                new_total = int_laptop_total + total_price
                laptops[4] ="$"+str(new_total)
                print("Your order",name_of_product,"of quantity", selected_quantity,"has been successfully placed in the cart")
                same = True
                break
        if same == False:
            laptops_purchased.append([name_of_product, manufacturer, selected_quantity, price_per_unit,  total_price_with_string])
            print("Your order",name_of_product,"of quantity", selected_quantity,"has been successfully placed in the cart")
            item_added = True


        while True:           
            more = input("Would you like to purchase more(y/n): ")
            if more.lower() == "y":
                print("\n")
                break
            elif more.lower() == "n":
                if item_added == True: # to make sure that the bill only gets generated if there is atleast one items that has been purchased

                    generate_bill_purchase(laptops_purchased, name)
                    

                    
                    
                    


                    

                    
                    purchase_loop = False
                    break



                else:
                    print("\t\t YOU HAVE NO ITEMS IN THE CART YET\n\t\t YOU MUST HAVE ATLEAST ONE ITEM TO GENERATE A BILL")
                    
                
            else:
                print("Invalid!!!")




def generate_bill_purchase(laptops_purchased_purchase, name_purchase):
    '''generate invoice as well as a .txt file'''

    name = name_purchase
    laptops_purchased = laptops_purchased_purchase
    total = 0
    
    for laptops in laptops_purchased:
        total += int(laptops[4].replace("$",""))
    vat_amount = (13/100) * total
    total_with_vat = total + vat_amount
    date_time = datetime.now()



   
    
    
                        
    print("\n")
    print("-"*98)
    print("\t\t\tEast or west we are best Suppliers\n")
    print("\t\t\t\t Thamel, street 5")
    print("\t\t\t\tVat No : 30780000")
    print("\t\t\t     ABBREVIATED TAX INVOICE\n\n")
    print("Transaction Date : " + str(date_time))
    print("Invoice Date     : " + str(date_time))
    print("Bill To          : " + "TechZone Laptops Pvt. ltd.")
    print("Contact number   : " + "980000000")
    print("VAT no.          : " + "30789564")
    print("Payment Mode     : Credit\n")
    print("-"*98)
                        
    print("Sn \t Item Name \t\t Manufacturer \t    Quantity \t Unit Price \t Total")
    print("-"*98)
    S_no = 1
    for laptops in laptops_purchased:
        print(S_no,"\t",laptops[0],"\t  ",laptops[1],"\t       ",laptops[2],"\t   ",laptops[3], "\t ", laptops[4])
        S_no += 1
                            
    print("\t\t\t\t\t","-"*57)
    print("\t\t\t\t\t\t\t      Gross Amount       :" , "$" + str(total))
    print("\t\t\t\t\t\t\t      VAT Amount         :" , "$" + str(vat_amount))
    print("\t\t\t\t\t\t" + "-"*57)
    print("\t\t\t\t\t\t\t      Net Total          :" , "$" + str(total_with_vat))
    print("\n")
    print("-"*98)
    print("\t\t WELCOME TO GREAT SHOPPING EXPERIENCE WITH East or west we are best Suppliers")
    print("\t\t EXCHABGE IN 7 DAYS WITH INVOICE BETWEEN 10-8")
    print("\t\t\t\t **CONDITIONS APPLY**\n")
    print("-"*98)
    print("\t\t\t\t HAVE A NICE DAY :-)")
    print("-"*98)
    print("\n")

    text_invoice_after_purchase(name,date_time, laptops_purchased, total, vat_amount, total_with_vat)
    

