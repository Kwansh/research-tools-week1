import argparse
import re
from collections import Counter
from pathlib import Path


def count_words(text: str) -> Counter[str]:
    words = re.findall(r"[A-Za-z0-9_]+|[\u3400-\u4dbf\u4e00-\u9fff]+", text.lower())
    return Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(description="统计文本中的词频")
    parser.add_argument("file", type=Path, help="要统计的文本文件路径")
    parser.add_argument(
        "-n", "--top", type=int, default=20, help="显示出现次数最多的词数（默认：20）"
    )
    args = parser.parse_args()

    if args.top < 1:
        parser.error("--top 必须是大于 0 的整数")
    if not args.file.is_file():
        parser.error(f"文件不存在：{args.file}")

    text = args.file.read_text(encoding="utf-8")
    frequencies = count_words(text)

    print(f"文件：{args.file}")
    print(f"词语总数：{sum(frequencies.values())}")
    print(f"不同词语数：{len(frequencies)}")
    print("\n词频排名：")
    for rank, (word, count) in enumerate(frequencies.most_common(args.top), start=1):
        print(f"{rank:>2}. {word}\t{count}")


if __name__ == "__main__":
    main()
