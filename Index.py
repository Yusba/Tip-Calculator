print("Welcome to the tip Calculator!")
bill = float(input("What was the total Bill : =N="))
tip = int(input("How much tips would you like to give ?  2,5,10,20,50 = "))
people = int(input("How many people would you like to split it with ? = "))
bills_with_tip = tip / 100 * bill + bill
print(f"Your split Tip is =N={bills_with_tip}")
