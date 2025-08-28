def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return f"{category} (BMI = {bmi})"

if __name__ == "__main__":
    print(bmi_calculator(60, 1.92))
