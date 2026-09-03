"""
Digest Module: Auto-generates monthly performance digests from the Analytics Log.
"""
import re
from pathlib import Path
from datetime import datetime
from .config import VAULT_ROOT, ANALYTICS_LOG, PUBLISHED_DIR

def generate_digest(month_name: str = None) -> bool:
    """Compile weekly analytics into a monthly digest with strategy validation checks."""
    if not month_name:
        month_name = datetime.now().strftime("%B")
        
    print(f"Generating performance digest for: {month_name}")
    
    # Read Analytics Log
    if not ANALYTICS_LOG.exists():
        print(f"Error: Analytics Log not found at {ANALYTICS_LOG}")
        return False
        
    log_content = ANALYTICS_LOG.read_text(encoding="utf-8")
    lines = log_content.splitlines()
    
    month_weeks = {
        "April": ["Week 14", "Week 15", "Week 16", "Week 17"],
        "May": ["Week 18", "Week 19", "Week 20", "Week 21", "Week 22"],
        "June": ["Week 23", "Week 24", "Week 25", "Week 26"]
    }
    
    target_weeks = month_weeks.get(month_name.capitalize(), [])
    if not target_weeks:
        print(f"Error: No week mappings configured for month: {month_name}")
        return False
        
    total_impressions = 0
    post_count = 0
    weekly_stats = []
    
    in_table = False
    headers = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("| Week |"):
            in_table = True
            headers = [h.strip() for h in stripped.split("|")[1:-1]]
            continue
        if in_table and not stripped.startswith("|"):
            in_table = False
            continue
        if in_table and stripped.startswith("|:---"):
            continue
        if in_table:
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if len(cells) == len(headers):
                row = dict(zip(headers, cells))
                week_name = row.get("Week", "").replace("**", "").strip()
                if any(w in week_name for w in target_weeks):
                    imps_str = row.get("Total Impressions", "0").replace("**", "").replace("~", "").replace(",", "").strip()
                    try:
                        imps = int(imps_str)
                    except ValueError:
                        imps = 0
                    
                    total_impressions += imps
                    drivers = row.get("Primary Driver", "")
                    if drivers.strip():
                        parts = [d.strip() for d in drivers.split(",") if d.strip()]
                        post_count += len(parts)
                        
                    weekly_stats.append({
                        "week": week_name,
                        "dates": row.get("Dates", ""),
                        "impressions": imps,
                        "driver": drivers
                    })
                    
    if not weekly_stats:
        print(f"Warning: No data found in Analytics Log for weeks: {target_weeks}")
        return False
        
    avg_imps = total_impressions / len(weekly_stats) if weekly_stats else 0
    
    # Count Turkish content metrics
    tr_count = 0
    en_count = 0
    tr_imps = 0
    en_imps = 0
    
    for stat in weekly_stats:
        driver = stat["driver"]
        # Broad regex pattern matching name and whatever is inside parentheses
        matches = re.findall(r"([A-Za-z0-9'\s:\u00c0-\u017f\.\-ŞşİıÇçÖöÜüĞğÂâ’]+)\s*\(([^\)]+)\)", driver)
        for name, imp_val in matches:
            name_clean = name.strip()
            # Extract digits only from the value parenthetical
            digits = re.search(r"\d+", imp_val.replace(",", ""))
            if not digits:
                continue
            val = int(digits.group(0))
            
            if name_clean.startswith("TR") or "TR:" in name_clean:
                tr_count += 1
                tr_imps += val
            else:
                en_count += 1
                en_imps += val
            
    total_parsed_imps = tr_imps + en_imps
    tr_share = (tr_imps / total_parsed_imps * 100) if total_parsed_imps > 0 else 0
    
    # Pillar balance count
    files = list(PUBLISHED_DIR.rglob("*.md"))
    pillar_counts = {"AI in Scrum": 0, "Manager Partnership": 0, "Psychological Safety": 0, "Continuous Improvement": 0}
    total_h2_posts = 0
    for f in files:
        if "Archive" in str(f):
            continue
        text = f.read_text(encoding="utf-8")
        p_match = re.search(r"pillar:\s*(.*)", text)
        if p_match:
            p_val = p_match.group(1).strip()
            for k in pillar_counts.keys():
                if k.lower() in p_val.lower() or p_val.lower() in k.lower():
                    pillar_counts[k] += 1
                    total_h2_posts += 1
                    break
                    
    pillar_pct = {}
    for k, v in pillar_counts.items():
        pillar_pct[k] = (v / total_h2_posts * 100) if total_h2_posts > 0 else 0
        
    pillar_alerts = []
    targets = {"AI in Scrum": (15, 20), "Manager Partnership": (30, 40), "Psychological Safety": (20, 30), "Continuous Improvement": (20, 30)}
    for k, (low, high) in targets.items():
        pct = pillar_pct.get(k, 0)
        if pct < low - 5 or pct > high + 5:
            pillar_alerts.append(f"\u26a0\ufe0f {k} is at {pct:.1f}% (Target: {low}-{high}%)")
            
    digest_dir = VAULT_ROOT / "LinkedIn-Content" / "Analytics" / "Digests"
    digest_dir.mkdir(parents=True, exist_ok=True)
    
    digest_file = digest_dir / f"2026_{month_name}_Performance_Digest.md"
    
    # Pre-calculate string representations for conditional statuses and alerts
    if pillar_alerts:
        joined_alerts = "\n".join(pillar_alerts)
        alerts_text = f"### \u26a0\ufe0f Pillar Deviations Detected:\n{joined_alerts}"
    else:
        alerts_text = "### \u2705 Pillar Balance Aligned"
        
    if tr_share >= 25:
        status_text = "\u2705 Active Reach Driver"
    else:
        status_text = "\u26a0\ufe0f Under target reach (Target: \u226525% share)"
        
    digest_md = f"""# \U0001f4ca Performance Digest \u2014 {month_name} 2026

## \U0001f4c8 High-Level Metrics
- **Total Impressions:** {total_impressions:,}
- **Average Impressions/Week:** {avg_imps:.1f}
- **Estimated Posting Frequency:** {len(weekly_stats)} weeks, {post_count} posts total ({post_count/len(weekly_stats):.1f} posts/week)

## \U0001f1f9\U0001f1f7 Localization Strategy Health
- **Turkish Reach Share:** {tr_share:.1f}% of total impressions
- **Turkish Posts Count:** {tr_count} translated / original posts
- **Status:** {status_text}

## \U0001f3af Pillar Balance Compliance (H2 YTD)
- **Total Posts Counted:** {total_h2_posts}
- **AI in Scrum:** {pillar_counts['AI in Scrum']} posts ({pillar_pct['AI in Scrum']:.1f}%) \u2014 Target: 15-20%
- **Manager Partnership:** {pillar_counts['Manager Partnership']} posts ({pillar_pct['Manager Partnership']:.1f}%) \u2014 Target: 35%
- **Psychological Safety:** {pillar_counts['Psychological Safety']} posts ({pillar_pct['Psychological Safety']:.1f}%) \u2014 Target: 25%
- **Continuous Improvement:** {pillar_counts['Continuous Improvement']} posts ({pillar_pct['Continuous Improvement']:.1f}%) \u2014 Target: 25%

{alerts_text}

## \U0001f4dd Weekly Summary
"""
    for stat in weekly_stats:
        digest_md += f"- **{stat['week']}** ({stat['dates']}): {stat['impressions']:,} impressions | Drivers: {stat['driver']}\n"
        
    digest_file.write_text(digest_md, encoding="utf-8")
    print(f"Digest generated successfully at: {digest_file.name}")
    return True