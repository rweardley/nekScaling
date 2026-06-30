#!/bin/bash

# ------------------------------------------------------------------
# Case specifications
# ------------------------------------------------------------------

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

base_script="submit_array.mi300x"

# ------------------------------------------------------------------
# Check array lengths match
# ------------------------------------------------------------------

n_cases=${#nodes_arr[@]}

if [[ ${#ranks_per_node_arr[@]} -ne $n_cases ]] || \
   [[ ${#walltime_arr[@]} -ne $n_cases ]] || \
   [[ ${#array_spec_arr[@]} -ne $n_cases ]]; then
    echo "Error: input arrays have different lengths."
    exit 1
fi

# ------------------------------------------------------------------
# Generate cases
# ------------------------------------------------------------------

for ((i=0; i<n_cases; i++)); do

    ranks_per_node=${ranks_per_node_arr[i]}
    nodes=${nodes_arr[i]}
    walltime=${walltime_arr[i]}
    array_spec=${array_spec_arr[i]}

    ranks_tot=$((ranks_per_node * nodes))

    case_dir="${ranks_tot}_ranks"
    case_script="${case_dir}/submit_array.mi300x"

    mkdir -p "${case_dir}"
    cp "${base_script}" "${case_script}"

    sed -i "s/J NRS_MI300X_CPX_8/J NRS_MI300X_CPX_${ranks_tot}/" "${case_script}"
    sed -i "s/nodes=1/nodes=${nodes}/" "${case_script}"
    sed -i "s/time=00:45:00/time=${walltime}/" "${case_script}"
    sed -i "s/array=1-9:1/array=${array_spec}/" "${case_script}"

    if [[ ${nodes} -eq 1 ]]; then
        sed -i \
            "s/nrsmpi laminarPipe 8/nrsmpi laminarPipe ${ranks_per_node}/" \
            "${case_script}"
    else
        sed -i \
            "s/nrsmpi laminarPipe 8/mpirun -np ${ranks_tot} -ppn ${ranks_per_node} nekrs --setup laminarPipe.par/" \
            "${case_script}"
    fi

    echo "Created ${case_script}"

done