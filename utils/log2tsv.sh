#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

log_file="$1"
output_file="summary.tsv"

awk '
BEGIN {
    OFS="\t"

    print "Timestep","CFL","t","dt","ElapsedStep", \
          "P_iter","UVW_iter","PB_iter","Bxyz_iter","PHI_iter","T_iter"
}

#
# Old-format full-induction solves
#
/^[[:space:]]*P[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        p_iter=a[1]
}

/^[[:space:]]*UVW[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        uvw_iter=a[1]
}

/^[[:space:]]*PB[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        pb_iter=a[1]
}

/^[[:space:]]*Bxyz[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        bxyz_iter=a[1]
}

#
# New-format inductionless solves
#
/FLUID p[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        p_iter=a[1]
}

/FLUID U[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        uvw_iter=a[1]
}

/MHD PHI[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        phi_iter=a[1]
}

/SCALAR temperature[[:space:]]*:[[:space:]]*iter/ {
    if (match($0,/iter[[:space:]]+([0-9]+)/,a))
        t_iter=a[1]
}

#
# Old-format timestep summary
#
/step=.*t=.*dt=.*elapsedStep=/ {

    timestep=""
    t=""
    dt=""
    cfl=""
    elapsed=""

    if (match($0,/step=[[:space:]]*([0-9]+)/,a))
        timestep=a[1]

    if (match($0,/t=[[:space:]]*([^[:space:]]+)/,a))
        t=a[1]

    if (match($0,/dt=[[:space:]]*([^[:space:]]+)/,a))
        dt=a[1]

    if (match($0,/C=[[:space:]]*([^[:space:]]+)/,a))
        cfl=a[1]

    if (match($0,/elapsedStep=[[:space:]]*([^s[:space:]]+)/,a))
        elapsed=a[1]

    print timestep,cfl,t,dt,elapsed,\
          p_iter,uvw_iter,pb_iter,bxyz_iter,phi_iter,t_iter

    next
}

#
# New-format time line
#
/step=.*t=.*dt=.*CFL=/ {

    if (match($0,/step=[[:space:]]*([0-9]+)/,a))
        timestep=a[1]

    if (match($0,/t=[[:space:]]*([^[:space:]]+)/,a))
        t=a[1]

    if (match($0,/dt=[[:space:]]*([^[:space:]]+)/,a))
        dt=a[1]

    if (match($0,/CFL=[[:space:]]*([^[:space:]]+)/,a))
        cfl=a[1]

    next
}

#
# New-format elapsed line
#
/step=.*elapsedStep=.*elapsedStepSum=/ {

    if (match($0,/elapsedStep=[[:space:]]*([^s[:space:]]+)/,a))
        elapsed=a[1]

    print timestep,cfl,t,dt,elapsed,\
          p_iter,uvw_iter,pb_iter,bxyz_iter,phi_iter,t_iter
}
' "$log_file" > "$output_file"

echo "Data has been extracted to $output_file"
