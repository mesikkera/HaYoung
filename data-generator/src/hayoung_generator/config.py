from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass(frozen=True)
class GeneratorConfig:
    """Configuration for sample commerce data generation."""

    seed: int = 42
    start_date: date = date(2026, 1, 1)
    days: int = 30
    user_count: int = 1_000
    product_count: int = 300
    order_count: int = 5_000
    output_dir: Path = Path("data/raw")

    @property
    def end_date(self) -> date:
        """Return the last date included in the generated dataset."""

        return date.fromordinal(self.start_date.toordinal() + self.days - 1)

    def to_dict(self) -> dict[str, str | int]:
        """Return config as a serializable dictionary."""

        return {
            "seed": self.seed,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "days": self.days,
            "user_count": self.user_count,
            "product_count": self.product_count,
            "order_count": self.order_count,
            "output_dir": str(self.output_dir),
        }
