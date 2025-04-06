# core.py
import json
import logging
import time
import traceback

from content import get_content_urls
from groqai import get_content_summary
from models import FullSearchResult
from search import search

logger = logging.getLogger(__name__)


def perform_full_search(
    query, search_type="text", max_results=5, timelimit=None, region=None
) -> FullSearchResult:
    """
    Perform a full search: retrieve search results and fetch full content for each.

    Args:
        query (str): The search query.
        search_type (str): Type of search ('text', 'news', etc.).
        max_results (int): Maximum number of results.
        timelimit (str): Time limit for results (e.g., 'd', 'w', 'm').
        region (str): Region for news search (e.g., 'us-en').

    Returns:
        FullSearchResult: A list of search results with AI summaries.
    """
    try:
        # Step 1: Perform the search using DuckDuckGo
        results = search(query, search_type, max_results, timelimit, region)

        # Step 2: Fetch full content for each result using Jina AI
        full_results = get_content_urls(results)

        # Step 3: Get a summary of the content
        full_content_str = "\n".join([result.content for result in full_results])
        ai_summary = get_content_summary(full_content_str)
        final_result = FullSearchResult(
            search_results=full_results, ai_summary=ai_summary
        )

        new_file_result = f"{int(time.time())}.json"
        with open(new_file_result, "w") as f:
            json.dump(final_result.model_dump(), f, indent=4, ensure_ascii=False)
        return final_result
    except Exception as e:
        tb = traceback.format_exc()
        logger.error(f"Error performing full search: {e}\n{tb}")
        return FullSearchResult(search_results=[], ai_summary=str(e))
