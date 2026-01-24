"""
Pytest fixtures and mock data generators for Data Bridge tests.
"""
import pytest
import pandas as pd
from pathlib import Path
import tempfile


@pytest.fixture
def mock_linkedin_export(tmp_path):
    """Create a mock LinkedIn export Excel file in Turkish format."""
    data = {
        "Genel Performans": ["Görüntülenme", "Erişilen üyelerin sayısı"],
        "15.01.2026 - 21.01.2026": [365, 179]
    }
    df = pd.DataFrame(data)
    filepath = tmp_path / "Content_2026-01-15_2026-01-21_Test.xlsx"
    df.to_excel(filepath, index=False)
    return filepath


@pytest.fixture
def sample_analytics_log(tmp_path):
    """Create a sample Analytics Log markdown file."""
    content = """# 2026 Q1 Analytics Log

### January Data

| Week | Dates | Schedule | Total Impressions | Primary Driver (Top Content) | Net Growth? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Week 2** | Jan 5-11 | Tuesday Only | **659** | Post (Jan 6) | - |
| **Week 3** | Jan 12-18 | Tuesday Only | **234** | Post (Jan 13) | 🔴 -64% |
| **Week 4** | Jan 19-25 | **Tue + Thu (Exp)** | [Insert] | [Insert] | 🟢 Pending |

---
"""
    filepath = tmp_path / "test_analytics_log.md"
    filepath.write_text(content, encoding="utf-8")
    return filepath
