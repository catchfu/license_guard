#!/usr/bin/env python3
"""
LicenseGuard Team Session Runner for CI/CD

Runs agent team sessions using Claude API and saves output.
Designed for GitHub Actions but works locally too.
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

from agents import TEAM

# Phase definitions
PHASES = {
    "discovery": {
        "name": "Discovery Phase",
        "description": "Requirements gathering and competitive analysis",
        "tasks": [
            ("product_lead", "Define MVP user stories for: license generation, validation API, dashboard, developer SDKs"),
            ("growth_lead", "Competitive analysis of Keygen.sh, Cryptlex, and Gumroad licensing"),
            ("engineering_lead", "Technical feasibility assessment and architecture options"),
        ]
    },
    "design": {
        "name": "Design Phase",
        "description": "Architecture, UX, and API design",
        "tasks": [
            ("engineering_lead", "Design system architecture: API, database schema, infrastructure"),
            ("engineering_lead", "Design API endpoints for license CRUD and validation"),
            ("ux_content_lead", "Design dashboard wireframes: products, licenses, analytics"),
            ("ux_content_lead", "Write API documentation structure and quick start guide"),
            ("qa_engineer", "Create test strategy and security test plan"),
        ]
    },
    "build": {
        "name": "Build Phase",
        "description": "MVP implementation",
        "tasks": [
            ("engineering_lead", "Implement license key generation with cryptographic signing"),
            ("engineering_lead", "Implement validation API with rate limiting"),
            ("engineering_lead", "Build dashboard: auth, products, licenses views"),
            ("ux_content_lead", "Write complete API documentation"),
            ("qa_engineer", "Write and run automated tests"),
            ("qa_engineer", "Security audit of validation endpoint"),
        ]
    },
    "launch": {
        "name": "Launch Phase",
        "description": "Beta release and go-to-market",
        "tasks": [
            ("growth_lead", "Create Hacker News Show HN launch plan"),
            ("growth_lead", "Write Product Hunt launch content"),
            ("growth_lead", "Define SEO strategy and landing page copy"),
            ("ux_content_lead", "Finalize documentation and onboarding flow"),
            ("product_lead", "Define success metrics and feedback collection"),
        ]
    }
}


class AgentSession:
    """Runs multi-agent sessions with Claude."""

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.model = "claude-sonnet-4-5-20250929"

    def run_task(self, agent_key: str, task: str) -> str:
        """Run a single agent task."""
        agent = TEAM[agent_key]

        print(f"\n{'='*60}")
        print(f"[{agent['name']}] {task[:50]}...")
        print(f"{'='*60}")

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=agent["prompt"],
            messages=[{
                "role": "user",
                "content": f"Complete this task:\n\n{task}\n\nProvide detailed, actionable output."
            }]
        )

        result = response.content[0].text
        print(f"Completed ({len(result)} chars)")

        return result

    def run_phase(self, phase_key: str) -> str:
        """Run all tasks in a phase."""
        phase = PHASES[phase_key]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        output = [
            f"# LicenseGuard: {phase['name']}",
            f"**Date:** {timestamp}",
            f"**Objective:** {phase['description']}",
            "",
            "---",
            ""
        ]

        for i, (agent_key, task) in enumerate(phase["tasks"], 1):
            agent = TEAM[agent_key]

            result = self.run_task(agent_key, task)

            output.extend([
                f"## Task {i}: {task}",
                f"**Agent:** {agent['name']}",
                "",
                result,
                "",
                "---",
                ""
            ])

        # Phase summary
        summary = self.run_task("product_lead", f"""
Summarize the {phase['name']} outputs:
1. Key decisions made
2. Artifacts produced
3. Open questions for next phase
4. Risks identified
""")

        output.extend([
            "## Phase Summary",
            "",
            summary
        ])

        return "\n".join(output)

    def run_full(self) -> str:
        """Run all phases sequentially."""
        output = [
            "# LicenseGuard: Full Build Session",
            f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "---",
            ""
        ]

        for phase_key in ["discovery", "design", "build", "launch"]:
            phase_output = self.run_phase(phase_key)
            output.append(phase_output)
            output.append("\n---\n")

        return "\n".join(output)

    def save(self, phase: str, content: str) -> Path:
        """Save session output to file."""
        sessions_dir = Path(__file__).parent / "sessions"
        sessions_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = sessions_dir / f"{timestamp}_{phase}_ci.md"

        filepath.write_text(content, encoding="utf-8")
        return filepath


def main():
    phases = list(PHASES.keys()) + ["full"]

    if len(sys.argv) < 2 or sys.argv[1] not in phases:
        print(f"Usage: python run_with_claude_ci.py <phase>")
        print(f"Phases: {', '.join(phases)}")
        sys.exit(1)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    phase = sys.argv[1]

    print(f"\n{'#'*60}")
    print(f"# LICENSEGUARD AGENT SESSION: {phase.upper()}")
    print(f"{'#'*60}")

    session = AgentSession()

    if phase == "full":
        result = session.run_full()
    else:
        result = session.run_phase(phase)

    filepath = session.save(phase, result)

    print(f"\n{'='*60}")
    print(f"Session complete!")
    print(f"Output saved to: {filepath}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
