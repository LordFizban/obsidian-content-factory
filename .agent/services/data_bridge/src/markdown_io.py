"""
Markdown I/O Module: Safely reads and updates Markdown tables.
"""
import re
import shutil
from pathlib import Path
from datetime import datetime
from tabulate import tabulate


def backup_file(filepath: Path) -> Path:
    """Create a .bak backup of the file."""
    backup_path = filepath.with_suffix(filepath.suffix + ".bak")
    shutil.copy(filepath, backup_path)
    return backup_path


def parse_markdown_table(lines: list[str]) -> tuple[list[dict], int, int]:
    """
    Parse a Markdown table into a list of dicts.
    Returns: (rows as list of dicts, start_line_index, end_line_index)
    """
    table_start = None
    table_end = None
    header_line = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # Detect table by pipe characters
        if stripped.startswith("|") and stripped.endswith("|"):
            if table_start is None:
                table_start = i
                header_line = i
            table_end = i
        elif table_start is not None and not stripped.startswith("|"):
            # Table has ended
            break
    
    if table_start is None:
        return [], -1, -1
    
    # Parse header
    header = [h.strip() for h in lines[header_line].split("|")[1:-1]]
    
    # Skip separator line (e.g., |---|---|)
    data_start = header_line + 2
    
    rows = []
    for i in range(data_start, table_end + 1):
        cells = [c.strip() for c in lines[i].split("|")[1:-1]]
        if len(cells) == len(header):
            row = dict(zip(header, cells))
            rows.append(row)
    
    return rows, table_start, table_end


def find_week_row(rows: list[dict], week_dates: str) -> int:
    """Find the row index matching a date range."""
    for i, row in enumerate(rows):
        if week_dates in row.get("Dates", ""):
            return i
    return -1


def parse_engagements(lines: list[str]) -> list[dict]:
    """
    Parse the 'Strategic Engagements' section aka Comments.
    """
    engagements = []
    current_item = {}
    
    in_section = False
    for line in lines:
        stripped = line.strip()
        
        # Detect Start
        if "Strategic Engagements" in line and "###" in line:
            in_section = True
            continue
            
        # Detect End (Horizontal Rule or Next Header)
        if in_section:
            if stripped == "---" or (line.startswith("## ") and not "Strategic" in line):
                break
            
            if not stripped.startswith("-"):
                continue
            
            # Check for new item start
            if "**Topic:**" in stripped:
                if current_item:
                    engagements.append(current_item)
                current_item = {}
            
            # Extract key-value
            # Matches: - **Key:** Value
            # We use finding the first colon after **
            match = re.search(r"\*\*(.*?):\*\* (.*)", stripped)
            if match:
                key = match.group(1)
                val = match.group(2)
                current_item[key] = val
        
    if current_item:
        engagements.append(current_item)
        
    return engagements


def update_analytics_log(
    filepath: Path,
    impressions: int,
    date_start: datetime,
    date_end: datetime,
    driver: str = "[Auto-detected]"
) -> bool:
    """Update the Analytics Log markdown table with new data."""
    # (Existing implementation omitted for brevity in replace, but needed for full file)
    # Since I'm using write_to_file, I must include the full content of the function.
    
    backup_file(filepath)
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)
    
    table_section_start = None
    for i, line in enumerate(lines):
        if "### January Data" in line or "| Week |" in line:
            table_section_start = i
            break
    
    if table_section_start is None:
        print("Warning: Could not find data table in Analytics Log")
        return False
    
    rows, t_start, t_end = parse_markdown_table(lines[table_section_start:])
    t_start += table_section_start
    t_end += table_section_start
    
    formatted_dates = f"{date_start.strftime('%b')} {date_start.day}-{date_end.day}"
    row_idx = find_week_row(rows, formatted_dates)
    
    if row_idx == -1:
        print(f"Warning: Could not find row for dates '{formatted_dates}'")
        return False
    
    rows[row_idx]["Total Impressions"] = f"**{impressions}**"
    rows[row_idx]["Primary Driver (Top Content)"] = driver
    
    headers = list(rows[0].keys())
    table_data = [[row.get(h, "") for h in headers] for row in rows]
    new_table = tabulate(table_data, headers=headers, tablefmt="github")
    new_table_lines = [line + "\n" for line in new_table.split("\n")]
    
    new_lines = lines[:t_start] + new_table_lines + lines[t_end + 1:]
    filepath.write_text("".join(new_lines), encoding="utf-8")
    return True
