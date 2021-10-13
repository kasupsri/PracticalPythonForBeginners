#expenses = [10.50,8,5,15,20,5,3]
#sum = 0
#for x in expenses:
#    sum = sum + x

no_of_expenses = int(input("Enter No of expenses you have to enter:"))

expenses=[]
for n in range(no_of_expenses):
    expenses.append(float(input("Enter an expenses:")))

total = sum(expenses)

print("You spent $",total, sep='')