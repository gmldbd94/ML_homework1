import numpy as np
import matplotlib.pyplot as plt

#7-1번 문제
def no_of_values(in_list):
    result = len(in_list)
    print("#### no_of_values ####")
    print(result)
    return result

#7-2 과 7-3번 문제
def no_of_dis_val(in_list):
    value_list = {}

    for list in in_list:
        if list in value_list:
            value_list[list] +=1
            continue
        else:
            value_list[list] = 1
    result = len(value_list)
    print("#### no_of_dis_val ####")
    print(result)
    print("#### dictionary value ####")
    print(value_list)
    return result

# 7-4번 문제
def plot_bar(in_list):
    value_list = {}
    x_list = []
    y_list = []
    for list in in_list:
        if list in value_list:
            value_list[list] +=1
            continue
        else:
            value_list[list] = 1

    for x_key in value_list.keys():
        x_list.append(x_key)

    for y_value in value_list.values():
        y_list.append(y_value)

    n_groups = len(x_list)
    index = np.arange(n_groups)
    plt.bar(index, y_list, tick_label=x_list, align='center', color = "red")
    plt.xlabel('distinct value')
    plt.ylabel('count')
    plt.title('distinct value counter graph')
    plt.xlim(-1, n_groups)
    plt.ylim(0, 10)
    plt.show()

no_of_values([0,1,1,2,0])

no_of_dis_val([0,1,1,2,0])

plot_bar([0,1,1,2,0])
