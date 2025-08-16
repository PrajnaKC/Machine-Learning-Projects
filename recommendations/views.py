from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import sys
import os

# Add the parent directory to the path to import our recommendation system
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from movie_recommendation_system import MovieRecommendationSystem

# Global instance to avoid reloading the model for each request
recommendation_system = None

def index(request):
    """Serve the main HTML page"""
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static', 'index.html'), 'r') as f:
        html_content = f.read()
    return HttpResponse(html_content)

def get_recommendation_system():
    """Get or initialize the recommendation system"""
    global recommendation_system
    if recommendation_system is None:
        recommendation_system = MovieRecommendationSystem()
        try:
            recommendation_system.load_model()
        except:
            # If model doesn't exist, create it
            recommendation_system.load_data()
            recommendation_system.preprocess_data()
            recommendation_system.create_similarity_matrix()
            recommendation_system.save_model()
    return recommendation_system

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({'status': 'healthy', 'message': 'Movie Recommendation API is running'})

@api_view(['GET'])
def get_movies(request):
    """Get list of available movies"""
    try:
        mrs = get_recommendation_system()
        movies = mrs.new_df['title'].unique().tolist()
        
        # Paginate results
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 50))
        start = (page - 1) * page_size
        end = start + page_size
        
        paginated_movies = movies[start:end]
        
        return Response({
            'movies': paginated_movies,
            'total': len(movies),
            'page': page,
            'page_size': page_size,
            'has_next': end < len(movies)
        })
    except Exception as e:
        return Response(
            {'error': f'Failed to get movies: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def search_movies(request):
    """Search for movies by title"""
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response(
            {'error': 'Search query is required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        mrs = get_recommendation_system()
        matching_movies = mrs.new_df[
            mrs.new_df['title'].str.contains(query, case=False, na=False)
        ]['title'].unique().tolist()
        
        return Response({
            'query': query,
            'movies': matching_movies[:20],  # Limit to 20 results
            'total_found': len(matching_movies)
        })
    except Exception as e:
        return Response(
            {'error': f'Search failed: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
def get_recommendations(request):
    """Get movie recommendations"""
    movie_title = request.data.get('movie_title', '').strip()
    num_recommendations = request.data.get('num_recommendations', 5)
    
    if not movie_title:
        return Response(
            {'error': 'Movie title is required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        num_recommendations = int(num_recommendations)
        if num_recommendations < 1 or num_recommendations > 20:
            num_recommendations = 5
    except (ValueError, TypeError):
        num_recommendations = 5
    
    try:
        mrs = get_recommendation_system()
        recommendations = mrs.recommend(movie_title, num_recommendations)
        
        if isinstance(recommendations, list):
            return Response({
                'movie_title': movie_title,
                'recommendations': recommendations,
                'total_recommendations': len(recommendations)
            })
        else:
            # Movie not found, suggest similar movies
            similar_movies = mrs.new_df[
                mrs.new_df['title'].str.contains(
                    movie_title.split()[0] if movie_title.split() else movie_title, 
                    case=False, na=False
                )
            ]['title'].unique().tolist()[:5]
            
            return Response({
                'error': f"Movie '{movie_title}' not found",
                'suggestions': similar_movies
            }, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response(
            {'error': f'Recommendation failed: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_movie_details(request, movie_title):
    """Get details for a specific movie"""
    try:
        mrs = get_recommendation_system()
        movie_data = mrs.new_df[mrs.new_df['title'] == movie_title]
        
        if movie_data.empty:
            return Response(
                {'error': f"Movie '{movie_title}' not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        movie_info = movie_data.iloc[0]
        
        return Response({
            'title': movie_info['title'],
            'movie_id': int(movie_info['movie_id']),
            'tags_preview': ' '.join(movie_info['tags'].split()[:10]) + '...'
        })
    except Exception as e:
        return Response(
            {'error': f'Failed to get movie details: {str(e)}'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
