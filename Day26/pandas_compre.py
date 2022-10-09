import pandas

studunt_dict = {"student": ["Angela", "Yuno", "Tom"], "score": [88, 90, 72]}

student_data_frame = pandas.DataFrame(studunt_dict)
# print(student_data_frame.score[0])

# pandas dataframe도 dict처럼 items로 이터레이션을 돌릴 수 있다.
# column이 key로, 각 열이(pandas.Series)가 value로 나온다.
# pandas.Series는 to_list()활용 list로 쉽게 정리할 수 있다.
# for k, v in student_data_frame.items():
#     print(k)
#     print(v.to_list())

# for idx, row in student_data_frame.iterrows():
#     # print(idx)
#     print(row.student)


# student_dict = {k: v.to_list() for k, v in student_data_frame.items()}
