import openpyxl
import re

def validate_roll_number(roll_number):
    return bool(re.match(r'^[A-Za-z0-9]+$', roll_number))

def validate_name(name):
    return bool(re.match(r'^[A-Za-z]+$', name))

def add_data_to_excel(roll_number, name):
    # Load existing workbook or create a new one if it doesn't exist
    try:
        workbook = openpyxl.load_workbook('data.xlsx')
    except FileNotFoundError:
        workbook = openpyxl.Workbook()

    # Select the active sheet (first sheet by default)
    sheet = workbook.active

    # Append the data to the sheet if valid
    if validate_roll_number(roll_number) and validate_name(name):
        sheet.append([roll_number, name])
        # Save the workbook
        workbook.save('data.xlsx')
        print("Data saved successfully!")
    else:
        print("Invalid input. Roll number should contain only alphabets and numerics, and name should contain only alphabets.")

def main():
    # Input roll number and name
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    # Display successful message
    print("Successfully!")

    # Add data to Excel file if valid
    add_data_to_excel(roll_number, name)

if __name__ == "__main__":
    main()