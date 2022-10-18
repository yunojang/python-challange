# raise TimeoutError("hurry")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3.0:
  raise ValueError("too long height")

bmi = weight / height**2
print(bmi)