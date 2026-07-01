#!/bin/bash

exo2nek << EOF 2>&1 | tee log.exo2nek
1
pipe
0
1
1 2
pipe
EOF