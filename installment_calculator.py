def calculate_installments(unit_price, down_payment_pct, years):
    down_payment = unit_price * down_payment_pct
    remaining = unit_price - down_payment
    monthly = remaining / (years * 12)
    quarterly = remaining / (years * 4)
    return down_payment, monthly, quarterly

price = float(input("Enter unit price (EGP): "))
dp_pct = float(input("Enter down payment (%): ")) / 100
yrs = int(input("Enter installment years: "))

dp, monthly_inst, quarterly_inst = calculate_installments(price, dp_pct, yrs)

print(f"\nDown Payment: {dp:,.0f} EGP")
print(f"Monthly Installment: {monthly_inst:,.0f} EGP")
print(f"Quarterly Installment: {quarterly_inst:,.0f} EGP")

if monthly_inst > 50_000:
    print("Alert: High monthly installment!")
else:
    print("Good: Installment is within budget.")