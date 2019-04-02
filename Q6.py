import random
# 6번문제
def min_max_avg(in_list):
    result = []
    minimun = min(in_list)
    maximum = max(in_list)
    average = sum(in_list)/len(in_list)
    result.append(minimun)
    result.append(maximum)
    result.append(average)
    print(result)

my_randoms = [random.randrange(1, 101, 1) for _ in range(20)]
print("#### my_rand_num ####")
print(my_randoms)

print("#### min_max_avg ####")
min_max_avg(my_randoms)

def equ_discretize(min_max, num):
    result = []
    min = min_max[0]
    max = min_max[1]
    interval = (max - min)/num
    tmp = min
    for i in range(num):
        result.append([int(tmp), int(tmp+interval)])
        tmp = tmp + interval
    print(result)

print("#### equ_discretize ####")
equ_discretize([-4, 8], 3)