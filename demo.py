"""
Interactive Movie Recommendation Demo

This script provides an easy-to-use interface for testing your movie recommendation system.
"""

from movie_recommendation_system import MovieRecommendationSystem
import pandas as pd

class MovieRecommendationDemo:
    def __init__(self):
        self.mrs = MovieRecommendationSystem()
        self.movies_loaded = False
        
    def load_system(self):
        """Load the recommendation system"""
        print("🎬 Loading Movie Recommendation System...")
        try:
            # Try to load saved model first
            self.mrs.load_model()
            self.movies_loaded = True
            print("✅ Loaded saved model successfully!")
        except:
            print("📊 No saved model found. Processing data...")
            self.mrs.load_data()
            self.mrs.preprocess_data()
            self.mrs.create_similarity_matrix()
            self.mrs.save_model()
            self.movies_loaded = True
            print("✅ System ready!")
    
    def get_movie_list(self, limit=20):
        """Get a sample of available movies"""
        if not self.movies_loaded:
            self.load_system()
        
        movies = self.mrs.new_df['title'].unique()[:limit]
        return movies
    
    def search_movies(self, search_term):
        """Search for movies containing the search term"""
        if not self.movies_loaded:
            self.load_system()
        
        matching_movies = self.mrs.new_df[
            self.mrs.new_df['title'].str.contains(search_term, case=False, na=False)
        ]['title'].unique()
        
        return matching_movies
    
    def get_recommendations(self, movie_title, num_recommendations=5):
        """Get recommendations for a specific movie"""
        if not self.movies_loaded:
            self.load_system()
        
        recommendations = self.mrs.recommend(movie_title, num_recommendations)
        return recommendations
    
    def run_demo(self):
        """Run the interactive demo"""
        print("🎬 Welcome to the Movie Recommendation System!")
        print("=" * 50)
        
        # Load the system
        self.load_system()
        
        while True:
            print("\n🎯 What would you like to do?")
            print("1. Get recommendations for a movie")
            print("2. Search for movies")
            print("3. See sample movies")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                self.handle_recommendations()
            elif choice == '2':
                self.handle_search()
            elif choice == '3':
                self.show_sample_movies()
            elif choice == '4':
                print("👋 Thanks for using the Movie Recommendation System!")
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
    
    def handle_recommendations(self):
        """Handle getting recommendations"""
        movie_title = input("\n🎬 Enter a movie title: ").strip()
        
        if not movie_title:
            print("❌ Please enter a movie title.")
            return
        
        try:
            num_recs = input("📊 How many recommendations? (default: 5): ").strip()
            num_recs = int(num_recs) if num_recs else 5
        except ValueError:
            num_recs = 5
        
        print(f"\n🔍 Getting recommendations for '{movie_title}'...")
        recommendations = self.get_recommendations(movie_title, num_recs)
        
        if isinstance(recommendations, list):
            print(f"\n🎥 Top {len(recommendations)} recommendations:")
            for i, movie in enumerate(recommendations, 1):
                print(f"   {i}. {movie}")
        else:
            print(f"❌ {recommendations}")
            # Suggest similar movies
            similar = self.search_movies(movie_title.split()[0] if movie_title.split() else movie_title)
            if len(similar) > 0:
                print(f"\n💡 Did you mean one of these?")
                for movie in similar[:5]:
                    print(f"   • {movie}")
    
    def handle_search(self):
        """Handle searching for movies"""
        search_term = input("\n🔍 Enter search term: ").strip()
        
        if not search_term:
            print("❌ Please enter a search term.")
            return
        
        matches = self.search_movies(search_term)
        
        if len(matches) > 0:
            print(f"\n📽️ Found {len(matches)} movies matching '{search_term}':")
            for i, movie in enumerate(matches[:10], 1):  # Show first 10
                print(f"   {i}. {movie}")
            if len(matches) > 10:
                print(f"   ... and {len(matches) - 10} more")
        else:
            print(f"❌ No movies found matching '{search_term}'")
    
    def show_sample_movies(self):
        """Show sample movies"""
        print("\n🎭 Sample movies in the dataset:")
        movies = self.get_movie_list(15)
        for i, movie in enumerate(movies, 1):
            print(f"   {i}. {movie}")
        print("   ... and many more!")

if __name__ == "__main__":
    demo = MovieRecommendationDemo()
    demo.run_demo()