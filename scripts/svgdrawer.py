#!/usr/bin/env python

import csv
from pathlib import Path
import re
from sys import stderr
import svgwrite

SRC_GRID_PATH = Path('data', 'stategrid.csv')
DEST_PATH = Path('svg', 'stategrid.svg')

PX = 50
PY = 15

STROKE_COLOR = (0, 0, 0, '%')


def main():
    DEST_PATH.parent.mkdir(exist_ok=True, parents=True)

    dwg = svgwrite.Drawing(str(DEST_PATH), size=(600, 400))

    dwg.add(dwg.rect(insert=(0,0), size=(600,400), fill='white',))

    for state in csv.DictReader(SRC_GRID_PATH.open()):
        x = int(state['col'])
        y = int(state['row'])
        bb = (
                [((x+0)*PX, (y+0)*PX), ((x+1)*PX, (y+0)*PX)],
                [((x+1)*PX, (y+0)*PX), ((x+1)*PX, (y+1)*PX)],
                [((x+1)*PX, (y+1)*PX), ((x+0)*PX, (y+1)*PX)],
                [((x+0)*PX, (y+1)*PX), ((x+0)*PX, (y+0)*PX)],
            )
        # draw 0,0 to 1,0
        dwg.add(dwg.line(bb[0][0], bb[1][0], stroke=svgwrite.rgb(*STROKE_COLOR)))
        # draw 1,0 to 1,1
        dwg.add(dwg.line(bb[1][0], bb[1][1], stroke=svgwrite.rgb(*STROKE_COLOR)))
        # draw 1,1 to 0,1
        dwg.add(dwg.line(bb[2][0], bb[2][1], stroke=svgwrite.rgb(*STROKE_COLOR)))
        # # draw 0,1 to 0,0
        dwg.add(dwg.line(bb[3][0], bb[3][1], stroke=svgwrite.rgb(*STROKE_COLOR)))

        ix = (bb[0][0][0]+PY, bb[0][0][1]+PY+PY)
        # print("ix:", ix)
        dwg.add(dwg.text(state['state'], insert=ix, fill='red'))


    dwg.save()


if __name__ == '__main__':
    main()
