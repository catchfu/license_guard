#!/usr/bin/env python3
"""
LicenseGuard Team Session Runner

Orchestrates the agent team to work through project phases.
"""

import sys
from datetime import datetime
from pathlib import Path

from agents import TEAM

# Phase definitions with agent tasks
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


def generate_phase_prompt(phase_key: str) -> str:
    """Generate a prompt for running a specific phase."""
    phase = PHASES[phase_key]

    output = [
        f"# LicenseGuard: {phase['name']}",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Objective:** {phase['description']}",
        "",
        "---",
        ""
    ]

    for i, (agent_key, task) in enumerate(phase["tasks"], 1):
        agent = TEAM[agent_key]
        output.extend([
            f"## Task {i}: {task}",
            f"**Agent:** {agent['name']} ({', '.join(agent['roles'])})",
            "",
            "### Agent Instructions:",
            agent["prompt"],
            "",
            f"### Your Task:",
            task,
            "",
            "---",
            ""
        ])

    output.extend([
        "## Phase Summary",
        "",
        "After completing all tasks, provide:",
        "1. Key decisions made",
        "2. Artifacts produced",
        "3. Open questions for next phase",
        "4. Risks identified",
        ""
    ])

    return "\n".join(output)


def generate_full_session() -> str:
    """Generate a complete session across all phases."""
    output = [
        "# LicenseGuard: Full Build Session",
        f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Team",
        ""
    ]

    for key, agent in TEAM.items():
        output.append(f"- **{agent['name']}**: {', '.join(agent['roles'])}")

    output.extend(["", "---", ""])

    for phase_key in ["discovery", "design", "build", "launch"]:
        phase = PHASES[phase_key]
        output.extend([
            f"# {phase['name'].upper()}",
            f"*{phase['description']}*",
            ""
        ])

        for i, (agent_key, task) in enumerate(phase["tasks"], 1):
            agent = TEAM[agent_key]
            output.extend([
                f"## [{agent['name']}] {task}",
                "",
                "[Complete this task following agent instructions]",
                "",
            ])

        output.extend(["---", ""])

    return "\n".join(output)


def main():
    phases = list(PHASES.keys()) + ["full"]

    if len(sys.argv) < 2 or sys.argv[1] not in phases:
        print("Usage: python run_licenseguard_team.py <phase>")
        print(f"\nAvailable phases: {', '.join(phases)}")
        print("\nPhase descriptions:")
        for key, phase in PHASES.items():
            print(f"  {key}: {phase['description']}")
        print(f"  full: Run all phases sequentially")
        sys.exit(1)

    phase = sys.argv[1]

    print(f"\n{'='*60}")
    print(f"LICENSEGUARD TEAM SESSION: {phase.upper()}")
    print(f"{'='*60}\n")

    if phase == "full":
        prompt = generate_full_session()
    else:
        prompt = generate_phase_prompt(phase)

    print(prompt)

    # Save to file
    sessions_dir = Path(__file__).parent / "sessions"
    sessions_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = sessions_dir / f"{timestamp}_{phase}.md"
    filepath.write_text(prompt, encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"Session saved to: {filepath}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
