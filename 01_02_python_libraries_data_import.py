#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################01_02_PythonLibraries#####################################################
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt 

#import data
data = pd.read_csv("../Datasets/insurance.csv")

#see the first 15 lines of data
print(data.head(15))







