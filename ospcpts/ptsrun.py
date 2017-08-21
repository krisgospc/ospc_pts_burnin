#!/usr/bin/env python3
""" logic to interact with phoronix-test-suite """

import json

#basic JSON write
with open('filename.json', 'w') as f:
    json.dump(data, f)

#basic JSON read
with open('filename.json', 'r') as r:
    data_struct = json.load(f)
