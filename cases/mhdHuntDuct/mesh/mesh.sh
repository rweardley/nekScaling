#!/bin/bash

exo2nek << EOF 2>&1 | tee log.exo2nek
1
Ha_20_hunt_II_fluid
1
Ha_20_hunt_II_solid
0
0
channel
EOF

mv channel.re2 ..