"""
Tests for the ingest module.
"""
import pytest
from datetime import datetime
import sys
from pathlib import Path

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.ingest import parse_date_range, load_and_normalize, get_week_number


class TestParseDateRange:
    """Tests for date range parsing."""
    
    def test_valid_date_range(self):
        """Test parsing a standard LinkedIn date range."""
        start, end = parse_date_range("15.01.2026 - 21.01.2026")
        assert start == datetime(2026, 1, 15)
        assert end == datetime(2026, 1, 21)
    
    def test_invalid_format(self):
        """Test that invalid formats raise ValueError."""
        with pytest.raises(ValueError):
            parse_date_range("January 2026")


class TestGetWeekNumber:
    """Tests for week number calculation."""
    
    def test_week_3(self):
        """Jan 15, 2026 should be week 3."""
        date = datetime(2026, 1, 15)
        assert get_week_number(date) == 3
    
    def test_week_4(self):
        """Jan 22, 2026 should be week 4."""
        date = datetime(2026, 1, 22)
        assert get_week_number(date) == 4


class TestLoadAndNormalize:
    """Tests for Excel loading and normalization."""
    
    def test_load_mock_export(self, mock_linkedin_export):
        """Test loading a mock LinkedIn export file."""
        data = load_and_normalize(mock_linkedin_export)
        
        # Check that impressions were mapped correctly
        assert "impressions" in data
        assert data["impressions"] == 365
        
        # Check unique views
        assert "unique_views" in data
        assert data["unique_views"] == 179
