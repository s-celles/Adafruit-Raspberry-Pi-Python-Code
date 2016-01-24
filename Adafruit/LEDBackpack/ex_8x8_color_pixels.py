#!/usr/bin/python

import time
import datetime
from Adafruit.LEDBackpack import ColorEightByEight

def main():
    # ===========================================================================
    # 8x8 Pixel Example
    # ===========================================================================
    grid = ColorEightByEight(address=0x70)

    print "Press CTRL+Z to exit"

    iter = 0

    # Continually update the 8x8 display one pixel at a time
    while(True):
      iter += 1

      for x in range(0, 8):
        for y in range(0, 8):
          grid.setPixel(x, y, iter % 4 )
          time.sleep(0.02)

if __name__ == '__main__':
    main()
