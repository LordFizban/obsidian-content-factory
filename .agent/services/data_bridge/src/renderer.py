"""
Renderer Module: Generates Mermaid charts and Recent Content tables for the Content Dashboard.
"""
from pathlib import Path
from datetime import datetime
from tabulate import tabulate
import re
from .config import ANALYTICS_LOG, CONTENT_DASHBOARD, PUBLISHED_DIR, ARCHIVE_LOG
from .markdown_io import parse_markdown_table, parse_engagements


def generate_recent_content_table() -> str:
    """Generate a markdown table of the 10 most recent files in Published."""
    if not PUBLISHED_DIR.exists():
        return "<!-- Published directory not found -->"
        
    files = list(PUBLISHED_DIR.rglob("*.md"))
    file_data = []
    for f in files:
        if "Archive" in str(f):
            continue
        mtime = f.stat().st_mtime
        dt = datetime.fromtimestamp(mtime)
        file_data.append({"path": f, "title": f.stem, "date": dt, "mtime": mtime})
    
    file_data.sort(key=lambda x: x["mtime"], reverse=True)
    top_10 = file_data[:10]
    
    if not top_10:
        return "<!-- No published content found -->"
        
    table_rows = []
    for item in top_10:
        date_str = item["date"].strftime("%Y-%m-%d")
        link = f"[[{item['title']}]]"
        table_rows.append([date_str, link])
        
    return tabulate(table_rows, headers=["Date", "Article"], tablefmt="github")


def generate_engagements_table() -> str:
    """Generate a markdown table from the Strategic Engagements section of the log."""
    if not ARCHIVE_LOG.exists():
        return "<!-- Archive Log not found -->"
        
    log_content = ARCHIVE_LOG.read_text(encoding="utf-8")
    log_lines = log_content.splitlines()
    
    engagements = parse_engagements(log_lines)
    
    if not engagements:
        return "<!-- No engagements found -->"
        
    # Take top 5
    top = engagements[:5]
    table_rows = []
    for e in top:
        date = e.get("Date", "")
        topic = e.get("Topic", "Unknown")
        context = e.get("Context", "")
        # Truncate context if too long
        if len(context) > 50:
            context = context[:47] + "..."
        link = e.get("Link", "")
        
        table_rows.append([date, topic, context, link])
        
    return tabulate(table_rows, headers=["Date", "Topic", "Context", "Link"], tablefmt="github")


def generate_impressions_chart(rows: list[dict]) -> str:
    """Generate a Mermaid xychart-beta (bar chart) for weekly impressions."""
    valid_rows = []
    for row in rows:
        impressions = row.get("Total Impressions", "")
        clean = impressions.replace("**", "").replace("*", "").strip()
        if clean.isdigit():
            valid_rows.append({'week': row.get("Week", ""), 'impressions': int(clean)})
    
    if not valid_rows:
        return "<!-- No valid impression data for chart -->"
    
    weeks = [r['week'] for r in valid_rows]
    values = [r['impressions'] for r in valid_rows]
    
    return f'''```mermaid
xychart-beta
    title "Weekly Impressions (2026)"
    x-axis [{", ".join(f'"{w}"' for w in weeks)}]
    y-axis "Impressions" 0 --> {max(values) + 100}
    bar [{", ".join(str(v) for v in values)}]
```'''


def update_dashboard(dashboard_path: Path = CONTENT_DASHBOARD) -> bool:
    """Update the Content Dashboard with fresh Mermaid charts and Recent Content."""
    # 1. Update Charts
    log_content = ANALYTICS_LOG.read_text(encoding="utf-8")
    log_lines = log_content.splitlines()
    rows, _, _ = parse_markdown_table(log_lines)
    
    chart_replacement = ""
    if rows:
        chart_replacement = generate_impressions_chart(rows)
    
    # 2. Update Recent Content
    recent_table = generate_recent_content_table()
    
    # 3. Update Engagements
    engagements_table = generate_engagements_table()
    
    # Read dashboard
    if not dashboard_path.exists():
        dashboard_content = f'''# Content Dashboard

## 📊 2026 Goals
... (Static content) ...

## 📈 Weekly Performance
<!-- DATA_BRIDGE_START -->
{chart_replacement}
<!-- DATA_BRIDGE_END -->

## 📰 Recent Content
<!-- RECENT_CONTENT_START -->
{recent_table}
<!-- RECENT_CONTENT_END -->

## 💬 Recent Engagements
<!-- ENGAGEMENTS_START -->
{engagements_table}
<!-- ENGAGEMENTS_END -->
'''
        dashboard_path.write_text(dashboard_content, encoding="utf-8")
        return True
    
    content = dashboard_path.read_text(encoding="utf-8")
    
    def replace_block(text, start_marker, end_marker, new_content):
        pattern = f"{start_marker}.*?{end_marker}"
        replacement = f"{start_marker}\n{new_content}\n{end_marker}"
        if start_marker in text:
            return re.sub(pattern, replacement, text, flags=re.DOTALL)
        else:
            return text + f"\n\n## 💬 Recent Engagements\n{replacement}\n"

    content = replace_block(content, "<!-- DATA_BRIDGE_START -->", "<!-- DATA_BRIDGE_END -->", chart_replacement)
    content = replace_block(content, "<!-- RECENT_CONTENT_START -->", "<!-- RECENT_CONTENT_END -->", recent_table)
    content = replace_block(content, "<!-- ENGAGEMENTS_START -->", "<!-- ENGAGEMENTS_END -->", engagements_table)
    
    dashboard_path.write_text(content, encoding="utf-8")
    return True
