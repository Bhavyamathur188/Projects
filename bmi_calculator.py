def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


print("=" * 40)
print("        BMI CALCULATOR")
print("=" * 40)

while True:
    try:
        weight = float(input("\nEnter your weight (kg): "))
        height = float(input("Enter your height (meters): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            continue

        bmi = calculate_bmi(weight, height)

        print("\n===== RESULT =====")
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {bmi_category(bmi)}")

        choice = input("\nCalculate again? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using the BMI Calculator!")
            break

    except ValueError:
        print("Please enter valid numeric values.")