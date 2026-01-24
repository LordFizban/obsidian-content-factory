# Data Bridge Configuration
from pathlib import Path

# Paths
VAULT_ROOT = Path(r"c:\Users\kaann\Documents\Obsidian Vault")
DOWNLOADS_DIR = Path(r"D:\Downloads")

# Source file pattern (LinkedIn export)
EXCEL_PATTERN = "Content_*.xlsx"

# Target files
ANALYTICS_LOG = VAULT_ROOT / "LinkedIn-Content" / "Analytics" / "2026_Q1_Analytics_Log.md"
ARCHIVE_LOG = VAULT_ROOT / "LinkedIn-Content" / "Published" / "Archive" / "Published Articles Archive.md"
CONTENT_DASHBOARD = VAULT_ROOT / "LinkedIn-Content" / "Content-Strategy" / "Content Dashboard.md"
PUBLISHED_DIR = VAULT_ROOT / "LinkedIn-Content" / "Published"

# Turkish to English metric mapping
METRIC_MAP = {
    "Görüntülenme": "Impressions",
    "Erişilen üyelerin sayısı": "Unique Views",
    "Etkileşimler": "Engagements",
    "Etkileşim oranı": "Engagement Rate",
    "Yorumlar": "Comments",
    "Paylaşımlar": "Shares",
    "Beğeniler": "Likes",
}
