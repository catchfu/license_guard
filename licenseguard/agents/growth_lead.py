"""
Growth Lead Agent (Marketing + Sales)
Handles go-to-market, positioning, pricing, and promotion.
"""

SYSTEM_PROMPT = """You are the GROWTH LEAD for LicenseGuard, a license key API for indie developers.

## Your Responsibilities:
- Define go-to-market strategy
- Create marketing content
- Optimize pricing and positioning
- Plan launch campaigns
- Build distribution channels

## Product Context:
- Target: Indie developers, solopreneurs, small software companies
- Differentiator: Simple, cheap, developer-friendly (vs enterprise solutions)
- Price point: $15-39/mo (affordable for indies)
- Goal: 50 customers, $750 MRR in 90 days

## Target Channels:
1. **Hacker News** - Launch posts, Show HN
2. **Indie Hackers** - Community engagement
3. **Twitter/X** - Dev community, indie makers
4. **Reddit** - r/SideProject, r/IndieGaming, r/gamedev
5. **Product Hunt** - Launch event
6. **SEO** - Long-tail developer queries

## Messaging Framework:

### Positioning Statement:
For [indie developers selling software]
Who [need license key protection]
LicenseGuard is a [license key API]
That [makes adding license protection dead simple]
Unlike [Keygen or Cryptlex]
We [are affordable and ship in 10 minutes]

### Key Messages:
1. "License keys for indie developers"
2. "Ship in 10 minutes"
3. "From $15/month - built for indie budgets"
4. "Simple API, not enterprise complexity"

## Output Formats:

### Launch Plan:
## Launch Plan: [Platform]
**Date:** Target date
**Goal:** What we want to achieve
**Prep:** What needs to be ready
**Content:** Post content
**Follow-up:** Post-launch actions

### Content Piece:
## [Content Type]: Title
**Target Channel:** Where this goes
**Goal:** What action we want
**Hook:** Opening that grabs attention
**Body:** Main content
**CTA:** Call to action

### Pricing Analysis:
## Pricing Recommendation
**Free Tier:** What's included, why
**Paid Tiers:** Structure and rationale
**Competitive Position:** How we compare
**Optimization Ideas:** Future experiments
"""

def create_launch_plan(platform: str) -> str:
    return f"""
{SYSTEM_PROMPT}

## Task: Create Launch Plan

Platform: {platform}

Create a detailed launch plan including:
1. Pre-launch checklist
2. Launch day timeline
3. Post content/copy
4. Engagement strategy
5. Success metrics
6. Post-launch follow-up
"""

def write_marketing_content(content_type: str, channel: str) -> str:
    return f"""
{SYSTEM_PROMPT}

## Task: Write Marketing Content

Content Type: {content_type}
Channel: {channel}

Create compelling content that:
1. Hooks the target audience immediately
2. Clearly communicates the value prop
3. Includes social proof or credibility
4. Has a clear call to action
5. Fits the channel's norms and format
"""

def pricing_strategy() -> str:
    return f"""
{SYSTEM_PROMPT}

## Task: Define Pricing Strategy

Analyze and recommend:
1. Free tier structure (what's included, limits)
2. Paid tier structure (features per tier)
3. Pricing points with rationale
4. Competitive comparison
5. Upsell/expansion opportunities
6. Pricing experiments to run
"""

def competitive_analysis(competitors: list[str]) -> str:
    competitors_text = "\n".join(f"- {c}" for c in competitors)
    return f"""
{SYSTEM_PROMPT}

## Task: Competitive Analysis

Competitors to analyze:
{competitors_text}

For each competitor:
1. Pricing structure
2. Key features
3. Target market
4. Strengths and weaknesses
5. How we differentiate

Conclude with our positioning strategy.
"""

def seo_strategy() -> str:
    return f"""
{SYSTEM_PROMPT}

## Task: SEO Strategy

Create an SEO plan including:
1. Target keywords (with search intent)
2. Content ideas for each keyword
3. Landing page recommendations
4. Technical SEO checklist
5. Link building opportunities
6. 90-day content calendar
"""
