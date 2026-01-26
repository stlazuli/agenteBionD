import re
from typing import List, Set
from config import CATEGORIES


def normalize_text(text: str) -> str:
    return text.lower().strip()


def classify_message(message: str) -> List[str]:
    matched_categories: Set[str] = {"always"}
    normalized_message = normalize_text(message)

    for category_name, category_config in CATEGORIES.items():
        if category_name == "always":
            continue

        keywords = category_config.get("keywords", [])

        for keyword in keywords:
            normalized_keyword = normalize_text(keyword)
            if len(normalized_keyword) <= 3:
                pattern = rf'\b{re.escape(normalized_keyword)}\b'
                if re.search(pattern, normalized_message):
                    matched_categories.add(category_name)
                    break
            else:
                if normalized_keyword in normalized_message:
                    matched_categories.add(category_name)
                    break

    return list(matched_categories)


def get_categories_summary(categories: List[str]) -> str:
    if len(categories) == 1 and "always" in categories:
        return "Base instructions only"

    specific = [c for c in categories if c != "always"]
    return f"Base + {', '.join(specific)}"
