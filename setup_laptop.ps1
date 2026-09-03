<#
.SYNOPSIS
    Automated Onboarding & Environment Setup for Obsidian Content Factory on Windows 11.
.DESCRIPTION
    Sets up the laptop environment for the Japan trip:
    - Verifies / installs prerequisite tools (Git, Python, Obsidian).
    - Clones or verifies the Obsidian Vault at $HOME\Documents\Obsidian Vault.
    - Recreates the NTFS Junction for Knowledge layer.
    - Installs data_bridge Python requirements and runs self-tests.
#>

[CmdletBinding()]
param(
    [string]$VaultPath = "$HOME\Documents\Obsidian Vault",
    [string]$VaultRepo = "https://github.com/LordFizban/obsidian-vault.git",
    [switch]$InstallPrereqs = $false
)

$ErrorActionPreference = "Stop"

function Write-Header {
    param([string]$Message)
    Write-Host "`n========================================================" -ForegroundColor Cyan
    Write-Host "  $Message" -ForegroundColor Cyan
    Write-Host "========================================================`n" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[✓] $Message" -ForegroundColor Green
}

function Write-WarningMsg {
    param([string]$Message)
    Write-Host "[!] $Message" -ForegroundColor Yellow
}

function Write-ErrorMsg {
    param([string]$Message)
    Write-Host "[✗] $Message" -ForegroundColor Red
}

Write-Header "Obsidian Content Factory - Laptop Onboarding (Japan Travel)"

# ----------------------------------------------------
# 1. Check / Install Prerequisites
# ----------------------------------------------------
Write-Host "Step 1: Checking core tools..." -ForegroundColor White

$missingTools = @()

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    $missingTools += "Git.Git"
} else {
    Write-Success "Git is installed: $((git --version).Trim())"
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    $missingTools += "Python.Python.3.11"
} else {
    Write-Success "Python is installed: $((python --version).Trim())"
}

$obsidianInstalled = Test-Path "$env:LOCALAPPDATA\Obsidian\Obsidian.exe" -ErrorAction SilentlyContinue
if (-not $obsidianInstalled) {
    if (-not (Get-Command obsidian -ErrorAction SilentlyContinue)) {
        $missingTools += "Obsidian.Obsidian"
    } else {
        Write-Success "Obsidian CLI/App detected."
    }
} else {
    Write-Success "Obsidian is installed."
}

if ($missingTools.Count -gt 0) {
    if ($InstallPrereqs) {
        Write-Host "Installing missing tools via winget: $($missingTools -join ', ')..." -ForegroundColor Yellow
        foreach ($toolId in $missingTools) {
            Write-Host "Installing $toolId..." -ForegroundColor Yellow
            winget install --id $toolId -e --accept-source-agreements --accept-package-agreements --silent
        }
        Write-Success "Prerequisite installation triggered. Please restart PowerShell if commands are not yet in PATH."
    } else {
        Write-WarningMsg "Missing tools: $($missingTools -join ', ')"
        Write-WarningMsg "Run with -InstallPrereqs to automatically install via winget, or run:"
        foreach ($toolId in $missingTools) {
            Write-Host "  winget install -e --id $toolId" -ForegroundColor Gray
        }
    }
}

# ----------------------------------------------------
# 2. Verify or Clone Obsidian Vault
# ----------------------------------------------------
Write-Header "Step 2: Checking Obsidian Vault at '$VaultPath'"

$resolvedVaultPath = [System.IO.Path]::GetFullPath($VaultPath)

if (-not (Test-Path $resolvedVaultPath)) {
    Write-Host "Vault directory not found. Cloning from $VaultRepo..." -ForegroundColor Yellow
    $parentDir = Split-Path $resolvedVaultPath -Parent
    if (-not (Test-Path $parentDir)) {
        New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    }
    git clone $VaultRepo $resolvedVaultPath
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Vault cloned successfully to $resolvedVaultPath"
    } else {
        Write-ErrorMsg "Failed to clone vault. Check your GitHub credentials / SSH keys."
        exit 1
    }
} else {
    Write-Success "Vault exists at $resolvedVaultPath"
    if (Test-Path "$resolvedVaultPath\.git") {
        Push-Location $resolvedVaultPath
        Write-Host "Pulling latest changes in vault..." -ForegroundColor Gray
        git pull origin main
        Pop-Location
    }
}

# ----------------------------------------------------
# 3. Recreate Knowledge NTFS Junction
# ----------------------------------------------------
Write-Header "Step 3: Linking Knowledge layer via NTFS Junction"

$projectDir = $PSScriptRoot
$projectKnowledge = Join-Path $projectDir "Knowledge"
$vaultKnowledge = Join-Path $resolvedVaultPath "LinkedIn-Content\Knowledge"

if (-not (Test-Path $projectKnowledge)) {
    Write-ErrorMsg "Project Knowledge directory missing at: $projectKnowledge"
    exit 1
}

if (Test-Path $vaultKnowledge) {
    $item = Get-Item $vaultKnowledge -Force
    if ($item.Attributes -match "ReparsePoint") {
        Write-Success "Knowledge NTFS Junction already exists at $vaultKnowledge"
    } else {
        Write-WarningMsg "Existing directory found at $vaultKnowledge that is not a junction. Backing up..."
        $backupDir = "$vaultKnowledge`_backup_$(Get-Date -Format 'yyyyMMddHHmmss')"
        Rename-Item -Path $vaultKnowledge -NewName $backupDir
        Write-Host "Recreating Junction pointing to $projectKnowledge..." -ForegroundColor Yellow
        New-Item -ItemType Junction -Path $vaultKnowledge -Target $projectKnowledge | Out-Null
        Write-Success "Junction created at $vaultKnowledge -> $projectKnowledge"
    }
} else {
    $vaultLinkedIn = Join-Path $resolvedVaultPath "LinkedIn-Content"
    if (-not (Test-Path $vaultLinkedIn)) {
        New-Item -ItemType Directory -Path $vaultLinkedIn -Force | Out-Null
    }
    Write-Host "Creating Junction pointing to $projectKnowledge..." -ForegroundColor Yellow
    New-Item -ItemType Junction -Path $vaultKnowledge -Target $projectKnowledge | Out-Null
    Write-Success "Junction created at $vaultKnowledge -> $projectKnowledge"
}

# ----------------------------------------------------
# 4. Install Python Dependencies
# ----------------------------------------------------
Write-Header "Step 4: Setting up Python Environment for Data Bridge"

$reqFile = Join-Path $projectDir ".agent\services\data_bridge\requirements.txt"
if (Test-Path $reqFile) {
    Write-Host "Installing data_bridge requirements..." -ForegroundColor Yellow
    python -m pip install -q -r $reqFile
    Write-Success "Python requirements installed."
} else {
    Write-WarningMsg "Requirements file not found at $reqFile"
}

# ----------------------------------------------------
# 5. Run Self-Verification Tests
# ----------------------------------------------------
Write-Header "Step 5: Verifying System Health"

$bridgeTestDir = Join-Path $projectDir ".agent\services\data_bridge"
if (Test-Path $bridgeTestDir) {
    Push-Location $bridgeTestDir
    Write-Host "Running pytest on data bridge..." -ForegroundColor Gray
    python -m pytest --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Data Bridge tests passed successfully!"
    } else {
        Write-WarningMsg "Some tests failed. Check output above."
    }
    Pop-Location
}

Write-Header "SETUP COMPLETE!"
Write-Host "You are all set for operations in Japan!" -ForegroundColor Green
Write-Host "Obsidian Vault: $resolvedVaultPath" -ForegroundColor White
Write-Host "Project Root  : $projectDir" -ForegroundColor White
