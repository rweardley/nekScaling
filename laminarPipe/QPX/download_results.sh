ranks_list=(4 8 16 24 32 64)

echo "Enter run name:"
read runname

if [[ -n $runname ]]; then
  dir="${runname}/"
else
  dir=""
fi

for ranks in ${ranks_list[@]}
do
  if [[ -n $runname ]]; then mkdir ${ranks}_ranks/${dir}; fi
  scp login-dawn.hpc.cam.ac.uk:/home/ir-eard1/rds/rds-ukaea-ap002-mOlK9qn0PlQ/ir-eard1/NekRS/MI300X/user_problems/laminarPipeScaling/QPX/${ranks}_ranks/${dir}*.tsv ${ranks}_ranks/${dir}
done