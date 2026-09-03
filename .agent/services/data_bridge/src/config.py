# Data Bridge Configuration
import os
from pathlib import Path

# Paths (dynamically determined, configurable via environment variables)
VAULT_ROOT = Path(os.environ.get("OBSIDIAN_VAULT_ROOT", str(Path.home() / "Documents" / "Obsidian Vault")))

# Fallback: Check if D:\Downloads exists (Desktop setup), otherwise default to user Downloads folder
default_downloads = Path(r"D:\Downloads") if Path(r"D:\Downloads").exists() else Path.home() / "Downloads"
DOWNLOADS_DIR = Path(os.environ.get("DOWNLOADS_DIR", str(default_downloads)))

# Source file pattern (LinkedIn export)
EXCEL_PATTERN = "Content_*.xlsx"

# Target files
import glob
analytics_dir = VAULT_ROOT / "LinkedIn-Content" / "Analytics"
log_files = sorted(glob.glob(str(analytics_dir / "*_Analytics_Log.md")))
if log_files:
    ANALYTICS_LOG = Path(log_files[-1])
else:
    ANALYTICS_LOG = analytics_dir / "2026_Q1_Analytics_Log.md"

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
