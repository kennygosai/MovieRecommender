# MovieRecommender
Using Item-Based Collaborative Filtering, this script recommends you movies based on how you rated movies.

### Input
A .csv file with the with the tehe csv file in the form

Movie Name (Year) | Rating
----------------- | ------

A sample csv file is provided as input.csv

### Output

Movie Name (Year) | Number which tells you how well the movie correlates with the input
---------|--------


## How it works
Combines two data sets into one Ratings table which looks like this

DataFrame ID |movie_id|	title |	user_id |	rating
-------------|--------|-------|---------|--------
0|1|Toy Story (1995)|308|4
1|1|Toy Story (1995)|287|5
2|1|Toy Story (1995)|148|4
3|1|Toy Story (1995)|280|4
4|1|Toy Story (1995)|66|3

Then pivots the table making each film as the column names and the Datafram ID as the row names.
