#!/usr/bin/env python3
""" logic to interact with phoronix-test-suite """

import json
from subprocess import call


# basic JSON write
def write_prefs():
    with open('filename.json', 'w') as f:
        json.dumps(data, f)


# basic JSON read
def load_prefs():
    with open('filename.json', 'r') as r:
        data_struct = json.loads(f)


# find loops
def get_loops():
    for x in data_struct["loops"]:
        loops = x


# write the command for PTS to start running
def run_bash():
    call(["TOTAL_LOOP_TIME = ", loops, "PTS_CONCURRENT_TEST_RUNS = ", runs,
          "phoronix-test-suite stress-run ", test_suite])
