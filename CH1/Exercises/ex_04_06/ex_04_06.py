
def computepay(hours, rate):
     return hours * rate

inperr = "Error, please enter numberic input"

try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter Rate: "))
except:
    print(inperr)
    quit()

maxhours = 40
# Calculate pay, no overtime
if hours <= maxhours:
    pay = computepay(hours, rate)

# Calculate total pay including overtime
else:
    ot_hours = hours - maxhours
    ot_rate = rate * 1.5
    pay = computepay(maxhours, rate) + computepay(ot_hours, ot_rate)

print("Pay:", pay)
