# inventory-management-and-billing

# INTRODUCTION
A program has been developed in python using idle for a laptop shop whose name is 
“TechZone Laptops Pvt. Ltd.”, to manage the sales and purchase of laptops. A text file 
“Inventory.txt” contains the information about the laptops, their price and available 
quantity. The user can sell laptops to customers as well as purchase laptops from 
suppliers through the use of this program. The user provides the program with the 
inputs like name, phone number, laptops it wants to purchase or sell and the laptops 
quantity. The user selects the option provided and necessary changes are made to the 
text file containing the information regarding the stock of the laptop, it increases the 
quantity of the laptop after purchase and decreases the quantity of laptops after sale. 
And after the user does not want to purchase or sell more laptops an invoice is 
displayed as well as a text file in created containing all the information regarding the 
purchase and the sales including the buyers and sellers’ information. The program will 
operate in a loop until the user commands it to stop. There are 4 different files by the 
name “main.py”, “operations.py”, “read.py” and “write.py”, read.py contains the functions 
to generate a welcome message, and read from the text file, write.py contains functions 
that makes changes to inventory.txt file after the purchase and sales, as well as create 
a text for invoice generated after purchase and sales of laptops, operations.py consists 
of functions to validate the users input, and display the invoice, whereas main.py is 
where the magic happens as all the function are implemented to create a up and 
running system for buying and selling laptops. 
The objective of the program is to be able to sell and purchase laptops through the 
system, make changes to inventory after purchase and sales and generate a text file for 
the invoice, and during all this operation all the program should not crash because of 
any reasons like inappropriate inputs. The program should only stop when the user 
wants it to stop and takes the necessary steps provided as per the instructions. The 
process of buying and selling the laptops should be smooth and appropriate messages 
should be displayed in case of error rather that the system crashing.


# IMPLEMENTATION OF THE PROGRAM
When you first start the program you are greeted with a welcome message which is 
implemented using the function welcome() from read.py. We used a loop to ask for the 
user to choose between buy, purchase and exit until they choose to exit. If the user 
chooses to sell then then they are asked for further information like their name and 
phone number for the purpose of keeping track and generating a bill and a text file for 
the invoice. After the user provides the system with the asked input, the details 
regarding the laptops are provided like laptop id, name, company, price, quantity, 
graphics card and processor are displayed, for this we call the display_inventory() 
function. The display_inventory() reads through the inventory.txt file which contains the 
details regarding the laptops and printing them by replacing the comma with a tab 
space. Then validate_quantity_add_more() function is called. Inside this function an 
empty list is declared to keep the record of purchased laptops. A loop is initiated to end 
only if the user chooses not to purchase more laptops. The user is asked to provide the 
laptop id of the laptop they would like to purchase and after they enter the value if it is 
invalid then an error message is displayed and they are asked to enter the laptop id until 
a valid id is entered. After a valid laptop id is entered, the user is then asked to enter the 
quantity of the laptop they want to purchase. Just like the laptop id, the system will keep 
asking for a valid quantity until the one is entered. After a valid quantity is entered 
change_quantity_after_purchase() is called which writes in the inventory.txt file the 
changes in quantity after the purchase. Then another loop is initiated to check if the 
same laptop is already purchased so that in the bill when the same laptops are 
purchase twice, they are not displayed separately. Then we use for loop and a if 
statement to check the shop is out of stock. After the this the user is asked if they want 
to sell more if these choose sell more the process gets repeated until they don’t want to 
sell more and the bill gets generated for which we call the generate_bill() which 
genenrate the bill and then calls text_invoice() which creates a text file for the bill. For all 
the purchase and sales of laptops we use a dictionary which we created in file_read() 
and we exit the loop we created for selling multiple laptops and are again asked to 
choose between sell, purchase and exit.  If we choose to sell we are asked to provide 
our name and after that the inventory gets displayed when we call display_inventory(). 
After that we call purchase() where a loop is initiated to purchase multiple laptops until 
we want to add no more. A list is used to keep the track of purchase. After the loop is 
initiated we are asked to enter the laptop id and we are asked to enter one until we 
enter a valid laptop id. After that we are asked to enter the quantity and we are asked to 
enter the quantity unless we give the quantity more that zero. After a valid quantity is 
entered we call change_change_after_purchase() which write into inventory.txt to 
increase the quantity of purchased laptops. Then a for loop and if statement is used to 
not add same laptops purchased separately to be printed separately in the bill. After this 
the user is asked if they want to purchase more if they choose to purchase more they 
same process is repeated until they do not want to purchase more, then the 
generate_bill() is called which prints the bill in the terminal and then calls 
28 
text_invoice_after_purchase() than creates a text file of the bill and after this the loop 
ends and  the system ask if we want to sell, purchase and exit. If we choose to exit then 
we are asked again if are sure. If we choose we are sure then we finally exit the system 
as the loop ends.



