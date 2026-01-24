"""
Ingest Module: Reads LinkedIn Excel exports and normalizes data.
Handles the Turkish pivot-table format.
"""
import glob
from pathlib import Path
from datetime import datetime
import pandas as pd
from .config import DOWNLOADS_DIR, EXCEL_PATTERN, METRIC_MAP


def find_latest_export() -> Path:
    """Find the most recent LinkedIn export file in the Downloads folder."""
    pattern = str(DOWNLOADS_DIR / EXCEL_PATTERN)
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No files matching '{EXCEL_PATTERN}' found in {DOWNLOADS_DIR}")
    # Sort by modification time, newest first
    latest = max(files, key=lambda f: Path(f).stat().st_mtime)
    return Path(latest)


def parse_date_range(header: str) -> tuple[datetime, datetime]:
    """
    Parse LinkedIn's date range header.
    Example: '15.01.2026 - 21.01.2026' -> (datetime(2026, 1, 15), datetime(2026, 1, 21))
    """
    parts = header.split(" - ")
    if len(parts) != 2:
        raise ValueError(f"Invalid date range format: {header}")
    start = datetime.strptime(parts[0].strip(), "%d.%m.%Y")
    end = datetime.strptime(parts[1].strip(), "%d.%m.%Y")
    return start, end


def load_and_normalize(filepath: Path | None = None) -> dict:
    """
    Load the LinkedIn export and normalize to a standard dictionary.
    
    Returns:
        {
            'date_start': datetime,
            'date_end': datetime,
            'impressions': int,
            'unique_views': int,
            ...
        }
    """
    if filepath is None:
        filepath = find_latest_export()
    
    # Read raw Excel without assuming headers
    df = pd.read_excel(filepath, header=None)
    
    # The structure is:
    # Row 0: ['Genel Performans', '15.01.2026 - 21.01.2026'] <- Headers
    # Row 1: ['Görüntülenme', 365]
    # Row 2: ['Erişilen üyelerin sayısı', 179]
    # ...
    
    # Get date range from the first row, second column
    date_header = str(df.iloc[0, 1])  # e.g., '15.01.2026 - 21.01.2026'
    
    try:
        date_start, date_end = parse_date_range(date_header)
    except ValueError:
        date_start = None
        date_end = None
    
    # Build metrics dict
    result = {
        'date_start': date_start,
        'date_end': date_end,
        'raw_filepath': str(filepath),
    }
    
    # Iterate rows to extract metrics (skip row 0 which is the header)
    for i in range(1, len(df)):
        row = df.iloc[i]
        metric_tr = str(row.iloc[0])
        value = row.iloc[1]
        
        # Map Turkish to English
        metric_en = METRIC_MAP.get(metric_tr)
        if metric_en:
            # Normalize key to snake_case
            key = metric_en.lower().replace(" ", "_")
            result[key] = value
    
    return result


def get_week_number(date: datetime) -> int:
    """Return ISO week number for a date."""
    return date.isocalendar()[1]
