import logging
import os
import traceback

import requests
from dotenv import load_dotenv

from models import SearchResult

load_dotenv()

logger = logging.getLogger(__name__)


def get_content(search_result: SearchResult) -> SearchResult:
    """
    Fetch the content of a URL using the Jina Reader API.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        dict or None: JSON content if successful, None if failed.
    """
    try:
        headers = {
            "Authorization": f"Bearer {os.getenv('JINA_API_KEY')}",
            "Accept": "application/json",
            "X-Engine": "browser",
            "X-Return-Format": "markdown",
            "X-Timeout": "10",
            "X-Token-Budget": "200000",
            "X-With-Images-Summary": "true",
            "X-With-Links-Summary": "true",
        }
        response = requests.get(
            f"https://r.jina.ai/{search_result.url}", headers=headers
        )
        if response.status_code == 200:
            response_obj = response.json().get("data", {})
            if response_obj.get("content"):
                search_result.content = response_obj.get("content")
            if response_obj.get("description"):
                search_result.description = response_obj.get("description")
            if response_obj.get("links"):
                search_result.links = response_obj.get("links")
            if response_obj.get("images"):
                search_result.images = response_obj.get("images")
            if response_obj.get("title"):
                search_result.title = response_obj.get("title")
            return search_result
        return SearchResult(error=response.text)
    except Exception as e:
        tb = traceback.format_exc()
        logger.error(f"Error fetching content from {search_result.url}: {e}\n{tb}")
        return SearchResult(error=str(e))


def get_content_urls(search_results: list[SearchResult]) -> list[SearchResult]:
    """
    Fetch the content of a list of URLs using the Jina Reader API.
    """

    # Step 2: Fetch full content for each result using Jina AI
    full_results: list[SearchResult] = []
    for search_result in search_results:
        try:
            search_result = get_content(search_result)
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f"Error fetching content from {search_result.url}: {e}\n{tb}")
            search_result.error = str(e)
        full_results.append(search_result)

    return full_results
