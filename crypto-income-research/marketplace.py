"""ACP-style service draft: offline only. No ACP API, wallet or network calls."""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class ResearchOffer:
    name: str = "BTC/ETH Market Research"
    description: str = "Educational, timestamped market research. No personalized investment advice."
    currency: str = "USD"
    proposed_price: float = 5.0
    publication_status: str = "DRAFT_NOT_PUBLISHED"

def draft_offer() -> dict:
    return asdict(ResearchOffer())

def generate_research_report(symbol: str, closes: list[float], as_of: str) -> dict:
    if symbol not in ("BTC", "ETH"):
        raise ValueError("Only BTC and ETH research supported")
    if len(closes) < 2 or any(p <= 0 for p in closes):
        raise ValueError("Provide two or more positive prices")
    change = (closes[-1] / closes[0] - 1) * 100
    return {"type": "educational_market_research", "symbol": symbol,
            "as_of": as_of, "data_source": "user_supplied_demo",
            "first_close": closes[0], "last_close": closes[-1],
            "change_pct": round(change, 2),
            "disclaimer": "Not a price forecast or investment recommendation."}

if __name__ == "__main__":
    print(json.dumps(draft_offer(), indent=2))
