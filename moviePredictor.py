import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating'] #coloumn names for ratings DataFrame
ratings = pd.read_csv('assets/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1") #read ratings data

m_cols = ['movie_id', 'title']
movies = pd.read_csv('assets/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1") #read movie table

ratings = pd.merge(movies, ratings) #join both tables

ratings.head()

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()

corrMatrix = userRatings.corr()
corrMatrix.head()

corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()

# myRatings = userRatings.loc[0].dropna()
myRatings = pd.read_csv('input.csv', sep='|', names=['title', 'rating'], usecols=range(2), encoding="ISO-8859-1")
myRatings.set_index('title', inplace=True)
print(myRatings)

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # print(myRatings['title'][i])
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings['rating'][i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
# print (simCandidates.head(10))
simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
simCandidates.head(10)

filteredSims = simCandidates.drop(myRatings.index)
print(filteredSims.head(10))