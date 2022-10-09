from random import randint


names = ['yuno', 'angella', 'sooki']
students = {name: randint(0,100) for name in names}

passed_students = {k: v for (k, v) in students.items() if v >= 70}
print(passed_students)


# deep copy practice
user = {
  "name": 'yuno',
  "age": 24,
  "grade": "junior"
}

new_user = {key: value for (key, value) in user.items()}
# print(new_user)
new_user["grade"] = "middle"

print(new_user)
print(user)