# Insight Data Engineering - Coding Challenge

#object#

1. Clean and extract the text from the raw JSON tweets that come from the Twitter Streaming API, and track the number of tweets that contain unicode.

2. Calculate the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds, and update this each time a new tweet appears.

environment:Windows

system: win 8 64bit


external library:python-dateutil( pip install python-dateutil)

#Directories#
tweet_input: the tweets used in this project

tweet_output:the result of the project,containing two txt documents:ft1,ft2

ft1:the results of the first feature,clean tweets

ft2:the results of this second feature,the average degree of a vertex in a Twitter hashtag graph for the last 60 seconds

scr:the python code

tweets_cleaned.py :the source code for the first feature

average_degree.py :the source code for the second feature

run.sh: a shell script that runs the program
