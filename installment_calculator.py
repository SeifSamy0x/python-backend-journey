unit_price = 4_000_000
down_payment_pct = 0.10
years = 8

down_payment = unit_price * down_payment_pct
remaining = unit_price - down_payment
monthly_installment = remaining / (years * 12)

print(f"Down Payment: {down_payment:,.0f} EGP")
print(f"Monthly Installment: {monthly_installment:,.0f} EGP")