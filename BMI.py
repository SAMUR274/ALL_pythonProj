# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
converter_height=float(height)
converter_weight=int(weight)
BMI=converter_weight/converter_height **2
converter_BMI=int(BMI)
print(converter_BMI)
