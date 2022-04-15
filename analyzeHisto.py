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
import glob

path = '/home/simone/Documents/thesis/not_sorted/'

pairs_files = glob.glob(path + 'hist_ns*.csv')
print(len(pairs_files))     # why only 1320?
pairs_files.sort()

# let's start with the first file 
#dataframes = [pd.read_csv(pairs_files[0]),pd.read_csv(pairs_files[1])]
#print(pd.read_csv(pairs_files[0]))
#print(pd.read_csv(pairs_files[1]))
#first_pairs_df = pd.concat(dataframes)
first_pairs_df = pd.read_csv(pairs_files[0])
print(pairs_files[0])
print(first_pairs_df)
col = pd.DataFrame(first_pairs_df['pairIndex'])
plt.hist(col.values, bins=1000)
plt.show()      # So far so good

# now we sort all the hist corresponding to volume 7
pairs_ = {}
for i in range(col.size):
    if (first_pairs_df['volume1'][i] == 7):
        if str(first_pairs_df['pair'][i]) in pairs_.keys():
            pairs_[str(first_pairs_df['pair'][i])] += 1
        else: 
            pairs_[str(first_pairs_df['pair'][i])] = 1
plt.bar(pairs_.keys(), pairs_.values())
plt.xticks(rotation = 45) 
figsize = (20, 20)
#plt.yscale("log")
plt.show()

# let's try to make an histogram with all the pairs exept the ones with 0 occurences
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
        if (first_pairs_df['volume1'][i] == vol):
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