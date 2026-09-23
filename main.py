import secrets
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, HttpUrl
from fastapi.responses import RedirectResponse

app = FastAPI()

url_database ={

}

class URLRequest(BaseModel):
    url: HttpUrl


@app.get("/")
def home():
    return {"message": "URL Shortener API is running"}

def generate_short_code():
    secret_code = secrets.token_urlsafe(4)

    while secret_code in url_database:
        secret_code = secrets.token_urlsafe(4)
        
    return secret_code

@app.post("/shorten")
def shorten_url(request: URLRequest, http_request: Request):
    short_code = generate_short_code()
    url_database[short_code] =  str(request.url)

    short_url = str(http_request.base_url) + short_code

    return {
        "original_url": str(request.url),
        "short_code": short_code,
        "short_url": short_url
    }

@app.get("/{short_code}")
def redirect_url(short_code: str):
    original_url = url_database.get(short_code)

    if original_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=original_url)