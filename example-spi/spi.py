#!/usr/bin/python3

import mraa as m
import random as rand

# intialise SPI
dev = m.Spi(0)

for x in range(0,100):
    txbuf = bytearray(4)
    for y in range(0,4):
        txbuf[y] = rand.randrange(0, 256)

    # send and receive data through SPI
    rxbuf = dev.write(txbuf)
    if rxbuf != txbuf:
        print("Data mismatch!")
        exit(1)
