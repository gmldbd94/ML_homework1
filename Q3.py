# Importing library
import pandas
from random import shuffle
import os

# 3-1번 문제
# Getting all the arff files from the current directory
files = [arff for arff in os.listdir('.') if arff.endswith(".arff")]

# Function for converting arff list to csv list
def toCsv(content):
    data = False
    header = ""
    newContent = []
    for line in content:
        if not data:
            if "@attribute" in line:
                attri = line.split()
                columnName = attri[attri.index("@attribute")+1]
                header = header + columnName + ","
            elif "@data" in line:
                data = True
                header = header[:-1]
                header += '\n'
                newContent.append(header)
        else:
            newContent.append(line)
    return newContent

# Main loop for reading and writing files
for file in files:
    with open(file , "r") as inFile:
        content = inFile.readlines()
        name,ext = os.path.splitext(inFile.name)
        new = toCsv(content)
        with open(name+".csv", "w") as outFile:
            outFile.writelines(new)

# read csv file
a_dataframe = pandas.read_csv('tic-tac-toe.csv', names=['top-left-square','top-middle-square','top-right-square',
                                          'middle-left-square','middle-middle-square','middle-right-square',
                                          'bottom-left-square','bottom-middle-square','bottom-right-square',
                                          'Class'])  #a_list is pandas.DataFrame

# 3-2번문제
# 추출한 데이터
# print("##### data #####")
# print(a_dataframe)

# 데이터를 리스트화
a_list = a_dataframe.values.tolist()

#첫번째는 속성값 부분은 제외시킨다.
attribute = a_list[0]
del a_list[0]
#데이터셋을 shuffle를 한다.
shuffle(a_list)

# 3-3번문제


# print(type(a_list))
print("#### shuffled a_list ####")
for num in range(10):
    print(a_list[num])

# 3-4번문제
print("#### a_list with attribute####")
print(attribute)
for num in range(10):
    print(a_list[num])
