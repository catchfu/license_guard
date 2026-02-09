#!/usr/bin/env python3
"""
Run brainstorming session using Anthropic Claude API.

Requires: pip install anthropic
Set environment variable: ANTHROPIC_API_KEY
"""

import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Please install anthropic: pip install anthropic")
    sys.exit(1)

from agents.idea_generator import SYSTEM_PROMPT as IDEA_PROMPT
from agents.market_analyst import SYSTEM_PROMPT as MARKET_PROMPT
from agents.tech_architect import SYSTEM_PROMPT as TECH_PROMPT
from agents.devils_advocate import SYSTEM_PROMPT as DEVIL_PROMPT


class BrainstormSession:
    """Orchestrates multi-agent brainstorming with Claude."""

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.model = "claude-sonnet-4-5-20250929"  # Fast and capable
        self.conversation = []

    def _call_agent(self, agent_name: str, system_prompt: str, user_message: str) -> str:
        """Call an agent and get response."""
        print(f"\n{'='*50}")
        print(f"[{agent_name}] Thinking...")
        print(f"{'='*50}")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}]
        )

        result = response.content[0].text
        print(result[:500] + "..." if len(result) > 500 else result)

        return result

    def run(self, niche: str) -> str:
        """Run full brainstorming session."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        output = [
            f"# Brainstorming Session: {niche}",
            f"**Date:** {timestamp}",
            "",
            "---",
            ""
        ]

        # Phase 1: Idea Generation
        ideas = self._call_agent(
            "IDEA GENERATOR",
            IDEA_PROMPT,
            f"Generate 5-7 tool ideas for passive income in this niche: {niche}"
        )
        output.extend(["## Phase 1: Generated Ideas", "", ideas, "", "---", ""])

        # Phase 2: Market Analysis
        market = self._call_agent(
            "MARKET ANALYST",
            MARKET_PROMPT,
            f"Analyze the market potential for these ideas:\n\n{ideas}"
        )
        output.extend(["## Phase 2: Market Analysis", "", market, "", "---", ""])

        # Phase 3: Technical Assessment
        tech = self._call_agent(
            "TECH ARCHITECT",
            TECH_PROMPT,
            f"Assess technical feasibility for these ideas:\n\n{ideas}"
        )
        output.extend(["## Phase 3: Technical Assessment", "", tech, "", "---", ""])

        # Phase 4: Devil's Advocate
        challenge = self._call_agent(
            "DEVIL'S ADVOCATE",
            DEVIL_PROMPT,
            f"""Challenge these ideas:

IDEAS:
{ideas}

MARKET ANALYSIS:
{market}

TECHNICAL ASSESSMENT:
{tech}

Be critical and identify weaknesses."""
        )
        output.extend(["## Phase 4: Critical Review", "", challenge, "", "---", ""])

        # Phase 5: Synthesis
        synthesis = self._call_agent(
            "SYNTHESIS",
            "You are synthesizing a multi-perspective brainstorming session. Provide actionable recommendations.",
            f"""Based on all perspectives, provide final recommendations:

IDEAS GENERATED:
{ideas}

MARKET ANALYSIS:
{market}

TECHNICAL ASSESSMENT:
{tech}

CRITICAL REVIEW:
{challenge}

Provide:
1. Top 3 ideas ranked with reasoning
2. Immediate next steps for #1 idea
3. Ideas to shelve and why"""
        )
        output.extend(["## Phase 5: Final Recommendations", "", synthesis])

        return "\n".join(output)

    def save(self, niche: str, content: str) -> Path:
        """Save session to file."""
        sessions_dir = Path(__file__).parent / "sessions"
        sessions_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_niche = "".join(c if c.isalnum() else "_" for c in niche)[:30]
        filepath = sessions_dir / f"{timestamp}_{safe_niche}.md"

        filepath.write_text(content, encoding="utf-8")
        return filepath


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_with_claude.py \"<niche or problem area>\"")
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    niche = " ".join(sys.argv[1:])

    print(f"\n{'#'*60}")
    print(f"# AGENT TEAM BRAINSTORMING: {niche}")
    print(f"{'#'*60}")

    session = BrainstormSession()
    result = session.run(niche)

    filepath = session.save(niche, result)

    print(f"\n{'='*60}")
    print(f"Session saved to: {filepath}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
