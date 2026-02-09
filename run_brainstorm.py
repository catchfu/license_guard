#!/usr/bin/env python3
"""
Agent Team Brainstorming Session Runner

Orchestrates a multi-agent brainstorming session for niche market tool ideas.
Each agent provides a different perspective to thoroughly vet ideas.
"""

import sys
from datetime import datetime
from pathlib import Path

# Agent prompts
from agents.idea_generator import SYSTEM_PROMPT as IDEA_PROMPT
from agents.market_analyst import SYSTEM_PROMPT as MARKET_PROMPT
from agents.tech_architect import SYSTEM_PROMPT as TECH_PROMPT
from agents.devils_advocate import SYSTEM_PROMPT as DEVIL_PROMPT


def create_session_prompt(niche: str) -> str:
    """Create the full brainstorming session prompt."""

    return f"""
# Agent Team Brainstorming Session
**Niche/Topic:** {niche}
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## PHASE 1: Idea Generation

{IDEA_PROMPT}

**Your task:** Generate 5-7 tool ideas for the niche: "{niche}"

---

## PHASE 2: Market Analysis

{MARKET_PROMPT}

**Your task:** Analyze the business potential of each generated idea.

---

## PHASE 3: Technical Assessment

{TECH_PROMPT}

**Your task:** Evaluate technical feasibility and architecture for each idea.

---

## PHASE 4: Devil's Advocate Challenge

{DEVIL_PROMPT}

**Your task:** Challenge each idea and identify weaknesses.

---

## PHASE 5: Final Synthesis

Based on all perspectives, provide:

### Top 3 Recommended Ideas (Ranked)
For each:
1. **Idea Name & One-liner**
2. **Why It Scored Highest** (across all dimensions)
3. **Key Risk to Mitigate First**
4. **Suggested First Step**
5. **90-Day Goal** (what success looks like)

### Ideas to Shelve
- List ideas that didn't pass scrutiny and why

### Quick Wins
- Any low-effort, high-potential ideas worth testing immediately

---

Begin the brainstorming session now. Work through each phase systematically.
"""


def save_session(niche: str, output: str) -> Path:
    """Save brainstorming session to file."""
    sessions_dir = Path(__file__).parent / "sessions"
    sessions_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_niche = "".join(c if c.isalnum() else "_" for c in niche)[:30]
    filename = f"{timestamp}_{safe_niche}.md"

    filepath = sessions_dir / filename
    filepath.write_text(output, encoding="utf-8")

    return filepath


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_brainstorm.py \"<niche or problem area>\"")
        print("\nExamples:")
        print('  python run_brainstorm.py "tools for podcast creators"')
        print('  python run_brainstorm.py "automation for etsy sellers"')
        print('  python run_brainstorm.py "developer productivity tools"')
        sys.exit(1)

    niche = " ".join(sys.argv[1:])

    print(f"\n{'='*60}")
    print("AGENT TEAM BRAINSTORMING SESSION")
    print(f"{'='*60}")
    print(f"Niche: {niche}")
    print(f"{'='*60}\n")

    prompt = create_session_prompt(niche)

    # Print the prompt for use with Claude or other LLMs
    print(prompt)

    print(f"\n{'='*60}")
    print("Copy the above prompt to use with Claude or your preferred LLM.")
    print("Save the output to the 'sessions/' directory for future reference.")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
