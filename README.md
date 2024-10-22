# YouTube Video Fetcher API
It fetches the latest 10 videos sorted by most recently applied on youtube for the topic `Cricket`. It fetches it from PostgreSQL database. It also returns link to next page if more than 10 videos are present in the database.
- The Celery used in program fetches the latest youtube videos with topic `Cricket` using [YouTube Data API v3](https://developers.google.com/apis-explorer/#p/youtube/v3/) every 10 minutes.
- It uses redis Queue for celery tasks.
- The project is hosted on [render](https://render.com).

## Requirements
- Python 3.x
- Django
- PostgreSQL
- Redis (for Celery)
- YouTube Data API key

### How to use
1. just hit api [here](https://fetchyt.onrender.com)

## endpoints:
1. `/videos` : Fetches the latest 10 videos sorted by most recently applied on youtube for the topic `Cricket`. It fetches it from PostgreSQL database. It also returns link to next page if more than 10 videos are present in the database.

## Local Setup:
1. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up PostgreSQL and Redis on your local machine.

3. create a .env and add following api keys in it:
   ```
   API_KEY_1=
   API_KEY_2=
   API_KEY_3=
   DATABASE_URL=
   ```
3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the Celery worker:
    ```bash
    celery -A youtube_video_fetcher worker --loglevel=info
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Call the API to fetch videos (GET request):
    ```bash
    http://localhost:8000/videos/
    ```
