from pathlib import Path
from typing import List, Dict, Optional
from config import CATEGORIES, KNOWLEDGE_BASE_PATH


class InstructionLoader:
    def __init__(self, knowledge_path: Optional[Path] = None):
        self.knowledge_path = knowledge_path or KNOWLEDGE_BASE_PATH
        self._cache: Dict[str, str] = {}

    def _load_file(self, relative_path: str) -> str:
        if relative_path in self._cache:
            return self._cache[relative_path]

        file_path = self.knowledge_path / relative_path

        try:
            content = file_path.read_text(encoding="utf-8")
            self._cache[relative_path] = content
            return content
        except FileNotFoundError:
            print(f"Warning: File not found: {file_path}")
            return ""
        except Exception as e:
            print(f"Warning: Error reading {file_path}: {e}")
            return ""

    def load_category_instructions(self, category: str) -> str:
        if category not in CATEGORIES:
            print(f"Warning: Unknown category: {category}")
            return ""

        files = CATEGORIES[category].get("files", [])
        contents = []

        for file_path in files:
            content = self._load_file(file_path)
            if content:
                contents.append(content)

        return "\n\n---\n\n".join(contents)

    def load_instructions_for_categories(self, categories: List[str]) -> str:
        all_instructions = []

        if "always" in categories:
            always_content = self.load_category_instructions("always")
            if always_content:
                all_instructions.append("# Instruções Base\n\n" + always_content)

        for category in categories:
            if category == "always":
                continue

            content = self.load_category_instructions(category)
            if content:
                category_title = category.replace("_", " ").title()
                all_instructions.append(f"# Contexto: {category_title}\n\n" + content)

        return "\n\n" + "=" * 50 + "\n\n".join(all_instructions)

    def get_instructions_for_message(self, message: str) -> str:
        from classifier import classify_message

        categories = classify_message(message)
        return self.load_instructions_for_categories(categories)

    def clear_cache(self):
        self._cache.clear()


_loader: Optional[InstructionLoader] = None


def get_loader() -> InstructionLoader:
    global _loader
    if _loader is None:
        _loader = InstructionLoader()
    return _loader


def get_instructions(message: str) -> str:
    return get_loader().get_instructions_for_message(message)
