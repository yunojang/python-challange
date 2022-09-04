print("welcome to hte tip calc.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, 15? ")) + 100
people_count = float(input("How many people to split the bill? "))

each_pay = "{:.2f}".format(
    float(total_bill) * (tip_percentage / 100) / people_count)

print(f"Each person should pay: ${each_pay}")
