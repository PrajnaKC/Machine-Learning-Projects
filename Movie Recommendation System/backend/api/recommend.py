from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pickle

router = APIRouter()

# Load the movie list and similarity matrix
with open('movie_list.pkl', 'rb') as f:
    movie_list = pickle.load(f)
    print('movie_list type:', type(movie_list))
    if hasattr(movie_list, 'shape'):
        print('movie_list shape:', movie_list.shape)
    if hasattr(movie_list, 'columns'):
        print('movie_list columns:', movie_list.columns)
    if hasattr(movie_list, 'head'):
        print('movie_list sample:', movie_list.head())

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)
    print('similarity type:', type(similarity))
    if hasattr(similarity, '__len__'):
        print('similarity length:', len(similarity))

@router.get("/recommend/{movie_title}")
def get_recommendations(movie_title: str):
    try:
        index = movie_list[movie_list['title'].str.lower() == movie_title.lower()].index[0]
    except IndexError:
        return JSONResponse(status_code=404, content={"message": "Movie not found."})

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movie_list.iloc[i[0]].title)

    return {"recommendations": recommended_movies}