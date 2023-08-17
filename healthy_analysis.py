import pandas as pd
import numpy as np

number_var = 42

string_var = "Hello, Health Analysis"

list_var = [1,2,3,4,5]

nested_dict = {
    'name' : "John",
    'age' : 30,
    'measurement': [175,70],
    'details': {
        'blood type' : "A+",
        'Condition' : 'Healthy'
        }
    }
print(string_var)
print('Number Variable:', number_var)
print("List:", list_var)
print("Info:\n" , nested_dict)


def health_index(weight_kg,height_cm):
    height_m = height_cm/100

    bmi = weight_kg/(height_m **2)

    if bmi < 18.5:
        status = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        status = 'Normal Weight'
    elif 25 <= bmi <29.9:
        status = 'Overweight'
    else:
        status = 'Obese'

    return bmi, status

weight = 70
height = 175

bmi_result, health_status = health_index(weight, height)

print("\nHealth Index Calculation:")
print("BMI:", bmi_result)
print("Health Status:", health_status)
git clone https://github.com/jjomathew98/health-analytics.git
