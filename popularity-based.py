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

def getFrequency():
    max = 0
    frequencies = []
    for col in range(0,len(matrix_str[0])):
        frequency = 0
        for row in range(0,len(matrix_str)):
            if(matrix_str[row][col] == '1'):
                frequency = frequency + 1
        frequencies.append(frequency)      
        frequency = 0
    arr = np.array(frequencies)
    return np.argpartition(arr, -30)[-30:]

def recommend(row,col,top):
    for i in range(0,len(top)):
        if(col == top[i]):
            return 1
        else:
            return 0

def accuracy():
    print('Accuracy')
    y_true = []
    y_score = []
    top = getFrequency()

    for row in range(0, len(matrix_str)):
        for col in range(0,len(matrix_str[0])):
            y_true.append(int(matrix_str[row][col]))
            y_score.append(recommend(row,col,top))
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
getFrequency()
accuracy()

# MAE: 0.094004
# MSE: 0.094004
# RMSE: 0.306601


