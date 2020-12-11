
try:
    hours = float(input("Enter hours: "))
except:
    print("Error, please enter numberic input")
    quit()    

try:
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numberic input")
    quit()  

maxhours = 40
# Calculate pay, no overtime
if hours <= maxhours:
    pay = hours * rate

# Calculate total pay including overtime
else:
    ot_hours = hours - maxhours
    ot_rate = rate * 1.5
    pay = (maxhours * rate) + (ot_hours * ot_rate)

print("Pay:", pay)