#!/bin/bash

# ------------------------------------------------------------------
# Case specifications
# ------------------------------------------------------------------

jobname_prefix=NRS_MI300X_QPX
total_ranks_per_node=32
account=UKAEA-AP002-GPU
partition=ukaea-mi300x-32
profile=../case_profile

nodes_arr=(
    1
    1
    1
    1
    1
    2
)

ranks_per_node_arr=(
    4
    8
    16
    24
    32
    32
)

walltime_arr=(
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
    "3-9:1"
    "3-9:1"
    "5-9:1"
    "5-9:1"
)

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

    echo "#!/bin/bash" > ${case_script}
    echo "" >> ${case_script}
    echo "#SBATCH -J ${jobname_prefix}_${ranks_tot}" >> ${case_script}
    echo "#SBATCH -A ${account}" >> ${case_script}
    echo "#SBATCH --nodes=${nodes}" >> ${case_script}
    echo "#SBATCH --gres=gpu:${total_ranks_per_node}" >> ${case_script}
    echo "#SBATCH --time=${walltime}" >> ${case_script}
    echo "#SBATCH -p ${partition}" >> ${case_script}
    echo "#SBATCH --array=${array_spec}" >> ${case_script}
    echo "#SBATCH --exclusive" >> ${case_script}
    echo "" >> ${case_script}
    echo "jobdir=\"N_\${SLURM_ARRAY_TASK_ID}\"" >> ${case_script}
    echo "source ${profile}" >> ${case_script}
    echo "cp -r \$BASE_CASE \$jobdir" >> ${case_script}
    echo "cd \$jobdir" >> ${case_script}
    echo "sed -i \"s/polynomialOrder = 1/polynomialOrder = \${SLURM_ARRAY_TASK_ID}/\" laminarPipe.par" >> ${case_script}

    if [[ ${nodes} -eq 1 ]]; then
        echo "nrsmpi \${CASE_NAME} ${ranks_per_node} 2>&1 | tee log.run" >> ${case_script}
    else
        echo "mpirun -np ${ranks_tot} -ppn ${ranks_per_node} nekrs --setup \${CASE_NAME}.par 2>&1 | tee log.run" >> ${case_script}
    fi

    echo "\${NEK_SCALING_UTILS}/log2tsv.sh log.run" >> ${case_script}
    echo "mv summary.tsv ../N_\${SLURM_ARRAY_TASK_ID}.tsv" >> ${case_script}

    echo "Created ${case_script}"

done