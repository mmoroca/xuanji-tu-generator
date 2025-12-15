# =========================
# Xuanji Tu (璇玑图) -by Su Hui- generator
# =========================

import random
import argparse
import asyncio

from pypinyin import lazy_pinyin, Style

# =========================
# GOOGLETRANS
# =========================

async def translate_googletrans_async(text, dest="es"):
    from googletrans import Translator
    translator = Translator()
    result = await translator.translate(text, src="zh-cn", dest=dest)
    return result.text

# =========================
# TEXT FILE LOAD
# =========================

def load_grid(filepath):
    with open(filepath, encoding="utf-8") as f:
        return [line.strip().split() for line in f if line.strip()]

# =========================
# POEM EXTRACTION
# =========================

def extract_random_poem(grid, min_len, max_len):
    size = len(grid)
    directions = [
        (0, 1), (0, -1),
        (1, 0), (-1, 0),
        (1, 1), (1, -1),
        (-1, 1), (-1, -1)
    ]

    for _ in range(1000):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        dx, dy = random.choice(directions)
        length = random.randint(min_len, max_len)

        poem = []
        cx, cy = x, y

        for _ in range(length):
            if 0 <= cx < size and 0 <= cy < size:
                poem.append(grid[cx][cy])
                cx += dx
                cy += dy
            else:
                break

        if len(poem) >= min_len:
            return poem

    raise RuntimeError("A valid poem could not be generated.")

# =========================
# PINYIN
# =========================

def to_pinyin(poem_chars, with_tone):
    style = Style.TONE3 if with_tone else Style.NORMAL
    return " ".join(lazy_pinyin(poem_chars, style=style))

# =========================
# MAIN
# =========================

def main():
    parser = argparse.ArgumentParser(
        description="Random generator of poems from Xuanji Tu"
    )

    parser.add_argument("--file", default="xuanji_tu.txt")
    parser.add_argument("--min-len", type=int, default=5)
    parser.add_argument("--max-len", type=int, default=20)

    parser.add_argument("--hanzi", action="store_true")
    parser.add_argument("--pinyin", action="store_true")
    parser.add_argument("--both", action="store_true")
    parser.add_argument("--tone", action="store_true")

    parser.add_argument(
        "--translate",
        choices=["googletrans"],
        help="Translation engine"
    )

    parser.add_argument(
        "--translation-only",
        action="store_true",
        help="Show only the translation"
    )

    args = parser.parse_args()

    grid = load_grid(args.file)
    poem = extract_random_poem(grid, args.min_len, args.max_len)

    hanzi = "".join(poem)
    pinyin = to_pinyin(poem, args.tone)

    # Traducción
    translation = None
    if args.translate == "googletrans":
        translation = asyncio.run(
            translate_googletrans_async(hanzi)
        )

    # Salida
    if args.translation_only:
        if translation:
            print(translation)
            print("\n[Experimental machine translation – googletrans]")
        else:
            print("No translation engine was requested")
        return

    if args.both:
        print(hanzi)
        print(pinyin)
    elif args.hanzi:
        print(hanzi)
    elif args.pinyin:
        print(pinyin)
    else:
        # por defecto
        print(hanzi)
        print(pinyin)

    if translation:
        print("\n" + translation)
        print("[Experimental machine translation – googletrans]")

if __name__ == "__main__":
    main()
