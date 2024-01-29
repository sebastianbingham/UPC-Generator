import csv
from datetime import datetime


# Function to calculate the check digit of a UPC
def calculate_check_digit(upc_digits):
    weighted_digits = [int(digit) * (3 if i % 2 == 0 else 1) for i, digit in enumerate(upc_digits)]
    total = sum(weighted_digits)
    remainder = total % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder


# Function to generate UPC codes, prompt for input, and export to CSV
def generate_upc_codes():
    # Prompt for the Number System Character (single digit)
    num_system_char = input("Enter Number System Character (single digit): ")
    while not num_system_char.isdigit() or len(num_system_char) != 1:
        print("Invalid input. Please enter a single digit for Number System Character.")
        num_system_char = input("Enter Number System Character (single digit): ")

    # Prompt for the Company Prefix (exactly 5 digits)
    company_prefix = input("Enter Company Prefix (exactly 5 digits): ")
    while not company_prefix.isdigit() or len(company_prefix) != 5:
        print("Invalid input. Please enter exactly 5 digits for Company Prefix.")
        company_prefix = input("Enter Company Prefix (exactly 5 digits): ")

    # Prompt for the Starting Product Number (exactly 5 digits)
    start_product_number = input("Enter Starting Product Number (exactly 5 digits): ")
    while not start_product_number.isdigit() or len(start_product_number) != 5:
        print("Invalid input. Please enter exactly 5 digits for Starting Product Number.")
        start_product_number = input("Enter Starting Product Number (exactly 5 digits): ")

    # Prompt for the number of codes to generate
    num_to_generate = int(input("Enter the number of codes to generate: "))

    # Generate a timestamp for the output filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"barcodes_output_{timestamp}.csv"

    # Create and open a CSV file for writing
    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['UPC']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Generate and write the UPC codes to the CSV file
        for i in range(num_to_generate):
            product_number = str(int(start_product_number) + i)
            upc_digits = num_system_char + company_prefix + product_number
            check_digit = calculate_check_digit(upc_digits)
            upc_code = upc_digits + str(check_digit)
            writer.writerow({'UPC': upc_code})

    # Print a confirmation message
    print(f"{num_to_generate} UPC codes generated and saved to {filename}.")


# Main program
if __name__ == "__main__":
    generate_upc_codes()
