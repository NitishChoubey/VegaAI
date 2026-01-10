from pydantic import BaseModel
from typing import List, Optional

class VegaRequest(BaseModel):
    trip_id: str
    city: str
    country: str
    day: int
    time_slot: str
    total_budget: float
    remaining_budget: float
    preferences: Optional[List[str]] = []

class VegaSuggestion(BaseModel):
    title: str
    description: str
    reason: str

class VegaResponse(BaseModel):
    suggestions: List[VegaSuggestion]
