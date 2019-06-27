import csv
import numpy as np
import math
import random

matrix_str = []
matrix_str2 = []

def readCSV():
    with open('dataset.csv') as csv_file:
        print('Reading dataset')
        csv_reader = csv.reader(csv_file)
        row_counter = 0
        for row in csv_reader:
            row_counter += 1
            if(row_counter > 1): #skip the ID row
                row.pop(0)
                matrix_str.append(row)

def firstProb(user_index,item_index,value):
    p1 = 0
    total_rates = 0
    frequency = 0
    for row in range(0, len(matrix_str)):
        if(matrix_str[row][item_index] != '?'): #if there is any rate, count it
            total_rates += 1
            
        if(matrix_str[row][item_index] == value): #count the number of 1
            p1 += 1
    return float(p1)/float(total_rates)                 

def pGiven1(user_index,item_index):
    indexes1 = []
    prob = firstProb(user_index,item_index, '1')
    one_frequency = 0
    total_rates = 0

    for row in range (0, len(matrix_str)): #get all the positions with value 1 for a given item
        if(matrix_str[row][item_index] == '1'):
            indexes1.append(row)
    
    for col in range(0, len(matrix_str[0])):
        if(col != item_index and matrix_str[user_index][col] != '?'):
            for row in indexes1:
                if(matrix_str[row][col] == '?'):
                    one_frequency += 1
                if(matrix_str[row][col] == matrix_str[user_index][col]):
                    one_frequency += 1
            prob = prob * float((float(one_frequency) / float(len(indexes1))))
            one_frequency = 0
    return  prob

def pGiven0(user_index,item_index):
    indexes0 = []
    prob = firstProb(user_index,item_index, '0')
    zero_frequency = 0
    total_rates = 0

    for row in range (0, len(matrix_str)): # get all the positions with value 0 for a given item
        if(matrix_str[row][item_index] == '0'):
            indexes0.append(row)
    
    for col in range(0, len(matrix_str[0])):
        if(col != item_index):
            for row in indexes0:
                total_rates += 1
                if(matrix_str[row][col] == '0'):
                    zero_frequency += 1
            prob = prob * (float(zero_frequency) / float(total_rates))
    return  prob

def recommend(user_index,item_index):
    if(pGiven1(user_index, item_index) > pGiven0(user_index,item_index)):
        return 1
    else:
        return 0

def accuracy():
    print('Accuracy')
    y_true = []
    y_score = []

    for row in range(0, len(matrix_str)):
        for col in range(0,len(matrix_str[0])):
            y_true.append(int(matrix_str[row][col]))
            y_score.append(int(recommend(row,col)))
    print("MAE: %f" % MAE(y_true,y_score))
    print("MSE: %f" % MSE(y_true,y_score))
    print("RMSE: %f" % RMSE(y_true,y_score))
    return

def MAE(y_true, y_score):
    sum = 0
    for i in range(0, len(y_true)):
        sum += abs((y_true[i] - y_score[i]))
    return float(sum) / len(y_true)

def MSE(y_true, y_score):
    sum = 0
    for i in range(0, len(y_true)):
        sum += np.power((y_true[i] - y_score[i]),2)
    return  float(sum) / len(y_true)

def RMSE(y_true, y_score):
    sum = 0
    for i in range(0, len(y_true)):
        sum += np.power((y_true[i] - y_score[i]),2)
    return math.sqrt(float(sum) / len(y_true))

readCSV()
# for row in range(0,len(matrix_str)):
#     for col in range(0,len(matrix_str[0])):
#         if(matrix_str[row][col] == '?'):
#             print(row,col,recommend(row,col))
accuracy()

# MAE: 0.060075
# MSE: 0.060075
# RMSE: 0.245102
