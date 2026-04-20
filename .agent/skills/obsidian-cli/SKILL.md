---
name: obsidian-cli
description: "Use the Obsidian CLI to read, create, search, and manage vault content. This skill is configured to use the Local REST API to bypass system command conflicts."
risk: unknown
source: "https://github.com/kepano/obsidian-skills"
date_added: "2026-04-20"
---

# Obsidian CLI

Use this skill to interact with the running Obsidian instance. 

## Special Instructions (REST Mode)
Since local binary conflicts exist (obsidian pointing to test tools), the agent should favor using direct PowerShell/curl calls to the Local REST API (Port 27123) with the OBSIDIAN_API_KEY.

## Command reference
- obsidian read path="folder/note.md" -> GET /vault/folder/note.md
- obsidian search query="term" -> POST /search/gui
- obsidian backlinks file="Note" -> GET /search/backlinks?path=Note.md

## Pattern reference
- obsidian property:set name="status" value="done" file="My Note"
- obsidian search query="search term" limit=10
- obsidian backlinks file="My Note"
