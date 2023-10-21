from pathlib import Path
from collections import defaultdict
from tqdm import tqdm
from time import sleep


def to_megabytes(in_bytes: int):
    return in_bytes / 10**6


def compile_sizes(path: Path):
    sum_sizes = []
    for file in path.rglob("*"):
        stat = file.stat()
        size = stat.st_size
        sum_sizes.append(size)
    return to_megabytes(sum(sum_sizes))


def sort_result(result: dict):
    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def crawl_dir(parent: str):
    current_dir = Path(parent)
    path_size = defaultdict(int)
    for path in tqdm(current_dir.iterdir()):
        strpath = str(path)
        if path.is_dir():
            path_size[strpath] = compile_sizes(path)
        else:
            stat = path.stat()
            size = stat.st_size
            path_size[strpath] = to_megabytes(size)
    sort_by_size = sort_result(path_size)
    return sort_by_size


def main(parent: str):
    sort_by_size = crawl_dir(parent)
    for idx, result in enumerate(sort_by_size):
        if idx > len(sort_by_size) / 4:
            break
        path, size = result
        print(f"{path}: {size:.0f} MB")


if __name__ == "__main__":
    while True:
        try:
            parent = input("Path: ")
            main(parent)
        except OSError as oserr:
            print(oserr)
            continue
        except KeyboardInterrupt:
            print("\nexiting...")
            sleep(0.5)
            break
    exit(0)
