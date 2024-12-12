"""
Purpose: Electricity Board Current Bill Slab rates

    Electricity bill slabs
    -------------------------------------
    units Range     |    amount per unit
    -------------------------------------
    0 till 50       |   1.50
    50 till 120     |   2.50
    120 till 200    |   5.00
    200 till 300    |   8.00
    300 +           |  12.00

electricity cess : 2%
discount         : -1.11%

GST              : 8%

units consumed : 400
         50     +   70      + 80     + 100    + 100
         1.50/- + 2.50/-   + 5.00/- + 8.00/- + 12/- 

"""
import sys

units_consumed = 400

if units_consumed < 0:
    print("INVALID INPUT")
    sys.exit(0)

# Method 1
if 0 < units_consumed <= 50:
    billable_amount = units_consumed * 1.50
elif 50 < units_consumed <= 120:
    remaining_units  = units_consumed - 50
    billable_amount = 50 * 1.50 + remaining_units * 2.50
elif 120 < units_consumed <= 200:
    remaining_units  = units_consumed - 50 - 70
    billable_amount = 50 * 1.50 + 70 * 2.50 + remaining_units * 5.00
elif 200 < units_consumed <= 300:
    remaining_units  = units_consumed - 50 - 70 - 80
    billable_amount = 50 * 1.50 + 70 * 2.50 + 80 * 5.00 + remaining_units * 8.00
elif units_consumed > 300:
    remaining_units  = units_consumed - 50 - 70 - 80 - 100
    billable_amount = 50 * 1.50 + 70 * 2.50 + 80 * 5.00 + 100 * 8.00 + remaining_units * 12.00

print(f"""
            units consumed  : {units_consumed}
            Amount          : {billable_amount}
        """)

# Method 2
amount = 0
remaining_units = units_consumed

if units_consumed > 300:
    slab_units = remaining_units - 300
    amount += slab_units * 12.0
    remaining_units -= slab_units

if 200 < remaining_units <= 300:
    slab_units = remaining_units - 200
    amount += slab_units * 8.0
    remaining_units -= slab_units

if 120 < remaining_units <= 200:
    slab_units = remaining_units - 120
    amount += slab_units * 5.0
    remaining_units -= slab_units

if 50 < remaining_units <= 120:
    slab_units = remaining_units - 50
    amount += slab_units * 2.5
    remaining_units -= slab_units

if 0 <= remaining_units <= 50:
    slab_units = 50  # minimum charge
    amount += slab_units * 1.5

print(f"""
            units consumed  : {units_consumed}
            Amount          : {amount}
        """)