#!/usr/bin/env python3

import random

def keygen():
	return hex(random.getrandbits(random.randint(100, 300)))[2:]

