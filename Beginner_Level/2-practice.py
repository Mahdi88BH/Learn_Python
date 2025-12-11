total_bills = float(input("Enter total bills amount: "))
tips = int(input("Enter tip Would you like to give (e.g., 10, 12, or 15): "))
nb_people = int(input("Enter number of people to split the bill: "))

total_bills += tips
total_biils_of_each_idivedue = total_bills / nb_people
print("Each person should pay: " + str(total_biils_of_each_idivedue))

# print(66.5 * 4 == (253 + 13))