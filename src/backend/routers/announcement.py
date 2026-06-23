"""
Endpoint for serving announcement banner configuration
"""

from fastapi import APIRouter
from typing import Any, Dict, Optional

from ..database import config_collection

router = APIRouter(
    prefix="/announcement",
    tags=["announcement"]
)


@router.get("", response_model=Dict[str, Any])
def get_announcement() -> Dict[str, Any]:
    """
    Get the current announcement banner message and deadline date.

    Returns a dict with:
    - message: the announcement text
    - deadline: ISO 8601 date string (YYYY-MM-DD) for the registration deadline, or null
    """
    doc = config_collection.find_one({"_id": "announcement"})
    if not doc:
        return {"message": "", "deadline": None}
    return {"message": doc.get("message", ""), "deadline": doc.get("deadline")}
