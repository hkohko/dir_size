from pathlib import Path


def to_megabytes(fn):
    def wrapper(path: Path):
        in_bytes = fn(path)
        return in_bytes / 10**6

    return wrapper
