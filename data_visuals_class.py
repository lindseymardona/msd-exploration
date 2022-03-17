from matplotlib import pyplot as plt
import random
import pandas as pd
import numpy as np

def get_randcolor():
    '''
    Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.
    '''
    r = random.random()
    b = random.random()
    g = random.random()
    return (r, g, b)

def_title = '0'

class graph_visuals:
    '''
    Contains various methods to help visualize pieces of data together.
    '''
    def __init__(self, var1, var1_title, var2 = [0], var2_title = '0', bins = 0):
        '''
        Initializes an object of graph_visuals.
        Inputs:
        - var1, var2: lists which are columns from the data
        - var1_title, var2_title: strings containing the titles for the axes
        - bins: int indicating how many groups the data will be sorted into
        '''
        self.var1 = var1
        self.var2 = var2
        self.var1_title = var1_title
        self.var2_title = var2_title
        self.bins = bins
    
    def scatter_plot(self):
        '''
        Creates a scatterplot using the two data columns of interest.
        '''
        # creat subplot and appropriate axis titles
        fig, ax = plt.subplots(1, figsize=(25,12))
        ax.set(xlabel = self.var1_title, ylabel = self.var2_title, title = self.var1_title + ' vs. ' + self.var2_title)
        ax.scatter(self.var1, self.var2, alpha = 0.6, c=get_randcolor())
        
    def frequency_bar_graph(self):
        '''
        Creates a bar graph using one column of interest to display the frequency of occurrence.
        '''
        fig, ax = plt.subplots(1, figsize=(25,12))
        # plots frequency of each value for the chosen column
        self.var1.value_counts().plot(ax=ax, kind='bar', xlabel=self.var1_title, ylabel='Frequency', title = self.var1_title + ' with Frequency')
    
    def hist_graph(self):
        '''
        Creates a histogram using one column of interest to display the frequency of occurrence.
        '''
        # plots the frequency of each value of a chosen column using bins
        fig, ax = plt.subplots(1, figsize=(25,12))
        ax.set(xlabel = self.var1_title, ylabel = 'Frequency', title = self.var1_title + ' with Frequency')
        ax.hist(self.var1, self.bins)
        
