#!/bin/bash

exo2nek << EOF 2>&1 | tee log.exo2nek
1
Ha_20_shercliff
0
0
channel
EOF

mv channel.re2 ..