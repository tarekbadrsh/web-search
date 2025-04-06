import click
import uvicorn

from api import app as api_app
from cli import cli as cli_group


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """Entry point for the search engine application."""
    if ctx.invoked_subcommand is None:
        # Run API by default if no subcommand is provided
        ctx.invoke(api)


# Add CLI as a subcommand
main.add_command(cli_group, name="cli")


@main.command()
def api():
    """Run the web API server."""
    uvicorn.run(api_app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
