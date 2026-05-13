# Calculating fianl bill with tax and discount 
item_price = float(input("Enter price of item : "))
Discount_pct = float(input("Enter discount price : "))
discount_amount = (item_price * Discount_pct)/100 
tax_rate = 0.18       # 18 % GST 
tax_amount = item_price * tax_rate
final_price = item_price - discount_amount + tax_amount
print(f'Original price : {item_price:.3f}')
print(f'Discount offer : {discount_amount:.3f}')
print(f'Tax : {tax_amount:.3f}')
print(f'Final :  {final_price:.3f}')




