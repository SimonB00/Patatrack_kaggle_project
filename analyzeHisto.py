from urllib.request import parse_http_list
from matplotlib.backend_bases import FigureManagerBase
from matplotlib.pyplot import eventplot
from more_itertools import first
from numpy import sort, triu_indices
from operator import index, truth
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl
from matplotlib.ticker import PercentFormatter
from mpl_toolkits.mplot3d import Axes3D
import mplhep as hep 
import glob

path = '/home/simone/Documents/thesis/not_sorted/'

pairs_files = glob.glob(path + 'hist_ns*.csv')
print(len(pairs_files))     # why only 1320?
pairs_files.sort()

# let's start with the first file 
first_pairs_df = pd.read_csv(pairs_files[0])
print(first_pairs_df)
col = pd.DataFrame(first_pairs_df['pairIndex'])
print(type(first_pairs_df['volume1'][0]))

# create a column with the volume pairs
vol_pair_column = []
for i in range(len(col)):
    set_ = {first_pairs_df['volume1'][i],first_pairs_df['volume2'][i]}
    vol_pair_column.append(set_)

vol_pair_column = pd.Series(vol_pair_column)
first_pairs_df = pd.concat([first_pairs_df,vol_pair_column],axis=1)
first_pairs_df = first_pairs_df.rename(columns={0:'volPairs'})
print(first_pairs_df)

# Count the pairs for vol combination (credit to Angie)
countValues = first_pairs_df['pair'].value_counts()
print(countValues)

# only hits in blue volumes
pairs_bl = {}
count_bl = 0
for i in range(col.size):
    if (first_pairs_df['volume1'][i] == 8 and first_pairs_df['volume2'][i] == 8) or (first_pairs_df['volume1'][i] == 7 and first_pairs_df['volume2'][i] == 8) or (first_pairs_df['volume1'][i] == 8 and first_pairs_df['volume2'][i] == 9):
        count_bl += 1
        if str(first_pairs_df['pair'][i]) in pairs_bl.keys():
            pairs_bl[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs_bl[str(first_pairs_df['pair'][i])] = 1
print('hits blue = ' + str(count_bl)) # 7459
plt.style.use(hep.style.CMS)
plt.bar(pairs_bl.keys(), pairs_bl.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# now we sort all the hist corresponding to volume 7
pairs_ = {}
count7 = 0
for i in range(col.size):
    if (7 in first_pairs_df['volPairs'][i]):
        count7 += 1
        if str(first_pairs_df['pair'][i]) in pairs_.keys():
            pairs_[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs_[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 7 = ' + str(count7)) # 7459
plt.style.use(hep.style.CMS)
plt.bar(pairs_.keys(), pairs_.values())
plt.xticks(rotation = 45) 
plt.xlabel('Coppie di Layers')
plt.ylabel('Occorrenze')
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 8
pairs__ = {}
count8 = 0
for i in range(col.size):
    if (8 in first_pairs_df['volPairs'][i]):
        count8 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 8 = ' + str(count8))
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 9
pairs__ = {}
count9 = 0
for i in range(col.size):
    if (9 in first_pairs_df['volPairs'][i]):
        count9 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 9 = ' + str(count9)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 12
pairs__ = {}
count12 = 0
for i in range(col.size):
    if (12 in first_pairs_df['volPairs'][i]):
        count12 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 12 = ' + str(count12)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 13
pairs__ = {}
count13 = 0
for i in range(col.size):
    if (13 in first_pairs_df['volPairs'][i]):
        count13 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 13 = ' + str(count13)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 14
pairs__ = {}
count14 = 0
for i in range(col.size):
    if (14 in first_pairs_df['volPairs'][i]):
        count14 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 14 = ' + str(count14)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 16
pairs__ = {}
count16 = 0
for i in range(col.size):
    if (16 in first_pairs_df['volPairs'][i]):
        count16 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 16 = ' + str(count16)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 17
pairs__ = {}
count17 = 0
for i in range(col.size):
    if (17 in first_pairs_df['volPairs'][i]):
        count17 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 17 = ' + str(count17)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# same thing for volume 18
pairs__ = {}
count18 = 0
for i in range(col.size):
    if (18 in first_pairs_df['volPairs'][i]):
        count18 += 1
        if str(first_pairs_df['pair'][i]) in pairs__.keys():
            pairs__[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs__[str(first_pairs_df['pair'][i])] = 1
print('hits from a volume to volume 18 = ' + str(count18)) # 8618
plt.bar(pairs__.keys(), pairs__.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# let's try to make an histogram with all the pairs except the ones with 0 occurences
all_pairs_ = {}
for i in range(col.size):
    if str(first_pairs_df['pair'][i]) in all_pairs_.keys():
        all_pairs_[str(first_pairs_df['pair'][i])] += 1
    else: 
        all_pairs_[str(first_pairs_df['pair'][i])] = 1

sorted_dict = {}
sorted_keys = sorted(all_pairs_, key=all_pairs_.get)
for w in sorted_keys:
    sorted_dict[w] = all_pairs_[w]
all_pairs_ = sorted_dict

plt.bar(all_pairs_.keys(), all_pairs_.values())
plt.xticks(rotation = 45) 
figsize = (30, 20)
#plt.yscale("log")
plt.show()

# now I'll eliminate the pairs with 20 occurrences
new_dict = {}
for key in all_pairs_.keys():
    if (all_pairs_[key] > 20):
        new_dict[key] = all_pairs_[key]

all_pairs_ = new_dict
plt.bar(all_pairs_.keys(), all_pairs_.values())
plt.xticks(rotation = 45) 
figsize = (30, 20)
plt.yscale("log")
plt.show()

# same plot but sorting by volume
volumes = [7,8,9,12,13,14,16,17,18]

vol_sort_pairs = {}
for vol in volumes:
    for i in range(col.size):
        if (vol in first_pairs_df['volPairs'][i]):
            if str(first_pairs_df['pair'][i]) in vol_sort_pairs.keys():
                vol_sort_pairs[str(first_pairs_df['pair'][i])] += 1
            else: 
                vol_sort_pairs[str(first_pairs_df['pair'][i])] = 1

new_dict_2 = {}
for key in vol_sort_pairs.keys():
    if (vol_sort_pairs[key] > 20):
        new_dict_2[key] = vol_sort_pairs[key]
vol_sort_pairs = new_dict_2

plt.bar(vol_sort_pairs.keys(), vol_sort_pairs.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# plot the count of volume pairs
mycounts = []

for i in range(19):
    for j in range(19):
        x = sum((first_pairs_df.volume1 == i) & (first_pairs_df.volume2 == j))
        ttuple=(i,j,x)
        if x!=0: 
            mycounts.append(ttuple)         
#print(mycounts)

df1 = pd.DataFrame(mycounts, columns=['volume1', 'volume2', 'counts'])
volume1 = 'volume1'
volume2 = 'volume2'
df1['Volumes'] = df1['volume1'].map(str) + '-' + df1['volume2'].map(str)
df1

ax1 = df1.plot.bar(x='Volumes', y='counts', rot=60)
plt.xlabel("Coppie di volumi")
plt.ylabel("Occorrenze")
plt.show()