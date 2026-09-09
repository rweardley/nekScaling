ranks_list=(1 2 4 6 8 16)
remote=login-dawn.hpc.cam.ac.uk
remote_general=/home/ir-eard1/rds/rds-ukaea-ap002-mOlK9qn0PlQ/ir-eard1/NekRS/user_problems
remote_dir=$remote_general/nekScaling/hpc_runs/zenith_mi355x/laminarPipe/SPX

echo "Enter run name:"
read runname

if [[ -n $runname ]]; then
  dir="${runname}/"
else
  dir=""
fi

for ranks in ${ranks_list[@]}
do
  mkdir ${ranks}_ranks
  if [[ -n $runname ]]; then mkdir ${ranks}_ranks/${dir}; fi
  scp $remote:$remote_dir/${ranks}_ranks/${dir}*.tsv ${ranks}_ranks/${dir}
done