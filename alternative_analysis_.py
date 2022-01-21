import pandas as pd
import math

#create a dataframe for our alternative analysis matrix
AA=pd.DataFrame(columns=['criteria','weight','ratingA','ratingB','scoreA','scoreB'])
print(AA)

# First step: add a list of criteria
AA['criteria']=['risk', 'ROI', 'customerSatisfaction', 'feasibility','strategicAlignment']
print(AA)

# second step: identify weights
# weights show relatve importance of each criterion
# they must add up to 1 (or 100 if you use percentage)

AA['weight']=[0.1,0.15,0.3,.15,.3]
print(AA)

# step 3: rate each alternative across all criteria
# choose a scale: 1-5 or 1-7 or 1-10, or 1-3
# higher number: an alternative is doing better with respect to  that specific criterion

AA['ratingA']=[4,1,2,1,5]
AA['ratingB']=[3,4,2,3,2]

#step 4: calculate partial scores by multiplying weights * ratings
for index, row in AA.iterrows():
  AA['scoreA'][index]=row['ratingA']*row['weight']
  AA['scoreB'][index]=row['ratingB']*row['weight']

print(AA)

# step 5: add partial scores to get the total scores
# the solution with the highest score is the winner
totalScoreA=0
totalScoreB=0
for index, row in AA.iterrows():
  totalScoreA+=row['scoreA']
  totalScoreB+=row['scoreB']

print ('the total score for alternative A is {:.2f} and for B is {:.2f}'.format(totalScoreA, totalScoreB))
