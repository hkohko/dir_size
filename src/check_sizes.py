from collections import defaultdict
from pathlib import Path
from time import sleep

from tqdm import tqdm

from custom_decor import to_megabytes


@to_megabytes
def compile_dir_size(path: Path):
    sum_sizes = []
    for file in path.rglob("*"):
        stat = file.stat()
        size = stat.st_size
        sum_sizes.append(size)
    return sum(sum_sizes)


@to_megabytes
def file_size(path: Path):
    stat = path.stat()
    size = stat.st_size
    return size


def sort_result(result: dict):
    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def crawl_dir(parent: str):
    current_dir = Path(parent)
    path_size = defaultdict(int)
    for path in tqdm(current_dir.iterdir()):
        strpath = str(path)
        if path.is_dir():
            path_size[strpath] = compile_dir_size(path)
        else:
            filesize = file_size(path)
            path_size[strpath] = filesize
    sort_by_size = sort_result(path_size)
    return sort_by_size


def to_display(parent: str):
    sort_by_size = crawl_dir(parent)
    for idx, result in enumerate(sort_by_size):
        if idx > len(sort_by_size) / 4:
            break
        path, size = result
        print(f"{path}: {size:.0f} MB")


def main():
    while True:
        try:
            entry_parent = input("Path: ")
            to_display(entry_parent)
        except OSError as oserr:
            print(oserr)
            continue
        except KeyboardInterrupt:
            print("\nexiting...")
            sleep(0.5)
            break
    exit(0)


if __name__ == "__main__":
    main()
