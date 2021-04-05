#!/usr/bin/env python

__author__ = "Ricardo de Azambuja"
__version__ = "0.0.1"
__license__ = "GPL"
__maintainer__ = "Ricardo de Azambuja"
__email__ = "ricardo.azambuja@gmail.com"
__status__ = "Development"

from os import statvfs
import subprocess
import random

def run(args):
    drive_info = statvfs(args.drivename)

    bs = drive_info.f_bsize

    n_blocks = drive_info.f_blocks
    max_blocks = int((n_blocks/(100/args.percent))/args.size)

    rnd_seed = int(random.random()*100000)

    try:
        for i in range(max_blocks):
            # Cheap way to avoid repeating (it depends on the pseudo-random generator...)
            random.seed(i+rnd_seed)
            curr_pos = int(random.random()*n_blocks)
            cmd = f"sudo dd if=/dev/urandom of={args.drivename} seek={curr_pos} count={args.size} bs={bs}"
            print(f"Writing block #{i+1} of {max_blocks}): {cmd}")
            if not args.test:
                proc = subprocess.Popen(cmd.split(" "))
                proc.wait()
    except KeyboardInterrupt:
        print("Stopped by the user!")
        proc.terminate()
        proc.wait(1)
        proc.kill()