# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 20:11:38 2023

@author: RanjitPandey1605
"""

import pandas as pd


def countAllVowels(title) :
    title = str(title)
    title = title.lower()
    
    vowelCount = sum(map(title.count, ['a','e','i','o','u']))
    return vowelCount;
    
    
        


data = pd.read_csv('./data/titles.csv')

data['vowelsCount'] = data.apply(lambda row: countAllVowels(row['title']),axis = 1)

print(data)

