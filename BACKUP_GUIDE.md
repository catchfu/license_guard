# Backup & Recovery Guide

**Last Updated:** 2026-02-09

## Project Location
```
C:\QQ\Projects\agent_teams\
```

## Key Files to Preserve

### Session & Documentation
| File | Description |
|------|-------------|
| `SESSION_LOG.md` | Complete conversation history |
| `README.md` | Project overview |

### Brainstorming Team
| File | Description |
|------|-------------|
| `agents/idea_generator.py` | Creative ideation prompts |
| `agents/market_analyst.py` | Business analysis prompts |
| `agents/tech_architect.py` | Technical feasibility prompts |
| `agents/devils_advocate.py` | Risk identification prompts |
| `run_brainstorm.py` | Session runner (prompts) |
| `run_with_claude.py` | Session runner (API) |

### LicenseGuard Build Team
| File | Description |
|------|-------------|
| `licenseguard/project_brief.md` | Product vision |
| `licenseguard/FULL_SPEC.md` | Complete specification |
| `licenseguard/agents/product_lead.py` | PM/BA prompts |
| `licenseguard/agents/ux_content_lead.py` | UX/Writer prompts |
| `licenseguard/agents/engineering_lead.py` | Dev/Architect prompts |
| `licenseguard/agents/qa_engineer.py` | QA prompts |
| `licenseguard/agents/growth_lead.py` | Marketing/Sales prompts |
| `licenseguard/run_licenseguard_team.py` | Team session runner |

## How to Restore

If files are lost, the complete project can be recreated from:
1. `SESSION_LOG.md` - Contains all conversation context
2. `licenseguard/FULL_SPEC.md` - Contains complete product spec

## Quick Recovery Commands

```bash
# Verify all files exist
dir C:\QQ\Projects\agent_teams\ /s

# Run brainstorming team
cd C:\QQ\Projects\agent_teams
python run_brainstorm.py "your niche"

# Run LicenseGuard team
cd C:\QQ\Projects\agent_teams\licenseguard
python run_licenseguard_team.py discovery
```

## Version Control (Recommended)

```bash
cd C:\QQ\Projects\agent_teams
git init
git add .
git commit -m "Initial agent team setup"
```

## Cloud Backup (Optional)

Consider backing up to:
- GitHub private repo
- OneDrive/Google Drive
- Local backup drive
