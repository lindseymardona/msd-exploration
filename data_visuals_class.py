from matplotlib import pyplot as plt
import random
import pandas as pd
import numpy as np

def get_randcolor():
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    r = random.random()
    b = random.random()
    g = random.random()
    return (r, g, b)

def_title = '0'

class graph_visuals:
    '''
    will have various methods to help visual pieces of data together, inputs are columns of type objects
    input:
    - will consists of three variables, three columns of the data set
    '''
    def __init__(self, var1, var1_title, var2 = [0], var2_title = '0', bins = 0):
        self.var1 = var1
        self.var2 = var2
        self.var1_title = var1_title
        self.var2_title = var2_title
        self.bins = bins
    
    def scatter_plot(self):
        fig, ax = plt.subplots(1, figsize=(25,12))
        ax.set(xlabel = self.var1_title, ylabel = self.var2_title, title = self.var1_title + 'vs.' + self.var2_title)
        ax.scatter(self.var1, self.var2, alpha = 0.6, c=get_randcolor())
        
    def frequency_bar_graph(self):
        fig, ax = plt.subplots(1, figsize=(25,12))
        self.var1.value_counts().plot(ax=ax, kind='bar', xlabel=self.var1_title, ylabel='Frequency', title = self.var1_title + ' with Frequncy')
    
    def hist_graph(self):
        fig, ax = plt.subplots(1, figsize=(25,12))
        ax.set(xlabel = self.var1_title, ylabel = 'Frequency', title = self.var1_title + ' with Frequency')
        ax.hist(self.var1, self.bins)
        
