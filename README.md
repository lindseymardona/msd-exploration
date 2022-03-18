# MSD Exploration

Contributors: lindseymardona, jbfranco21, ryansuwarno

## The Task
Our goal is to aid in exploratory analysis of the Million Songs Dataset through visualizations of the data. There are two classes which assist us in doing so:
- data_visuals_class: This class streamlines the visualization process to compare and/or analyze columns from the dataset.
- ArtistSummary: This class streamlines the process to summarize some general information about the artist and their songs.

## The Dataset
The Million Song Dataset (MSD) is a collection of 1,000,000 contemporary, popular music tracks with their associated audio features and metadata. The songs are mostly of western origina and release years range from 1922 to 2011, with a peak in songs from the 2000s. The dataset used is a subset of the Million Song dataset, with 10,000 tracks.

### Track Information:
Each track description includes the following:
  - **SongNumber** - Number associated with the order in which the song appears in the dataset
  - **SongID** - The Echo Nest song ID
  - **AlbumID** - The Echo Nest album ID
  - **AlbumName** - Name of the Album
  - **ArtistID** - The ID of the artist accorrding to playme.com
  - **ArtistName** - Artist Name
  - **Danceability** - Danceability measure of the song according to The Echo Nest
  - **Duration** - Duration of the song track
  - **KeySignature** - Estimation of the key of the song according to The Echo Nest
  - **Tempo** - Tempo in BPM according to The Echo Nest
  - **TimeSignature** - Time signature of song according to The Echo nest (beats per minute)
  - **Title** - Song Title
  - **Year** - Year when the song was released, according to musicbrainz.org
  - **SongHotness** - According to The Echo Nest, the hotness of the song when downloaded (scale of 0 to 1)

## Installations
The users should pip install the requirements.txt
```
conda create --name msdenv --file requirements.txt
```
or
```
conda create --name msdenv 
conda install pip
pip instal -r requirements.txt
```

## Scope and Limitations
I. While data cleaning, certain songs were removed due to special characters within the album or track titles. Due to this, the dataset is composed of mainly Western music and various tracks from the early 2000's. Also due to the data cleaning of tracks with missing data, the dataset may be heavily skewed to more popular or well-known tracks or artists.

II. The dataset that we are able to obtain is an old data set and it is not complete. There are a lots of missing information such as the song publishing year and song hotness. Other than that we also dropped several columns that have 0 values and NaN values such as Artist Location and KeySignature.

III. Perhaps by being able to obtain more information in the data set we could generates more information and statistics such as the correlation of major types of songs that artist produce in different location. This could help song producers to see songs genre potentials in certain location.


## Description of the demo file

The csv. file used was a randomly chosen subset of the Million Song Dataset. The file included 10,000 tracks in total, but required data cleaning to remove unnecessary columns and tracks with missing data. 

### Data Visualization
We import several modules to gain access to the code in another module. urllib is a package that collects several modules for working with URLs. Pandas is a package that tells Python to bring the pandas data analysis library into your current environment. Numpy is a package to perform a number of mathematical operations on arrays such as trigonometric, statistical, and algebraic routines. Matplotlib.pyplot is a package to generate Pyplot such as Line Plot, Contour, Histogram, Scatter, 3D Plot, etc.

We import python file from data_visual_class.py to get the graph_visuals function. First of all we called the data set that we have already cleaned into the Dataset visualization file. Then, we assign axis strings with axis titles to each variable that we are using. Some tracks are missing values for certain columns. Throughout the visualizations, we will be removing any unknown values for certain columns for proper scatter plot, bar graph, or box plot visualizations.

#### I. Durations vs Tempo

We removed all rows that have 0 values for durations and tempo. We decided to use scatter plotto give us the data correlation between the durations and the tempo of the millions data set. From the result, the information we received is that most song durations are between 200 to 275 seconds, while most songs' tempo is between 80 to 130 beats per minute.
<img width="1102" alt="Screen Shot 2022-03-17 at 4 15 29 PM" src="https://user-images.githubusercontent.com/100387860/158909245-5065db28-d1fd-421a-b766-8fdb1622f486.png">

We generated boxplot for tempo and durations to get more clearer view of the data
<img width="832" alt="Screen Shot 2022-03-17 at 4 15 37 PM" src="https://user-images.githubusercontent.com/100387860/158909276-6b214bcd-97e8-4687-ac03-aaf768e85539.png">

From the “tempo” box plot above, we could see that most songs’ tempo were between 95 to 145 beats per minute, with the median around 120 beats per minute

<img width="832" alt="Screen Shot 2022-03-17 at 4 15 43 PM" src="https://user-images.githubusercontent.com/100387860/158909296-b6a114d6-aa51-40b3-8e1e-8f5c02e80872.png">

From the “duration” box plot above, we could see that most songs' duration were between 180 to 275 seconds, with the median around 210 seconds.

#### II. Tempo vs Time Signature
In order to get the data correlation between the tempo and time signature, we use a scatter plot. As the result, we see that most songs were at 1 beat per bar and 4 beats per bar.
<img width="1115" alt="Screen Shot 2022-03-17 at 4 27 24 PM" src="https://user-images.githubusercontent.com/100387860/158910148-48ff62b0-d74c-461b-8119-b6e28c332b3f.png">

#### III. Durations vs Time Signature
In order to get the data correlation between the durations of the song and the time signature, we use a scatter plot. We drops any rows where the seconds for Duration is longer than 700 in order to get better for viewing patterns. As the result, we see that most song were at 4 beats per bar with durations 100 to 400 seconds.
<img width="1107" alt="Screen Shot 2022-03-17 at 4 36 20 PM" src="https://user-images.githubusercontent.com/100387860/158910962-5f0e4957-56f8-4e62-84d1-136688564787.png">

#### IV. Durations vs Song Hotness
In order to get the data correlation between the durations of the song and the song hotness, we use a scatter plot.
<img width="1109" alt="Screen Shot 2022-03-17 at 4 36 30 PM" src="https://user-images.githubusercontent.com/100387860/158910990-dee5c3cc-ace4-4a20-9bb2-deda38fff45e.png">

#### V. Year of Song Released
In order to get the data of the numbers of songs that are released every year, we use a histograms and bar graph. As the result, we see that most song were produced after 2000. We also could see that the number of song produce every year is increase from the previous year.
<img width="1117" alt="Screen Shot 2022-03-17 at 4 36 38 PM" src="https://user-images.githubusercontent.com/100387860/158911007-af7b4cb7-4374-449a-aa0a-0768ccbf26e7.png">
<img width="1106" alt="Screen Shot 2022-03-17 at 4 36 51 PM" src="https://user-images.githubusercontent.com/100387860/158911019-ff8da8c4-0629-4b8b-aefa-d2baac589c74.png">

#### VI. Most Songs' Released With Certain Tempo
In order to get the data of the numbers of songs that are released for certain tempo, we use a histograms. As the result, we see that most artist produce their songs with tempo between 100 to 150 beats per minute
<img width="1104" alt="Screen Shot 2022-03-17 at 4 37 11 PM" src="https://user-images.githubusercontent.com/100387860/158911035-0cd3e13d-57ee-484b-91c9-7d66d78a73d3.png">


### Artist Summary Demo
The purpose of this Artist Summary file is to get certain data from the data set. We imported the ArtistSummary file to get the ArtistSummary function. We also use panda modules in this file. First of all we called the data set that we have already cleaned into the ArtistSummary Demo file. 

#### Retrieving Artist with the most data
We start by retrieving the artist with the most data available. Then we print the data set of the artist and it resulted that Mario Rosenstock have the most song in this data set.

<img width="1101" alt="Screen Shot 2022-03-17 at 5 50 25 PM" src="https://user-images.githubusercontent.com/100387860/158916762-ccd41f09-ae42-4ec7-a09f-1140029f0b84.png">

Then we call function summary() in order to get the informations and statistics summary of Mario Rosenstock. We got the information such as the artist name, artist id, average song durations of Rosenstock's song is 201.2 seconds, average song tempo of Rosenstock's song is 108.19 beats per minute, and his hottest song which is "Smoke". 

<img width="246" alt="Screen Shot 2022-03-17 at 5 56 52 PM" src="https://user-images.githubusercontent.com/100387860/158917391-91b5d39d-f006-4c86-b22b-915e3b4b96cc.png">

We also could get the information of the artist's activity which is how many songs that been produced every year for that specific artist. We could call the function by calling activity function. But for Mario Rosenstock, we are unable to get information of his activity because we do not have any information within the dataset regarding the years his song were released. 

<img width="283" alt="Screen Shot 2022-03-17 at 6 00 50 PM" src="https://user-images.githubusercontent.com/100387860/158917724-d4e314d6-4509-4baa-ade7-82283ace48f4.png">

We also could get informations and statistics of any artist in the data set. We gave two artist example in this project which is Sonora Santanera and Rick Astley"
##### Example 1
Artist name: Sonora Santanera
Artist ID: ARKRRTF1187B9984DA
Average song duration: 165.3
Average song tempo: 99.54
Error: No song hotness data available.

##### Example 2
Artist name: Rick Astley
Artist ID: ARWPYQI1187FB4D55A
Average song duration: 224.46
Average song tempo: 125.44
Hottest song: Never Gonna Give You Up (1987)

In the second example, in the data we have the information of the artist's activity per year. Therefore we could get the data of the numbers of song that Rick Astley produce for certain years.

<img width="1116" alt="Screen Shot 2022-03-17 at 6 06 50 PM" src="https://user-images.githubusercontent.com/100387860/158918443-8f888b14-e66e-491d-9e42-7fbcbf482e4b.png">

Lastly, we try to get the statistics and information of the artist that is not listed in the data set and it will resulted an error.

<img width="816" alt="Screen Shot 2022-03-17 at 6 08 17 PM" src="https://user-images.githubusercontent.com/100387860/158918319-9dc51364-aaa9-433a-8ea8-d7509e32b4d6.png">

## Licenses

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References
Project utilizes the Million Song Dataset:
Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011.
[link](http://millionsongdataset.com/)

UCI data description:
Dua, D. and Graff, C. (2019). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science. [link](http://archive.ics.uci.edu/ml/citation_policy.html)
