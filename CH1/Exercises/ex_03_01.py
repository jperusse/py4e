hours = float(input("Enter hours: "))
rate = float(input("Enter Rate: "))

# Calculate pay, np overtime
if hours <= 40:
    pay = hours * rate

# Calculate total pay including overtime
else:
    ot_hours = hours - 40
    ot_rate = rate * 1.5
    pay = (40 * rate) + (ot_hours * ot_rate)

print("Pay:", pay)