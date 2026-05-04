import json
import typer

from hayoung_generator import __version__
from hayoung_generator.config import GeneratorConfig

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

@app.command("show-config")
def show_config() -> None:
    """Show the default configuration for data generation."""
    config = GeneratorConfig()
    typer.echo(json.dumps(config.to_dict(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app()
