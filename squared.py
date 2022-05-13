from typing import Optional


def get_squared(num: int, limit: Optional[int] = None) -> Optional[int]:
    squared = num * num
    return squared if (not limit or squared <= limit) else None
