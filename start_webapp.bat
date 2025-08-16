@echo off
echo Starting Movie Recommendation Web Application...
echo.

REM Activate virtual environment
call movie_rec_env\Scripts\Activate.bat

REM Start Django development server
echo Starting Django server at http://localhost:8000
echo.
echo Open your browser and go to: http://localhost:8000
echo.
echo To stop the server, press Ctrl+C
echo.

python manage.py runserver

pause
