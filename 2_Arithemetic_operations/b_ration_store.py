"""
Purpose: Ration Store

    -----------------------------------------------
    item    cost        quantity        Amount
    -----------------------------------------------
    wheat   40/kg       80 kgs      40 * 80 = 3200/-
    Rice    20/kg       60 kgs      20 * 60 = 1200/-
                                -------------------
                                              4400/-
                                subsidy 20%   880/-
                                --------------------
                                BillableAmount:3520/-

Algorithm
---------
Step 1:  Get the cost of items into variables
Step 2:  Get the quantity of items into variables
Step 3:  Compute the selling price to each item,
         and add them
Step 4:  Compute the subsidy amount and subtract
         from the selling price
Step 5:  Display the Billable Amount

"""

# cost of Items
cost_of_wheat = 40
cost_of_rice = 20

# Quantities of Items
qty_of_wheat = 80  # kgs
qty_of_rice = 60  # kgs


# Selling Price Computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
# print(total_sp)
print("Total Selling Price:", total_sp)


# Subsidy calculation at 20 % subsidy
subsidy_amount = (total_sp * 20)/ 100 # PEMDAS
print("Subsidy Amount     :", subsidy_amount)


billable_amount = total_sp - subsidy_amount
print("Billable Amount    :", billable_amount)