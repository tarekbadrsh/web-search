# cli.py
import click

from core import perform_full_search


@click.group()
def cli():
    """Command-line interface for the search engine."""
    pass


@cli.command(name="search")
@click.argument("query")
@click.option("--search-type", default="text", help="Type of search: 'text' or 'news'")
@click.option("--max-results", default=5, help="Maximum number of results")
@click.option(
    "--timelimit", default=None, help="Time limit for results (e.g., 'd', 'w', 'm')"
)
@click.option("--region", default=None, help="Region for news search (e.g., 'us-en')")
def search_cmd(query, search_type, max_results, timelimit, region):
    """
    Search for a query and display results with full content.

    Args:
        query (str): The search query to execute.
        search_type (str): 'text' or 'news'.
        max_results (int): Maximum number of results.
        timelimit (str): Time limit for results.
        region (str): Region for news search.
    """
    # Delegate all logic to core
    full_results = perform_full_search(
        query, search_type, max_results, timelimit, region
    )

    if not full_results:
        click.echo("No results found.")
        return

    # Display the results
    print("Search done successfully, and results saved to file.")
