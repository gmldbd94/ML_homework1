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

# 5번문제
def divide_train_test(in_list, prop):
    train_list = []
    test_list = []
    result = []
    divide_num = int(len(in_list)*prop)
    for num in range(divide_num):
        train_list.append(in_list[num])
    for num in range(divide_num, len(in_list)):
        test_list.append(in_list[num])

    result.append(train_list)
    result.append(test_list)
    return result

#prop 0.9로 할때
test = divide_train_test(a_list, 0.9)
print("#### train_test_dataset ####")
print(test)