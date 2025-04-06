from typing import Dict, Optional

from pydantic import BaseModel


class SearchResult(BaseModel):
    url: str = None
    title: Optional[str] = None
    snippet: Optional[str] = None
    content: Optional[str] = None
    description: Optional[str] = None
    links: Optional[Dict[str, str]] = None
    images: Optional[Dict[str, str]] = None
    error: Optional[str] = None
    ai_summary: Optional[str] = None


class FullSearchResult(BaseModel):
    search_results: list[SearchResult]
    ai_summary: str
