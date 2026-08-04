from __future__ import annotations

import logging
import re
from pathlib import Path
from time import perf_counter

import pandas as pd


def ensure_directory(path: Path) -> Path:
    """Create the directory if it does not exist and return it."""
    path.mkdir(parents=True, exist_ok=True)
    return path


def clean_string_value(value: object) -> str | None:
    """Return a cleaned string value while keeping original letter casing."""
    if pd.isna(value):
        return None
    text = str(value)
    text = text.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    text = "".join(char for char in text if char.isprintable())
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


def normalize_text_key(value: object) -> str | None:
    """Normalize a text key for resilient, case-insensitive lookup joins."""
    cleaned = clean_string_value(value)
    if cleaned is None:
        return None
    return cleaned.upper()


def normalize_identifier_key(value: object) -> str | None:
    """Normalize identifier-like keys without forcing uppercase."""
    return clean_string_value(value)


def strip_trailing_zero(value: object) -> object:
    """Convert numeric-looking strings ending in .0 into integer-like strings."""
    cleaned = clean_string_value(value)
    if cleaned is None:
        return None
    if re.fullmatch(r"[+-]?\d+\.0+", cleaned):
        return cleaned.split(".", maxsplit=1)[0]
    return cleaned


def coerce_numeric_column(series: pd.Series) -> pd.Series:
    """Coerce a Series to numeric values where possible."""
    return pd.to_numeric(series, errors="coerce")


def coerce_string_column(series: pd.Series) -> pd.Series:
    """Coerce a Series to pandas string dtype with empty values as NA."""
    coerced = series.astype("string")
    return coerced.replace("", pd.NA)


def setup_logging(log_dir: Path, log_name: str = "phase1.log") -> logging.Logger:
    """Configure logger for Phase 1 ingestion."""
    ensure_directory(log_dir)
    logger = logging.getLogger("orderbook_automation_phase1")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        file_handler = logging.FileHandler(log_dir / log_name, encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger


class Timer:
    """Simple context timer to track execution duration."""


    def __init__(self) -> None:
        self.start = 0.0
        self.end = 0.0

    def __enter__(self) -> "Timer":
        self.start = perf_counter()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end = perf_counter()


    @property
    def elapsed_seconds(self) -> float:
        if self.start == 0.0:
            return 0.0
        if self.end == 0.0:
            return max(perf_counter() - self.start, 0.0)
        return max(self.end - self.start, 0.0)
