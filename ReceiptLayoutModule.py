#This module will basically contain the "LAYOUT OF BILL/RECEIPT" to be generated for that particular store.

import datetime

#This function will return final Bill/Recipt as a string (with full indentation).
#item[0] = Item Name, item[1] = Item Price
def receipt(items, cust_name, cust_phone, bill_no):
    max_name_len = -1       #will be used for spacing purpose.   
    total = 0               #total bill amount.
    for item in items:       
        total += item[1]                  
        if(len(item[0]) > max_name_len):
            max_name_len = len(item[0])

    item_name = "ITEM NAME"   #will be used for spacing purpose.
    item_price = "PRICE (Rs.)"
    total_amt = "TOTAL Amt"

    space_len = max(max_name_len+5, len(item_name)+5)  #space for item_name_word.

    ans = ""
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"

    ans += "\n|        ABC General Store" + "%14s"%"|"
    ans += "\n|      NIT Market, Kurukshetra" + "%10s"%"|"
    ans += "\n|         +91 85476 149XX" + "%15s"%"|"

    # for for dash ----- 
    ans += "\n"
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"

    ans += f"\n|  Receipt No. : %{-19}s"%bill_no + "%4s"%"|"
    ans += f"\n|  Date : {datetime.datetime.now()}" + "%4s"%"|"
    ans += f"\n|  Customer-Name : %{-19}s"%cust_name + "%2s"%"|"
    ans += f"\n|  Mobile-No. : %{-19}d"%cust_phone + "%5s"%"|"

    ans += "\n"
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"

    #       <------Left side ----------------->         <------Right side------->
    ans += f"\n|     %{-(space_len)}s"%item_name + "|" + f"     %{10}s"%item_price + "  |"

    ans += "\n"
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"
    # appending line for each ITEM of list items[].
    for item in items:
        ans += f"\n|     %{-(space_len)}s"%item[0] + "|" + f"     %{10}d"%item[1] + "   |"


    # again for dash ------- 
    ans += '\n'
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"

    ans += f"\n      %{-(space_len)}s"%total_amt + "|" + f"  Rs.%{10}d"%total
    
    # again for dash ------- 
    ans += '\n'
    for i in range(0,5+space_len+5+1+5+10):
        ans += "-"

    return ans #this returns the final bill/receipt as string.