principle = 0
rate = 0
time = 0
# Here we are calcluating CI in Years....

while principle <= 0:
    principle = float(input("Enter the principle amount :  "))
    if principle <= 0:
        print("The principle can't be less than or equals to zero")

while rate <= 0:
    rate = float(input("Enter the rate amount :  "))
    if rate <= 0:
        print("The rate can't be less than or equals to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("The time can't be less than or equal to zero")
  
compound_interest = principle * pow((1 + rate/100), time)

print(f"Your Compound Interest of {time} year /s is: {compound_interest}")
