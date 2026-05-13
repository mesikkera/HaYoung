import json

from typer.testing import CliRunner

from hayoung_generator.main import app


def test_health_command() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["health"])

    assert result.exit_code == 0
    assert "HaYoung data-generator is ready" in result.stdout


def test_show_config_command() -> None:
    runner = CliRunner()

    result = runner.invoke(app, ["show-config"])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == {
        "seed": 42,
        "start_date": "2026-01-01",
        "end_date": "2026-01-30",
        "days": 30,
        "user_count": 1_000,
        "product_count": 300,
        "order_count": 5_000,
        "output_dir": "data/raw",
    }
