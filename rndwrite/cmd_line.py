#!/usr/bin/env python

import argparse
from rndwrite import *

def main():
    parser = argparse.ArgumentParser(description="Write random data to random positions")
    parser.add_argument("drivename", help="Name of the drive to be randomly destroyed (e.g. /dev/sdc). Use lsblk to confirm you are deleting the correct one...")
    parser.add_argument("--size", help="Number of blocks to write at once. Default 100", type=int, default=100)
    parser.add_argument("--percent", help="Percentage of the drive to be overriden. Default 30", type=int, default=30)
    parser.add_argument('--test', dest='feature', action='store_true')
    parser.set_defaults(test=False)

    args = parser.parse_args()
    run(args)