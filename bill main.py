print("welcome to calcu")
bill=float(input("enter the total bill::\n"))
tip=float(input("enter the tips::\n"))
split=float(input("enter the number of people::\n"))
real_tip=float(round(tip/100,2))
total_bill=(bill/split+real_tip)
print(f"each people should pay:{total_bill}")
