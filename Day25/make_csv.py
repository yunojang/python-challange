import pandas

attendance = {
    "student": ["Jimi", "Angela", "Yuno"],
    "age": [28, 31, 25],
    "score": [7, 8, 9],
}

data = pandas.DataFrame(attendance)
data.to_csv("new_csv_attendance.csv")
