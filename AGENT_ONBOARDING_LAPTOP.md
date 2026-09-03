# AGENT DIRECTIVE: LAPTOP ONBOARDING & OPERATIONAL RECOVERY PROTOCOL

> **Target Agent**: Antigravity Assistant running on Windows 11 (Laptop Environment).  
> **Mission**: Restore the full Obsidian Content Factory and Obsidian Vault into an operational state on a brand-new machine upon arrival in Japan.

---

## 1. Operating Environment Context

- **Repository**: `LordFizban/obsidian-content-factory` (This repository).
- **Vault Repository**: `LordFizban/obsidian-vault` (Private repository).
- **Default Vault Path**: `$HOME\Documents\Obsidian Vault` (or `%USERPROFILE%\Documents\Obsidian Vault`).
- **Operating System**: Windows 11 (Single drive layout).
- **Key Architecture**:
  - The Vault connects to this project via an NTFS Junction:
    `$HOME\Documents\Obsidian Vault\LinkedIn-Content\Knowledge` -> `<ProjectRoot>\Knowledge`
  - Python Data Bridge reads from dynamic `$HOME\Documents\Obsidian Vault` and `$HOME\Downloads`.

---

## 2. Autonomous Execution Procedure

When activated on the laptop, execute the following steps in sequence:

### Step 1: System Readiness & Dependency Check
Check if Git, Python 3.10+, and Obsidian are available in PATH:
```powershell
git --version
python --version
```
If any prerequisites are missing on the brand-new Windows 11 system, install them via winget:
```powershell
# Run in an elevated or user terminal:
winget install -e --id Git.Git --accept-package-agreements --accept-source-agreements --silent
winget install -e --id Python.Python.3.11 --accept-package-agreements --accept-source-agreements --silent
winget install -e --id Obsidian.Obsidian --accept-package-agreements --accept-source-agreements --silent
```

### Step 2: Ensure Vault is Cloned
Verify if `$HOME\Documents\Obsidian Vault` exists. If not, clone the private vault repo:
```powershell
$vaultDir = "$HOME\Documents\Obsidian Vault"
if (-not (Test-Path $vaultDir)) {
    gh repo clone LordFizban/obsidian-vault $vaultDir
    # Or fallback to git clone if gh is not configured:
    # git clone https://github.com/LordFizban/obsidian-vault.git $vaultDir
}
```

### Step 3: Run the Automated Setup Script
Run the included setup script from the root of this project:
```powershell
.\setup_laptop.ps1
```
This script will:
1. Re-verify the toolchain.
2. Confirm the vault directory.
3. Automatically create/verify the NTFS Junction linking `LinkedIn-Content\Knowledge` to `<ProjectRoot>\Knowledge`.
4. Install all Python dependencies from `.agent/services/data_bridge/requirements.txt`.
5. Run unit tests (`pytest`) across the Data Bridge.

### Step 4: Verify Obsidian Plugins and Local REST API
1. Check that `$HOME\Documents\Obsidian Vault\.obsidian\community-plugins.json` is present and includes:
   - `dataview`
   - `templater-obsidian`
   - `obsidian-tasks-plugin`
   - `calendar`
   - `obsidian-kanban`
   - `obsidian-local-rest-api`
2. Launch Obsidian and select "Open folder as vault" -> Navigate to `$HOME\Documents\Obsidian Vault`.
3. Verify that the Obsidian Local REST API is listening on port `27123` (HTTP) or `27124` (HTTPS):
```powershell
Test-NetConnection -ComputerName 127.0.0.1 -Port 27123
```

### Step 5: Smoke Test the Data Bridge
Verify that the python configuration resolves all paths without errors:
```powershell
python -c "from src import config; print('Vault:', config.VAULT_ROOT, 'Exists:', config.VAULT_ROOT.exists())"
```

---

## 3. Daily Content Factory Workflow for Japan (Agent Reference)

When running content workflows during September:
- **Ideation & Strategy**: Use `@content_strategist` and `@agile_coach` to refine concepts.
- **Drafting & Polishing**: Use `@editor_in_chief` and `avoid-ai-writing` on drafts in `LinkedIn-Content\Drafts`.
- **Localization**: Use `@localization_lead` for Turkish translations.
- **Publishing & Archiving**: Use `@vault_manager` to move approved articles from `Drafts` to `Published\2026` and update `Published-Articles-Archive.md`.
- **Data Ingestion**: Place weekly LinkedIn export `Content_*.xlsx` into `$HOME\Downloads` and run:
  ```powershell
  python .agent/services/data_bridge/run_bridge.py
  ```

---

## 4. Disaster Recovery & Troubleshooting

- **Junction broken / file not found**:
  Rerun:
  ```powershell
  New-Item -ItemType Junction -Path "$HOME\Documents\Obsidian Vault\LinkedIn-Content\Knowledge" -Target "$PSScriptRoot\Knowledge" -Force
  ```
- **Permission errors with junction**:
  Ensure Developer Mode is enabled in Windows 11 Settings (`System` -> `For developers` -> `Developer Mode` = On) or run PowerShell as Administrator.
- **Python package import errors**:
  Reinstall dependencies:
  ```powershell
  python -m pip install -r .agent/services/data_bridge/requirements.txt
  ```
