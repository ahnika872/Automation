import os

BASE_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = os.getenv("c15cc9d0-2009-46b0-a800-46c1ae0000fd")  # Токен хранится в переменной окружения
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}