from read import *
from write import *
from operations import *



#header and welcome for the user
welcome()


#displaying options to the user
loop = True
while loop:
    print("Follow the instruction for navigation\n")
    print("\tPress 1 for sales")
    print("\tPress 2 for purchase")
    print("\tPress 3 to exit")
    print("\n\n")
    try:
        
    
        user_input = int(input("Enter the options from above to continue: "))
        print("\n")

        
        
        if user_input == 1:



            print("You are now inside the sales terminal :) \n\n")
        
            print("In order keep track of the purchase and to generate a bill, please provide the details: ")
            print("\n")
            name = input("\tEnter the customers name: ")
            phone_number = input("\tEnter the customers contact number: ")
            print("\n")

            
            display_inventory()  





            
            



            validate_id_quantity_add_more(name, phone_number)

           

            
      
           

    

        elif user_input == 2:


            
            print("You are now inside the purchase terminal :) \n\n")

            name = input("Enter your name : ")
    
            display_inventory()           
           
            purchase(name)


            






        elif user_input == 3:
            end_conti = True
            while end_conti:
                exit = input("Are you sure you want to exit the system (y/n): ")
                if exit.lower() == "y":
                    print("exiting the system......................")
                    print("Successfully exited the system")
                    print("Have a nice day :)")
                    loop = False
                    end_conti = False
                elif exit.lower() == "n":
                    print("")
                    end_conti = False

                else:
                    print("Invalid Input!!!!")
                    
                    

        else:
            print("Your option:", user_input,"is invalid!!!\nPlease try again\n" )
            

    except ValueError:
        print("\nInvalid input!!! Please try again\n")

        
