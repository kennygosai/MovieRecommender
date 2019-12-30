# MovieRecommender
Using Item-Based Collaborative Filtering, this script recommends you movies based on how you rated movies.

### Execution
run command:

python moviePredictor.py < input.txt >

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

Then pivots the table making each film as the column names and the Datafram ID as the row names. Using pandas built-in corr() method, a matrix is created with a correlation scored for every columna pair giving us the correlation score between every pair of movies.

Title|'Til There Was You (1997)|1-900 (1994)|101 Dalmatians (1996)|12 Angry Men (1957)|187 (1997)|2 Days in the Valley (1996)|20,000 Leagues Under the Sea (1954)|2001: A Space Odyssey (1968)|3 Ninjas: High Noon At Mega Mountain (1998)
----|------|------|------|------|------|------|------|------|------
'Til There Was You (1997)|1.0|NaN|-1.000000|-0.500000|-0.500000|0.522233|NaN|-0.426401|NaN
1-900 (1994)|NaN|1.0|NaN|NaN|NaN|NaN|NaN|-0.981981|NaN
101 Dalmatians (1996)|-1.0|NaN|1.000000|-0.049890|0.269191|0.048973|0.266928|-0.043407|NaN|0.111111
12 Angry Men (1957)|-0.5|NaN|-0.049890|1.000000|0.666667|0.256625|0.274772|0.178848|NaN|0.457176
187 (1997)|-0.5|NaN|0.269191|0.666667|1.000000|0.596644|NaN|-0.554700|NaN|1.000000

However this data shows that certain 'outlier' movies with not many votes can throw off the correlation between movie's and ratings. To fix this we restrict the results to movies where there are greator than 100 users rated in a given movie pair.

Then for the given input we take each input movie title and retrieve all of the movies which have a correlation with the input movie. Then multiply the rating from the correlation matrix with the input rating to scale the rated movie based on the users rating.
The list is then sorted and the top 10 results are returned.
