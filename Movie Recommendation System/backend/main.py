from fastapi import FastAPI
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
from api.recommend import router
from models.movie import Movie


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)