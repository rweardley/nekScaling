#!/bin/bash

# Set up arrays for specifying the cases to set up.
# These should all have the same number of entries,
# as they will all be stepped through synchronously
# and a case will be set up for each entry

nodes_arr=(
    1
    1
    1
    1
    1
    1
    1
    1
    1
    2
)
ranks_per_node_arr=(
    8
    12
    16
    24
    32
    40
    48
    56
    64
    64
)
walltime_arr=(
    "00:45:00"
    "00:45:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
    "00:30:00"
)
array_spec_arr=(
    "1-9:1"
    "1-9:1"
    "1-9:1"
    "3-9:1"
    "3-9:1"
    "3-9:1"
    "3-9:1"
    "5-9:1"
    "5-9:1"
    "5-9:1"
)

#
base_script="submit_array.mi300x"

for i in range(len(nodes_arr))
    ranks_per_node = ranks_per_node[i]
    nodes = nodes[i]
    walltime = walltime_arr[i]
    array_spec = array_spec_arr[i]

    ranks_tot=$((ranks_per_node*nodes))
    case_dir=${ranks_tot}_ranks
    case_script=$case_dir/submit_array.mi300x
    mkdir $case_dir
    cp $base_script $case_script

    sed -i "s/J NRS_MI300X_CPX_8/J NRS_MI300X_CPX_${ranks_tot}/" $case_script
    sed -i "s/nodes=1/nodes=${nodes}/" $case_script
    sed -i "s/time=00:45:00/time=${walltime}/" $case_script
    sed -i "s/array=1-9:1/array=${array_spec}/" $case_script
    if nodes==1:
        sed -i "s/nrsmpi laminarPipe 8/nrsmpi laminarPipe ${ranks_per_node}/" $case_script
    else:
        sed -i "s/nrsmpi laminarPipe 8/mpirun -np ${ranks_tot} -ppn ${ranks_per_node} nekrs --setup laminarPipe.par/" $case_script
