"""
Tests for the markdown_io module.
"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.markdown_io import parse_markdown_table, find_week_row


class TestParseMarkdownTable:
    """Tests for Markdown table parsing."""
    
    def test_parse_simple_table(self):
        """Test parsing a simple markdown table."""
        lines = [
            "| Name | Value |\n",
            "| --- | --- |\n",
            "| Foo | 100 |\n",
            "| Bar | 200 |\n",
        ]
        rows, start, end = parse_markdown_table(lines)
        
        assert len(rows) == 2
        assert rows[0]["Name"] == "Foo"
        assert rows[0]["Value"] == "100"
        assert rows[1]["Name"] == "Bar"
        assert start == 0
        assert end == 3
    
    def test_no_table(self):
        """Test handling content with no table."""
        lines = ["# Header\n", "Some text\n"]
        rows, start, end = parse_markdown_table(lines)
        
        assert rows == []
        assert start == -1


class TestFindWeekRow:
    """Tests for week row matching."""
    
    def test_find_existing_week(self):
        """Test finding a week that exists."""
        rows = [
            {"Week": "**Week 2**", "Dates": "Jan 5-11"},
            {"Week": "**Week 3**", "Dates": "Jan 12-18"},
            {"Week": "**Week 4**", "Dates": "Jan 19-25"},
        ]
        
        idx = find_week_row(rows, "Jan 19-25")
        assert idx == 2
    
    def test_week_not_found(self):
        """Test behavior when week doesn't exist."""
        rows = [{"Week": "**Week 2**", "Dates": "Jan 5-11"}]
        
        idx = find_week_row(rows, "Feb 1-7")
        assert idx == -1
