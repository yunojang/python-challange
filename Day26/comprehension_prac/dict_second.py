weather_c = {
  "monday": 12,
  "tuesday": 14,
  "wednesday": 15,
  "thursday": 14,
  "friday": 21,
  "saturday": 22,
  "sunday": 24,
}
def convert_f(temp_c):
    return (temp_c * 9 / 5) + 32 

result = {day: convert_f(temp_c) for (day, temp_c) in weather_c.items()}
print(result)