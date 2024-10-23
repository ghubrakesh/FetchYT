# YouTube Video Fetcher API
It fetches the latest 10 videos sorted by most recently applied on youtube for the topic `Cricket`. It fetches it from PostgreSQL database that is hosted on Render. It also returns link to next page if more than 10 videos are present in the database.
- The Celery used in program fetches the latest youtube videos with topic `Cricket` using [YouTube Data API v3](https://developers.google.com/apis-explorer/#p/youtube/v3/) every 10 seconds.
- It uses redis Queue for celery tasks (redis runs locally).
  
## Requirements
- Python 3.x
- Django
- PostgreSQL
- Redis (for Celery)
- YouTube Data API key

## endpoints:
1. `/videos` : Fetches the latest 10 videos sorted by most recently applied on youtube for the topic `Cricket`. It fetches it from PostgreSQL database. It also returns link to next page if more than 10 videos are present in the database.
2. `admin/youtube_api/video/` : List of all the videos stored in database. List, sort, and filter videos. (Needs login credentials as given below)
   
### To access all videos and sort/filter out all videos 
- use admin panel at http://127.0.0.1:8000/admin/youtube_api/video/
- use credentials as:
  ```yaml
  Username: demo_user
  Password: Pass@123
  ```
- View, Filter and sort the videos.

## Local Setup:
1. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
    
2. create a .env and add following api keys in it:
   ```
   API_KEY_1=
   API_KEY_2=
   API_KEY_3=
   DATABASE_URL=
   ```
   
3. Set up and run celery worker:
   ```bash
   celery -A fetchyt worker --loglevel=info
   ```

4. Set up and run celery beat to run celery task on every 10 seconds:
   ```bash
   celery -A fetchyt beat --loglevel=info
   ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

6. Call the API to fetch videos (GET request):
    ```bash
    http://localhost:8000/videos/
    ```
      
### Request (cURL):
```bash
curl --location 'http://127.0.0.1:8000/videos/' \
--header 'Cookie: csrftoken=t0eeRMdX3IyI37c9bLsI3nvljJ0N1vMG'
```
### Response format:
```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "next": "(http://127.0.0.1:8000/videos/)",
    "previous": "http://127.0.0.1:8000/videos/?page=3",
    "results": [
        {
            "video_id": "",
            "title": "",
            "description": "",
            "publish_datetime": "YYYY-MM-DDTHH:MM:SSZ",
            "thumbnail_urls": {
                "high": {
                    "url": "",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "",
                    "width": ,
                    "height": 
                },
                "default": {
                    "url": "",
                    "width": ,
                    "height":
                }
            }
        }
    ]
}
```
