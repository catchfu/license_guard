"""Agent Team for Niche Market Tool Brainstorming"""

from .idea_generator import SYSTEM_PROMPT as IDEA_GENERATOR_PROMPT
from .market_analyst import SYSTEM_PROMPT as MARKET_ANALYST_PROMPT
from .tech_architect import SYSTEM_PROMPT as TECH_ARCHITECT_PROMPT
from .devils_advocate import SYSTEM_PROMPT as DEVILS_ADVOCATE_PROMPT

__all__ = [
    "IDEA_GENERATOR_PROMPT",
    "MARKET_ANALYST_PROMPT",
    "TECH_ARCHITECT_PROMPT",
    "DEVILS_ADVOCATE_PROMPT",
]
