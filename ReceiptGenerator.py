#To create Receipt/Bill Generator for any General Store.]

#this module will be imported.
from ReceiptLayoutModule import receipt

option = 1
bill_no = 1
while(option==1):
    #taking input customer details
    print("")
    print("Bill No. :",bill_no)
    cust_name = input("Enter Customer Name = ")
    cust_phone = int(input("Enter Customer Phone-Number = "))
    #A List to store items.
    n = int(input("Enter Total no. of items he/she bought = "))
    items = []

    #Taking input for all item names and their prices.
    for i in range(0,n):
        print("For Item-",i+1," : ",sep="")
        name = input("     Enter Item Name = ")
        price = int(input("     Enter Item Price (in Rs.) = "))
        #appending these all item in list.
        items.append([name, price])

    #Now passing items[] to receipt() function, that will return a "Bill/Receipt" (as a string) with well INDENTATION.
    ans = receipt(items, cust_name, cust_phone, bill_no)
    print("\nFinal Bill : ")
    print(ans)

    #Writing abive returned Bill/Receipt(string) to a new or pre-existing ".txt" file of name Receipt.pdf
    f = open(f"Receipt_{bill_no}.txt", "w+")
    f.write(ans)
    print(f.read)
    f.close()

    #asking for next bill
    option = int(input("Press : 1 to create next bill or 0 to Exit = "))
    bill_no += 1

print("\n******************************************* OVER *************************************************")