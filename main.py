"""Garden Paws Desktop — A local helper for Garden Paws farm folders, shop files, and animal photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='garden_paws_desktop',
        description='A local helper for Garden Paws farm folders, shop files, and animal photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Garden Paws Desktop')
    print('Keep the farm on disk before a shop update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
