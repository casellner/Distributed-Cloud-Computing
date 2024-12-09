import decimal
import time

def compute_pi(digits):
    # Set the precision
    decimal.getcontext().prec = digits + 2
    pi = decimal.Decimal(0)

    # BBP formula
    for k in range(digits):
        pi += (decimal.Decimal(1) / (16 ** k)) * (
            decimal.Decimal(4) / (8 * k + 1) -
            decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) -
            decimal.Decimal(1) / (8 * k + 6)
        )

    return str(pi)[:digits + 2]

# Get user input for number of digits
while True:
    try:
        num_digits = int(input("Enter the number of digits to calculate PI to: "))
        if num_digits > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid integer.")

start_time = time.time()
pi_value = compute_pi(num_digits)
end_time = time.time()
execution_time = end_time - start_time

print(f"Value of π to {num_digits} digits: {pi_value}")
print(f"Calculation took {execution_time:.2f} seconds")
