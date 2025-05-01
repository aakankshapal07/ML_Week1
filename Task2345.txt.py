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


                            Task 3
marks = int(input("Enter your marks (0-100): "))

if 90 <= marks <= 100:
    grade = 'A'
elif 75 <= marks < 90:
    grade = 'B'
elif 60 <= marks < 75:
    grade = 'C'
elif 40 <= marks < 60:
    grade = 'D'
elif 0 <= marks < 40:
    grade = 'Fail'
else:
    grade = 'Invalid input'

print(f"Your grade is: {grade}")

                           Task 4 
temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

average = sum(temperatures) / len(temperatures)
print(f"\nAverage temperature over 5 days: {average:.2f}°C")

                            Task 5
import random

secret_number = random.randint(1, 20)
attempts = 5

print("Guess the number (between 1 and 20). You have 5 attempts!")

for i in range(attempts):
    guess = input(f"Attempt {i+1}: ")

    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)

    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry! The correct number was {secret_number}.")

