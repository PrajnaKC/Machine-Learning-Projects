import numpy as np
import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommendationSystem:
    def __init__(self):
        self.movies = None
        self.new_df = None
        self.similarity = None
        self.cv = None
        
    def load_data(self, movies_path='tmdb_5000_movies.csv', credits_path='tmdb_5000_credits.csv'):
        """Load and merge movie and credits datasets"""
        self.movies = pd.read_csv(movies_path)
        credits = pd.read_csv(credits_path, engine='python')
        
        # Merge datasets
        self.movies = self.movies.merge(credits, on='title')
        
        # Select relevant columns
        self.movies = self.movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        
        print(f"Dataset shape: {self.movies.shape}")
        return self.movies.head()
    
    def convert(self, text):
        """Convert JSON string to list of names"""
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name'])
        return L
    
    def convert3(self, text):
        """Convert and limit to top 3 cast members"""
        L = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter < 3:
                L.append(i['name'])
            counter += 1
        return L
    
    def fetch_director(self, text):
        """Extract director from crew data"""
        L = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
        return L
    
    def collapse(self, L):
        """Remove spaces from names"""
        L1 = []
        for i in L:
            L1.append(i.replace(" ", ""))
        return L1
    
    def preprocess_data(self):
        """Preprocess the movie data"""
        # Remove null values
        self.movies.dropna(inplace=True)
        
        # Convert JSON strings to lists
        self.movies['genres'] = self.movies['genres'].apply(self.convert)
        self.movies['keywords'] = self.movies['keywords'].apply(self.convert)
        self.movies['cast'] = self.movies['cast'].apply(self.convert3)
        self.movies['crew'] = self.movies['crew'].apply(self.fetch_director)
        
        # Remove spaces from names
        self.movies['cast'] = self.movies['cast'].apply(self.collapse)
        self.movies['crew'] = self.movies['crew'].apply(self.collapse)
        self.movies['genres'] = self.movies['genres'].apply(self.collapse)
        self.movies['keywords'] = self.movies['keywords'].apply(self.collapse)
        
        # Split overview into words
        self.movies['overview'] = self.movies['overview'].apply(lambda x: x.split())
        
        # Create tags column
        self.movies['tags'] = (self.movies['overview'] + 
                              self.movies['genres'] + 
                              self.movies['keywords'] + 
                              self.movies['cast'] + 
                              self.movies['crew'])
        
        # Create new dataframe
        self.new_df = self.movies.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])
        self.new_df['tags'] = self.new_df['tags'].apply(lambda x: " ".join(x))
        
        return self.new_df.head()
    
    def create_similarity_matrix(self):
        """Create similarity matrix using CountVectorizer and cosine similarity"""
        self.cv = CountVectorizer(max_features=5000, stop_words='english')
        vector = self.cv.fit_transform(self.new_df['tags']).toarray()
        
        self.similarity = cosine_similarity(vector)
        print(f"Similarity matrix shape: {self.similarity.shape}")
        
        return self.similarity
    
    def recommend(self, movie_title, num_recommendations=5):
        """Recommend movies based on similarity"""
        try:
            index = self.new_df[self.new_df['title'] == movie_title].index[0]
            distances = sorted(list(enumerate(self.similarity[index])), 
                             reverse=True, key=lambda x: x[1])
            
            recommendations = []
            for i in distances[1:num_recommendations+1]:
                recommendations.append(self.new_df.iloc[i[0]].title)
            
            return recommendations
        except IndexError:
            return f"Movie '{movie_title}' not found in database."
    
    def save_model(self, movie_list_path='movie_list.pkl', similarity_path='similarity.pkl'):
        """Save the processed data and similarity matrix"""
        pickle.dump(self.new_df, open(movie_list_path, 'wb'))
        pickle.dump(self.similarity, open(similarity_path, 'wb'))
        print("Model saved successfully!")
    
    def load_model(self, movie_list_path='movie_list.pkl', similarity_path='similarity.pkl'):
        """Load the processed data and similarity matrix"""
        self.new_df = pickle.load(open(movie_list_path, 'rb'))
        self.similarity = pickle.load(open(similarity_path, 'rb'))
        print("Model loaded successfully!")

# Example usage
if __name__ == "__main__":
    # Initialize the recommendation system
    mrs = MovieRecommendationSystem()
    
    # Load and preprocess data
    print("Loading data...")
    mrs.load_data()
    
    print("Preprocessing data...")
    mrs.preprocess_data()
    
    print("Creating similarity matrix...")
    mrs.create_similarity_matrix()
    
    # Get recommendations
    print("\nRecommendations for 'Gandhi':")
    recommendations = mrs.recommend('Gandhi')
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")
    
    # Save the model
    mrs.save_model()
