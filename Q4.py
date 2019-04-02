import pandas

# read csv file
a_dataframe = pandas.read_csv('tic-tac-toe.csv', names=['top-left-square','top-middle-square','top-right-square',
                                          'middle-left-square','middle-middle-square','middle-right-square',
                                          'bottom-left-square','bottom-middle-square','bottom-right-square',
                                          'Class'])  #a_list is pandas.DataFrame
# 데이터를 리스트화
a_list = a_dataframe.values.tolist()

#첫번째는 속성값 부분은 제외시킨다.
attribute = a_list[0]
del a_list[0]

# 4번문제
print("### a_list ####")
# 만약 속성값을 넣어주고 싶으면 아래 코드의 주석을 풀어준다.
# a_list.Insert(0, attribute)
print(attribute)
print(a_list)


# a_list 역순을 으로 바꿔준다.
a_list.reverse()
c_list = a_list

# a_list 를 원상복구 시킨다.
a_list.reverse()

# 만약 속성값을 넣어주고 싶으면 아래 코드의 주석을 풀어준다.
# c_list.Insert(0, attribute)
print("#### c_list #####")
print(attribute)
print(c_list)