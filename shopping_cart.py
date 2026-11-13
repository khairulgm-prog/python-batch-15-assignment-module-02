
#PythonBatch14Module02Assignment submitted by Md Khairul Alam Prodhan

#Shopping Cart

# 1. Take the customer's name as input

customer_name = input("Enter customer's name: ")

# 2. Take the names and prices of 3 products as input

product1_name = input("\nEnter name of product 1: ")
product1_price = float(input(f"Enter price of {product1_name}: "))

product2_name = input("\nEnter name of product 2: ")
product2_price = float(input(f"Enter price of {product2_name}: "))

product3_name = input("\nEnter name of product 3: ")
product3_price = float(input(f"Enter price of {product3_name}: "))

# 3. Calculate the subtotal

subtotal = product1_price + product2_price + product3_price

# 4. Determine the discount percentage based on the subtotal
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

# Calculate the discount amount and final total

discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount

# 5. Display the shopping summary using f-strings
print("\n" + "=" * 35)
print(f"Shopping Summary for {customer_name}")
print("=" * 35)
print(f"1. {product1_name:<20} {product1_price:>10.2f}")
print(f"2. {product2_name:<20} {product2_price:>10.2f}")
print(f"3. {product3_name:<20} {product3_price:>10.2f}")
print("-" * 35)
print(f"Subtotal:               {subtotal:>10.2f}")
print(f"Discount ({int(discount_rate * 100)}%):         -{discount_amount:>9.2f}")
print("=" * 35)
print(f"Final Total:            {final_total:>10.2f}")
print("=" * 35)
