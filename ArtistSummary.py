from matplotlib import pyplot as plt
import pandas as pd
from Error import EmptyListError
from data_visuals_class import graph_visuals

class ArtistSummary:
    '''
    Analyzes the artist's data and summarizes their data.
    '''
    
    def __init__(self, df, name):
        '''
        Initializes an ArtistSummary object.
        Arguments:
        - df, a dataframe consisting of artists and their data.
        - name, the name of the artist to analyze.
        '''
        self.name = name
        self.df = df.loc[df['ArtistName'] == self.name]
    
    def summary(self):
        '''
        Prints the summary statistics for the ArtistSummary object.
        '''
        try:
            if self.df.empty: # checks if the artist exists within the DataFrame
                raise EmptyListError
            print("Artist name:", self.name)
            print("Artist ID:", self.df['ArtistID'].iloc[0])
            print("Average song duration:", round(self.df['Duration'].mean(), 2))
            print("Average song tempo:", round(self.df['Tempo'].mean(), 2))
            print("Hottest song:", self.hottestSong()['Title'], '(%s)' % self.hottestSong()['Year'])
        except EmptyListError: # raised if the artist has no info within the DataFrame
            print("Error: DataFrame is empty.")
        except TypeError: # raised when trying to access indexes of a hottestSong that doesn't exist
            print("Error: No song hotness data available.")
            
    def activity(self):
        '''
        Displays a visualization for the artist's yearly activity.
        '''
        temp = self.df.loc[self.df['Year'] != 0] # drop rows with no Year data
        try:
            if temp.empty:
                raise EmptyListError
            viz = graph_visuals(self.df['Year'], 'Year')
            viz.frequency_bar_graph() # creates a bar graph for songs released in a year
            print("%s made the least songs in %s." % (self.name, temp['Year'].value_counts().idxmin()))
            print("%s made the most songs in %s." % (self.name, temp['Year'].value_counts().idxmax()))
        except EmptyListError: # raised if after dropping empty Year rows, DataFrame is empty
            return("Error: No year data available.")
        
    def hottestSong(self):
        '''
        Finds the information for the artist's hottest song.
        '''
        temp = self.df.dropna(subset=['SongHotness']) # drop rows with no SongHotness data 
        try:
            if temp.empty:
                raise EmptyListError
            hottestSong = self.df.loc[self.df['SongHotness'].idxmax()] # retrieves the row with highest song hotness
            return hottestSong
        except EmptyListError: # raised if after dropping empty song hotness rows, DataFrame is empty
            return("Error: No song hotness data available.")