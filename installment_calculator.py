unit_price = float(input("Enter unit price (EGP): "))
down_payment_pct = float(input("Enter down payment (%): ")) / 100
years = int(input("Enter installment years: "))

down_payment = unit_price * down_payment_pct
remaining = unit_price - down_payment
monthly_installment = remaining / (years * 12)

print(f"\nDown Payment: {down_payment:,.0f} EGP")
print(f"Monthly Installment: {monthly_installment:,.0f} EGP")

quarterly_installment = remaining / (years * 4)
print(f"Quarterly Installment: {quarterly_installment:,.0f} EGP")

if monthly_installment > 50_000:
    print("Alert: High monthly installment!")
else:
    print("Good: Installment is within budget.")