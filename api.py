# api.py
from fastapi import FastAPI

from core import perform_full_search

app = FastAPI(title="Search Engine API")


@app.get("/search")
def search_api(
    q: str,
    search_type: str = "text",
    max_results: int = 5,
    timelimit: str = None,
    region: str = None,
):
    """
    Search endpoint to retrieve results and full content for a given query.
    """
    # Delegate all logic to core
    full_results = perform_full_search(q, search_type, max_results, timelimit, region)
    return full_results
