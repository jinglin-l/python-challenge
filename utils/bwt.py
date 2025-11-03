#!/usr/bin/env python3

import sys

def burrows_wheeler_transform(text):
    rotations = generate_rotations(text)
    sorted_rotations = sorted(rotations)
    index = sorted_rotations.index(text)
    bwt_output = "".join(rotation[-1] for rotation in sorted_rotations)
    return bwt_output, index



def generate_rotations(text):
    output = []
    for i in range(len(text)):
        output.append(text[i:] + text[:i])
    return output


def main():
    try:
        text = sys.argv[1]
    except IndexError:
        print("Usage: bwt.py <text>", file=sys.stderr)
        return 1
    output = burrows_wheeler_transform(text)
    for line in output:
        print(line)
    return 0

if __name__ == "__main__":
    sys.exit(main())

