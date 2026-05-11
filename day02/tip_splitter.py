bill_amount = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip_amount = bill_amount * tip_percent / 100

total_bill = bill_amount + tip_amount

split_amount = total_bill / people

print("Tip Amount:", tip_amount)
print("Total Bill:", total_bill)
print("Each Person Pays:", split_amount)