import pandas as pd
df=pd.read_csv('bestsellers.csv')  #df is a dataframe obj
print(df.head())   #gets first 5 rows of the spreadsheet
print(df.shape)    #gets shape of spreadsheet
print(df.columns)
print(df.describe())     #gets summary statistics for each column

df.drop_duplicates(inplace=True)  #setting inplace to true the changes are made directly into the original df

df.rename(columns={"Name":"Title",
                   "Year":"Publication Year",
                   "User Rating":"Rating"},
                     inplace =True)

df["Price"]=df["Price"].astype(float)   #astype() converts type

author_counts=df["Author"].value_counts()
print(author_counts)

avg_rating_by_genre=df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#export top 10 selling authors to a csv file
author_counts.head(10).to_csv("top_authors.csv")
#exporting avg rating by genre
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
