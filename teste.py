import numpy as np
import scipy
import pandas as pd
import math
import random
import sklearn
import nltk

ratingsDF = pd.read_csv("dataset2.csv",usecols=['userid', 'poi', 'like'])
ratingsDF.columns = ['userid', 'poi', 'like']
print('# ratings: %d' % len(ratingsDF))
print ('# itens: %d' % itemsDF.itemId.shape[0])
print ('# itens unicos: %d' % itemsDF.itemId.unique().shape[0])