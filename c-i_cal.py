principle = 0
rate = 0
time = 0
# Here we are calculating CI in Years....

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("The principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("The rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("The time can't be less than zero")
    else:
        break

compound_interest = principle * pow((1 + rate/100), time)

print(f"Your Compound Interest of {time} year/s is: {compound_interest:.2f}")