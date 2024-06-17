def welcome():
    """for printing out the greeting"""

    print("\n")
    print("\t\t\t TechZone Laptops PVT. LTD.")
    print("\t\t\tPutalisadak, Kamal Marg, street 5")
    print("\t\t\t\tVAT No : 30789564")
    print("\n\n")
    print("Welcome back to the system :)\n\n")


def file_read():
    """reading form the text file Inventory.txt and adding them to a dictionary """
    file = open("Inventory.txt", "r")#open
    laptop_dictionary = {}
    laptop_id = 1
    for line in file:
        
        line = line.replace("\n", "")
        laptop_dictionary.update({laptop_id: line.split(",")})#addind into the dictionary a key value pair where "laptopId" is the key and value is obtained by spliting the line
        laptop_id += 1

    file.close()#close
    return laptop_dictionary
    
def display_inventory():
    """for displaying in table like format for user to view and select"""
    print("-"*90)
    print("Id\tLaptop\t\tManufacturer\t  Price   Qty\t  Processor\tGraphics Card")
    print("-"*90)
    file = open("Inventory.txt", "r")#open
    a = 1
    for line in file:
        print(a, "\t"+line.replace(",","\t"+" "))
        print("-"*90)
        a += 1
        
    file.close()#close

    print("\n")



