prices = [10, 5, 20]     
quantities = [3, 2, 4]    

total_bill = 0


for i in range(3):
    total_bill = total_bill + (prices[i] * quantities[i])

print(f"Total Bills is {total_bill}")