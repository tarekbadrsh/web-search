from duckduckgo_search import DDGS

from models import SearchResult


def search(
    query, search_type="text", max_results=5, timelimit=None, region=None
) -> list[SearchResult]:
    """
    Perform a search using DuckDuckGo and return standardized results.

    Args:
        query (str): The search query.
        search_type (str): Type of search ('text', 'news', 'images', 'videos', default: 'text').
        max_results (int): Maximum number of results (default: 5).
        timelimit (str): Time limit for results (e.g., 'd', 'w', 'm', default: None).
        region (str): Region for news search (e.g., 'us-en', default: None).

    Returns:
        list: List of dictionaries with 'title', 'url', and 'snippet'.
    """
    ddgs = DDGS()
    standardized_results: list[SearchResult] = []

    if search_type == "text":
        kwargs = {"max_results": max_results}
        if timelimit is not None:
            kwargs["timelimit"] = timelimit
        results = ddgs.text(query, **kwargs)
        for r in results:
            if r.get("href"):
                standardized_results.append(
                    SearchResult(
                        title=r.get("title", ""),
                        url=r.get("href"),
                        snippet=r.get("body", ""),
                    )
                )

    elif search_type == "news":
        kwargs = {"max_results": max_results}
        if timelimit is not None:
            kwargs["timelimit"] = timelimit
        if region is not None:
            kwargs["region"] = region
        results = ddgs.news(query, **kwargs)
        for r in results:
            if r.get("url"):
                standardized_results.append(
                    SearchResult(
                        title=r.get("title", ""),
                        url=r.get("url"),
                        snippet=r.get("body", ""),
                    )
                )

    elif search_type == "images":
        kwargs = {"max_results": max_results}
        if timelimit is not None:
            kwargs["timelimit"] = timelimit
        if region is not None:
            kwargs["region"] = region
        results = ddgs.images(query, **kwargs)
        for r in results:
            if r.get("url"):
                standardized_results.append(
                    SearchResult(
                        title=r.get("title", ""),
                        url=r.get("url"),
                        snippet=r.get("image", ""),
                    )
                )

    elif search_type == "videos":
        kwargs = {"max_results": max_results}
        if timelimit is not None:
            kwargs["timelimit"] = timelimit
        if region is not None:
            kwargs["region"] = region
        results = ddgs.videos(query, **kwargs)
        for r in results:
            if r.get("url"):
                standardized_results.append(
                    SearchResult(
                        title=r.get("title", ""),
                        url=r.get("url"),
                        snippet=r.get("content", ""),
                    )
                )

    else:
        raise ValueError(f"Invalid search type: {search_type}")

    return standardized_results
