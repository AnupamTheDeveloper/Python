#shop will give discount of 10% if the cost of purchase quantity is more than 1000
purchase_unit=int(input("Enter the number of purchase unit:"))
cost=int(purchase_unit*100)
discount=int(cost*0.1)
if(cost>1000):
    final_cost=int(cost-discount)
    print(f"Total Cost is {final_cost}")
else:
    final_cost=cost
    print(f"Total Cost{final_cost}")