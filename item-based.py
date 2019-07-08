import csv
import numpy as np
import math
import random

matrix_str = []
matrix_str2 = []
averages = []
similarities = []

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

def computeAverage():
    for row in range(0, len(matrix_str)):
        rates = 0
        n = 0
        for col in range(0,len(matrix_str[0])):
            rates = rates + float(matrix_str[row][col])
            n = n+1
        averages.append(float(rates/n))

def itemSimilarity(u,v):
    top_part = 0
    bottom_part_a = 0
    bottom_part_b = 0
    for row in range(0,len(matrix_str)):
        top_part = top_part + ((float(matrix_str[row][u]) - averages[row]) * (float(matrix_str[row][v]) - averages[row]))
        bottom_part_a = bottom_part_a + ((float(matrix_str[row][u]) - averages[row]) * (float(matrix_str[row][u]) - averages[row]))
        bottom_part_b = bottom_part_b + ((float(matrix_str[row][v]) - averages[row]) * (float(matrix_str[row][v]) - averages[row]))
    bottom_part = math.sqrt(bottom_part_a) * math.sqrt(bottom_part_b)
    return float(top_part/(bottom_part + 1))

def prediction(row,col,topk):
    first = getFirst(topk,col)
    second = getSecond(topk,col,first[0][0])
    
    a = first[0][0] * float(matrix_str[row][first[0][1]])
    b = second[0][0] * float(matrix_str[row][second[0][1]])
    result = float(a + b) / (float(matrix_str[row][first[0][1]]) + float(matrix_str[row][second[0][1]]) +1 ) 

    if(result >= 0.5):
        return 1
    else:
        return 0           

def getFirst(arr,r):
    max = 0
    max_index = 0
    result = []
    for i in range(0,len(arr[0])):
        if(arr[r][i][0] > max and arr[r][i][0] < 0.999):
            max = arr[r][i][0]
            max_index = arr[r][i][1]
    result.append([max,max_index])
    return result

def getSecond(arr,r,first):
    max = 0
    max_index = 0
    result = []
    for i in range(0,len(arr[0])):
        if(arr[r][i][0] > max and arr[r][i][0] < 0.999 and arr[r][i][0] != first):
            max = arr[r][i][0]
            max_index = arr[r][i][1]
    result.append([max,max_index])
    return result

def getTopk():
    topk = []
    topk_id = []
    temp_topk = []
    for u in range(0, len(matrix_str[0])):
        for v in range(0, len(matrix_str[0])):
            temp_topk.append([itemSimilarity(u,v),v])
        topk.append(temp_topk)
        temp_topk = []
    return topk

def accuracy():
    print('Accuracy')
    y_true = []
    y_score = []
    topk = getTopk()

    for row in range(0, len(matrix_str)):
        for col in range(0,len(matrix_str[0])):
            y_true.append(int(matrix_str[row][col]))
            y_score.append(int(prediction(row,col,topk)))
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
computeAverage()
accuracy()

# Accuracy
# MAE: 0.500000
# MSE: 0.500000
# RMSE: 0.707107

# MAE: 0.061890
# MSE: 0.061890
# RMSE: 0.248776
