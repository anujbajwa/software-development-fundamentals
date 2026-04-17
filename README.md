# software-development-fundamentals
Requisition System (Python)

This is a simple Python program that simulates a staff requisition system.
It allows users to:

Enter staff details
Add requisition items
Calculate total cost
Check approval status
Display final requisition summary
 Functions Overview
1. staff_info()

This function collects basic staff information.

What it does:
Takes input:
Date
Staff ID
Staff Name
Generates a Requisition ID
Prints staff details
Key Logic:
requisition_counter = requisition_counter + 1
requisition_id = 10000 + requisition_counter
Each requisition gets a unique ID starting from 10001
Returns:
(date, staff_id, staff_name, requisition_id)
2. requisitions_total()

This function handles item entry and calculates total cost.

What it does:
Calls staff_info() to get staff details
Allows user to enter multiple items
Stops when user types "done"
Adds item prices to calculate total
Loop Logic:
while True:
    item_name = input("Item name: ")
    if item_name.lower() == "done":
        break
Error Handling:
try:
    item_price = float(item_price)
except:
    print("Please enter a valid number")
Returns:
(date, staff_id, staff_name, requisition_id, total)
3. requisition_approval()

This function checks whether the requisition is approved.

Approval Rule:
if total < 500:
    status = "Approved"
else:
    status = "Pending"
Approval Reference Number:
approval_ref = staff_id + str(requisition_id)[-3:]
Combines:
Staff ID
Last 3 digits of requisition ID
Example:
Staff ID: A123
Requisition ID: 10045
Approval Ref: A123045
Returns:
(date, staff_id, staff_name, requisition_id, total, status, approval_ref)
4. display_requisitions()

This function displays the final output.

What it does:
Calls requisition_approval()
Prints:
Date
Staff details
Total cost
Status
Approval reference (if approved)
 Program Execution
display_requisitions()

This line starts the entire program.

Important Note (Bug)
Problem:
requisition_counter = 0
This resets the counter every time the function runs
Result: Requisition ID is always the same (10001)


Move it outside the function:

requisition_counter = 0

def staff_info():
    global requisition_counter
    requisition_counter += 1
 Summary

This program demonstrates:

User input handling
Loops (while)
Conditionals (if-else)
Error handling (try-except)
Function calls and returns
