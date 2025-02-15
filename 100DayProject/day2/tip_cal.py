print(" Welcome to the tip calculator!")
bill= float(input("What was the total bill?\nRupee:"))
tip = float(input("How much tip would you like to give? 10 , 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Your total bill in Rupee:{total_bill}\nEach person should pay in Rupee: {final_amount}")