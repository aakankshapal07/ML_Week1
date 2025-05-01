Task 2 
total = 0
n = int(input("Enter the number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    quantity = int(input(f"Enter quantity of item {i+1}: "))
    total += price * quantity

gst = total * 0.18
grand_total = total + gst

print(f"\nSubtotal: ₹{total:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total Bill: ₹{grand_total:.2f}")
