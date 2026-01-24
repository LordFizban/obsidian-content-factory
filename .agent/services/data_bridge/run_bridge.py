#!/usr/bin/env python
"""
Data Bridge CLI: Main entry point for the LinkedIn Analytics automation.

Usage:
    py run_bridge.py --auto       # Auto-detect latest export and update logs
    py run_bridge.py --dry-run    # Show what would be updated without writing
    py run_bridge.py --query X    # Query specific metric (for agent integration)
"""
import argparse
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.ingest import find_latest_export, load_and_normalize
from src.markdown_io import update_analytics_log
from src.renderer import update_dashboard
from src.config import ANALYTICS_LOG


def main():
    parser = argparse.ArgumentParser(description="Data Bridge: LinkedIn Analytics Automation")
    parser.add_argument("--auto", action="store_true", help="Auto-update from latest export")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be updated")
    parser.add_argument("--query", type=str, help="Query a specific metric (e.g., 'impressions')")
    parser.add_argument("--file", type=str, help="Specify a specific Excel file to process")
    
    args = parser.parse_args()
    
    # Find or specify file
    if args.file:
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"Error: File not found: {filepath}")
            return 1
    else:
        try:
            filepath = find_latest_export()
            print(f"Found export: {filepath.name}")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1
    
    # Load and normalize data
    try:
        data = load_and_normalize(filepath)
    except Exception as e:
        print(f"Error parsing Excel: {e}")
        return 1
    
    # Query mode: just return a specific metric
    if args.query:
        key = args.query.lower().replace(" ", "_")
        if key in data:
            print(data[key])
        else:
            print(f"Unknown metric: {args.query}")
            print(f"Available: {list(data.keys())}")
            return 1
        return 0
    
    # Dry run: show data without updating
    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"Date Range: {data.get('date_start')} - {data.get('date_end')}")
        print(f"Impressions: {data.get('impressions')}")
        print(f"Unique Views: {data.get('unique_views')}")
        print("No files were modified.")
        return 0
    
    # Auto mode: update everything
    if args.auto:
        print("=== AUTO UPDATE ===")
        print(f"Source: {filepath.name}")
        print(f"Date Range: {data.get('date_start')} to {data.get('date_end')}")
        print(f"Impressions: {data.get('impressions')}")
        
        # Update the Analytics Log
        if data.get('date_start') and data.get('impressions'):
            success = update_analytics_log(
                ANALYTICS_LOG,
                impressions=data['impressions'],
                date_start=data['date_start'],
                date_end=data['date_end']
            )
            if success:
                print(f"✅ Updated: {ANALYTICS_LOG.name}")
            else:
                print(f"⚠️ Could not update Analytics Log (row not found)")
        
        # Update the Dashboard
        update_dashboard()
        print(f"✅ Updated: Content Dashboard")
        
        return 0
    
    # Default: just show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
