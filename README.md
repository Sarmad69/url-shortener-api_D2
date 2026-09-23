# URL Shortener API

A simple URL Shortener API built with FastAPI as part of my backend development learning journey.

## Features

- Shorten long URLs
- Generate unique short codes
- Redirect short URLs to their original URLs
- URL validation using Pydantic
- Handle invalid short codes with 404 responses

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- uv

## Run Locally

## Limitations

URLs are currently stored in memory, so they are lost when the server restarts.

Install dependencies:

```bash
uv sync