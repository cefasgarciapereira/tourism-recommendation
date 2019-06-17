import csv

matrix_str = []

def readCSV():
    with open('dataset-backup.csv') as csv_file:
        print('Reading dataset')
        csv_reader = csv.reader(csv_file)
        row_counter = 0
        for row in csv_reader:
            row_counter += 1
            if(row_counter > 1): #skip the ID row
                row.pop(0)
                matrix_str.append(row)

def prob1(user_index,item_index):
    p1 = 0
    total_rates = 0
    frequency = 0
    for row in range(0, len(matrix_str)):
        if(matrix_str[row][item_index] != '?'): #if there is any rate, count it
            total_rates += 1
            
        if(matrix_str[row][item_index] == '1'): #count the number of 1
            p1 += 1
    return float(p1)/float(total_rates)

def prob0(user_index,item_index):
    p0 = 0
    total_rates = 0
    frequency = 0
    for row in range(0, len(matrix_str)):
        if(matrix_str[row][item_index] != '?'): #if there is any rate, count it
            total_rates += 1
            
        if(matrix_str[row][item_index] == '0'): #count the number of 1
            p0 += 1
    return float(p0)/float(total_rates)    

def pGiven1(user_index,item_index):
    indexes1 = []
    prob = prob1(user_index,item_index)
    one_frequency = 0
    total_rates = 0

    for row in range (0, len(matrix_str)): #get all the positions with value 1 for a given item
        if(matrix_str[row][item_index] == '1'):
            indexes1.append(row)
    
    for col in range(0, len(matrix_str[0])):
        if(col != item_index):
            for row in indexes1:
                total_rates += 1
                if(matrix_str[row][col] == '1'):
                    one_frequency += 1
            prob = prob * float((float(one_frequency) / float(total_rates)))
    return  prob

def pGiven0(user_index,item_index):
    indexes0 = []
    prob = prob0(user_index,item_index)
    zero_frequency = 0
    total_rates = 0

    for row in range (0, len(matrix_str)): #get all the positions with value 1 for a given item
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
    print('Recommending...')
    if(pGiven1(user_index, item_index) > pGiven0(user_index,item_index)):
        return 1
    else:
        return 0

readCSV()

for row in range(0,len(matrix_str)):
    for col in range(0,len(matrix_str[0])):
        if(matrix_str[row][col] == '?'):
            print(pGiven1(row,col))