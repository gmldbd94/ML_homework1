## 머신러닝 과제
~~~
Machine Learning Homework 1 (Python Exercise)

Mar. 20, 2019

    Please note that all homework should be your own work. You should also not copy answers from other person’s, books or internet resources. 
    I didn’t proofread the questions. If you find any typos/errors, let me know.

1. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
 Input List : ['cbc', 'xyz', 'abb', '1221']
 Output : 2

2. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a list.
 Input List : [[2, 6], [1, 2], [3, 4], [2, 3], [2, 1]]
 Output : [[2, 1], [1, 2], [2, 3], [3, 4], [2, 6]]

    Select ONE arff file from e-class. Change it to csv file. The csv file must contain numbers and/or strings only, each of which is separated by commas. In dong so, you have to modify arff file by removing header part (% and @ part) of the data.

3. Write Python code for the following tasks
    1) read csvfile into a two dimension list (called “a_list”) 
    e.g.: csvfile=   a_list=[[1,0,2,3,1], [0,1,1,2,0], [0,1,0,1,1], [0,0,2,3,1]]
    2) write a Python program which randomly shuffles ‘a_list’ data
    3) write a Python program that shows the first 10 rows from the “a_list”.
    4) show the number of column(attribute) and number of rows(record), respectively. 

4. Using the “a_list” in question 2. write Python code for the following tasks
    1) given a column(attribute) number, write a program that shows the values of the column.
    2) reverse the elements of q. 1)
    3) copy the result of q. 2) into c_list.

5. Using the “a_list”, write Python code for the following tasks
    1) define a function “divide_train_test(in_list, prop)” function where
       input: 1) in_list: a 2D list, 2) prop: proportion of training data
       output: train_data (first “prop” percent of in_list), test_data (the rest of in_list)
    2) run divide_train_test(b_list, prop) TWO times using prop=0.6, 0.8, respectively, and show the result.
       e.g.: divide_train_test([[1,2,3], [5,1,8], [8,5,2], [0,3,6], [1,7,3]], 0.6) returns
       [ [ [1,2,3], [5,1,8], [8,5,2] ], [ [0,3,6], [1,7,3] ] ]
       \# train_data                \test_data

6. Write Python code for the tasks.
    1) define a function “min_max_avg” which takes a list of numbers and returns [minimum, maximum, average] of the list
      e.g.: def min_max_avg(in_list):
    2) randomly generate 20 numbers and, calculate the average, minimum, and maximum values using above “min_max_avg” function
      e.g.: mean_min_max([1,6,2,8,3,5,-4,2]) returns [-4, 8, 2.875]
      
3) define a function “equ_discretize” which divides a value range into n equal intervals. 
    input: 1) list [min, max] of range, 2) number of intervals
    output: list of (equal distance) intervals
4) run equ_discretize 3 times by using different values of list and number of intervals.
  e.g.: equ_discretize([-4, 8], 3) returns [[-4,0], [0,4], [4,8]]

7. Write Python code for the following tasks.
1) define a function “no_of_values” which takes a list and returns the number of values in the list.
2) define a function “no_of_dis_val” which takes a list and returns the number of “distinct” values in the list.
e.g.: a_list=[0,1,1,2,0]
     no_of_dis_val(a_list) returns 3 ==> 3 unique values
     This means a_list contains 3 distinct values
3) for every attribute in “a_list”, calculate the number of values and distinct values, respectively, using q 1) and q 2).
4) plot a graphic table(e.g.: bar graph) by your favorite color using matplotlib as follows: X axis: index of attribute, Y axix: number of distinct values.


Hand In
1) submit a hardcopy report which includes questions & program code & results. Refer to the following example.

e.g.: In your report
...
6. .Write Python code for the tasks...
1) define a function “min_max” ...
<PROGRAM CODE> <== This is title
put your program code segment for Q 6 1) here
<RESULT> <== This is title
put the screen dump of your program run for Q 6 1) here

2) randomly generate ...
<PROGRAM CODE> <== This is title
put your program code segment for Q 6 2) here
<RESULT> <== This is title
put the screen dump of your program run here
...

2) Submit hardcopy report in class, and upload the following files at e-class.
   i) report file, ii) program source file, iii) datafile file

Due: 4/3(Wed)
~~~
