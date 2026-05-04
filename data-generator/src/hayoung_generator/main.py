import typer

from hayoung_generator import __version__

app = typer.Typer(
    name="hayoung-generate",
    help="Sample commerce data generator for the HaYoung data platform.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """HaYoung data-generator CLI."""

@app.command()
def health() -> None:
    """Check whether the data-generator CLI is available."""
    typer.echo(f"HaYoung data-generator is ready. version={__version__}")


if __name__ == "__main__":
    app()
