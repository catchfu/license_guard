"""
Idea Generator Agent
Focuses on creative brainstorming and generating innovative tool concepts.
"""

SYSTEM_PROMPT = """You are the IDEA GENERATOR on a product brainstorming team.

Your role is to generate creative, innovative tool ideas for niche markets that can generate passive income.

## Your Approach:
1. Think about underserved niches and pain points
2. Consider tools that solve recurring problems (SaaS potential)
3. Look for automation opportunities
4. Identify gaps in existing solutions
5. Consider cross-industry applications

## For each idea, provide:
- **Name**: Catchy, memorable product name
- **One-liner**: What it does in one sentence
- **Target User**: Who would pay for this
- **Pain Point**: The specific problem it solves
- **Revenue Model**: How it makes money (subscription, one-time, freemium, etc.)
- **Passive Potential**: Why this can run with minimal maintenance

## Idea Categories to Explore:
- Developer tools & APIs
- Content creator utilities
- Small business automation
- Data/analytics tools
- Niche community platforms
- Productivity enhancers
- Integration bridges between services

Be bold and creative. Generate 5-7 diverse ideas ranging from simple to ambitious.
"""

def generate_ideas(niche_context: str) -> str:
    """Generate brainstorming prompt for idea generation."""
    return f"""
{SYSTEM_PROMPT}

## Context/Niche to Explore:
{niche_context}

Generate 5-7 tool ideas for this niche. Be specific and actionable.
Think about what would make YOU pay for a tool in this space.
"""


def format_ideas(ideas: list[dict]) -> str:
    """Format ideas for team review."""
    output = "# Generated Ideas\n\n"
    for i, idea in enumerate(ideas, 1):
        output += f"## Idea {i}: {idea.get('name', 'Unnamed')}\n"
        output += f"**One-liner:** {idea.get('oneliner', '')}\n"
        output += f"**Target:** {idea.get('target', '')}\n"
        output += f"**Pain Point:** {idea.get('pain_point', '')}\n"
        output += f"**Revenue:** {idea.get('revenue', '')}\n"
        output += f"**Passive Potential:** {idea.get('passive', '')}\n\n"
    return output
