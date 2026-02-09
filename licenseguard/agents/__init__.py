"""LicenseGuard Agent Team"""

from .product_lead import SYSTEM_PROMPT as PRODUCT_LEAD_PROMPT
from .ux_content_lead import SYSTEM_PROMPT as UX_CONTENT_LEAD_PROMPT
from .engineering_lead import SYSTEM_PROMPT as ENGINEERING_LEAD_PROMPT
from .qa_engineer import SYSTEM_PROMPT as QA_ENGINEER_PROMPT
from .growth_lead import SYSTEM_PROMPT as GROWTH_LEAD_PROMPT

TEAM = {
    "product_lead": {
        "name": "Product Lead",
        "roles": ["PM", "BA"],
        "prompt": PRODUCT_LEAD_PROMPT
    },
    "ux_content_lead": {
        "name": "UX & Content Lead",
        "roles": ["UX Design", "Tech Writer"],
        "prompt": UX_CONTENT_LEAD_PROMPT
    },
    "engineering_lead": {
        "name": "Engineering Lead",
        "roles": ["Developer", "Tech Architect"],
        "prompt": ENGINEERING_LEAD_PROMPT
    },
    "qa_engineer": {
        "name": "QA Engineer",
        "roles": ["QA"],
        "prompt": QA_ENGINEER_PROMPT
    },
    "growth_lead": {
        "name": "Growth Lead",
        "roles": ["Marketing", "Sales"],
        "prompt": GROWTH_LEAD_PROMPT
    }
}

__all__ = [
    "TEAM",
    "PRODUCT_LEAD_PROMPT",
    "UX_CONTENT_LEAD_PROMPT",
    "ENGINEERING_LEAD_PROMPT",
    "QA_ENGINEER_PROMPT",
    "GROWTH_LEAD_PROMPT",
]
