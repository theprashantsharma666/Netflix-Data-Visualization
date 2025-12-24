# Step 1 :- Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2 :- Load the data
df = pd.read_csv('netflix_titles.csv')

# clean data
df = df.dropna(subset=['type','release_year','rating','duration'])

# Plotting bar graph between Number of Movies vs TV Shows on Netflix
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

# Plotting pie chart on percentage of content rating
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle = 90)
plt.title('Percentage of content rating')
plt.tight_layout()
plt.savefig('content_ratings_pie.png')
plt.show()

# Plotting Histogram on Distribution of Movie Duration
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min','').astype('int')
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins = 30 , color = 'purple',edgecolor='black')
plt.xlabel('Duartion (minutes)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Duration')
plt.tight_layout()
plt.savefig('movie_duartion_histogram.png')
plt.show()

# Plotting Scstter plot between Release year vs Number of show
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.xlabel('Release Year')
plt.ylabel('Number of show')
plt.title('Release year vs Number of show')
plt.tight_layout()
plt.savefig('release_year_scatter.png')
plt.show()

# Plotting Horizontal bar graph of Top 10 countries by number of shows
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.title('Top 10 countries by number of shows')
plt.tight_layout()
plt.savefig('top10_countries.png')
plt.show()

# SUBPLOTS

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax = plt.subplots(1,2,figsize=(12,5))

# Subplots movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movie released per year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of movies')

ax[1].plot(content_by_year.index,content_by_year['TV Show'],color='orange')
ax[1].set_title('TV Shows released per year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Years')
plt.tight_layout()
plt.savefig('movies_TV_Shows_comparison.png')
plt.show()