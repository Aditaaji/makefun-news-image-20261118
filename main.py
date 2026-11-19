"""news-image-20261118: write one image summing up 18 November 2026's world news.

The program copies the bundled image (entry.png, 1024x1024, under 1 MiB)
to /output/entry.png. Deterministic, standard library only, no network:
both runs write the same bytes because the source file never changes.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copied entry.png has the wrong size")


if __name__ == "__main__":
    main()
