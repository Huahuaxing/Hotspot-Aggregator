from backend.app.tasks.celery_app import Celery
from app.settings import settings
import httpx
from bs4 import BeautifulSoup

celery = Celery("hotspot_worker", broker=settings.REDIS_URL, backend=settings.REDIS_URL)

@celery.task
def fetch_page_title(url: str):
    try:
        r = httpx.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "lxml")
        title = soup.title.string if soup.title else "No Title"
        return {"url": url, "title": title}
    except Exception as e:
        return {"error": str(e), "url": url}
