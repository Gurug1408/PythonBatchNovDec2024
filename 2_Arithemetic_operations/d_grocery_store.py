"""
Purpose: Grocery Store

    Item       cost
    ------------------------
    rice        45/kg
    wheat       65/kg

Algorithm
---------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input()
        -> to get value in run-time
        -> will give any input as string only

"""

# cost of items
cost_of_rice = 45  # per kg
cost_of_wheat = 65  # per kg


# Quantities of Items
qty_of_rice = input("Enter Qty. of Rice  (in Kgs):")
# qty_of_rice = int(qty_of_rice)
qty_of_rice = float(qty_of_rice)
print("Qty of Rice  :", qty_of_rice, type(qty_of_rice))



# qty_of_wheat = input('Enter Qty. of Wheat(in Kgs):')
# qty_of_wheat = float(qty_of_wheat)

qty_of_wheat = float(input("Enter Qty. of Wheat(in Kgs):"))


# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("SP of Rice   :", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("SP of Wheat  :", sp_of_wheat)


total_sp = sp_of_rice + sp_of_wheat
print("Total SP     :", total_sp)