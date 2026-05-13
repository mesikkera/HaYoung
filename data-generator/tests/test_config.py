from datetime import date
from pathlib import Path

from hayoung_generator.config import GeneratorConfig


def test_default_config() -> None:

    config = GeneratorConfig()
    assert config.seed == 42
    assert config.start_date == date(2026, 1, 1)
    assert config.days == 30
    assert config.end_date == date(2026, 1, 30)
    assert config.user_count == 1_000
    assert config.product_count == 300
    assert config.order_count == 5_000
    assert config.output_dir == Path("data/raw")


def test_config_to_dict() -> None:
    config = GeneratorConfig()
    config_dict = config.to_dict()
    assert config_dict["start_date"] == "2026-01-01"
    assert config_dict["end_date"] == "2026-01-30"
    assert config_dict["output_dir"] == "data/raw"
