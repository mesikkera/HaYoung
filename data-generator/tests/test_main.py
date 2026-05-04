from typer.testing import CliRunner
from hayoung_generator.main import app


def test_health_command() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["health"])

    assert result.exit_code == 0
    assert "HaYoung data-generator is ready" in result.stdout

