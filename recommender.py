import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("C:/Users/Priyanshee/OneDrive/Documents/netflix-recommender/dataset/netflix_titles.csv")

# Fill missing descriptions
df["description"] = df["description"].fillna("")

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["description"])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index for mapping
df = df.reset_index()

# Function to get recommendations
def get_recommendations(title):
    title = title.lower()
    indices = df[df["title"].str.lower() == title].index

    if len(indices) == 0:
        return ["Sorry! Movie not found in dataset."]

    idx = indices[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # top 5 recommendations

    movie_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[movie_indices].tolist()
