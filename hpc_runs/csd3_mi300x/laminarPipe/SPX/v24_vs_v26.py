import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.lines import Line2D
import numpy as np
from pyscaling.scaling import StrongScalingCase
from pyscaling.scaling import WeakScalingCases

align_cpx_with_spx = (
    True  # limit number of points plotted so they cover the same range
)
# align_cpx_with_spx = False  # limit number of points plotted so they cover the same range

# savedir = "comparison_plots/comp1"
# SPX_casedir = "run1"
# CPX_casedir = "run3"

savedir = "v24_vs_v26"
v26_rootdir = ""
v26_casedir = ""
v24_rootdir = "old_runs/"
v24_casedir = "run3"
# v24_casedir = ""

timestep_range = slice(100, 2000)
lelg = 54000  # number of elements in .re2 mesh

N_values = range(1, 10)
colours = cm.tab10(np.linspace(0, 1, len(N_values)))

# N_values_to_plot = N_values
# suffix = ""

min_N = 8
max_N = 9
N_values_to_plot = range(min_N, max_N+1)
suffix = f"_N_{N_values_to_plot[0]}-{N_values_to_plot[-1]}"

# N_values_to_plot = [7]
# suffix = f"_N_{N_values_to_plot[0]}"

# if align_cpx_with_spx:
#     suffix += f"_aligned"

SPX_ranks_per_gpu = 1

v24_linestyle = "--"
v26_linestyle = "-"

# load v24 SPX results

v24_ranks_N1 = [1, 2]
v24_files_N1 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_1.tsv"
    for rank in v24_ranks_N1
]
v24_scaling_N1 = StrongScalingCase(
    v24_ranks_N1,
    SPX_ranks_per_gpu,
    v24_files_N1,
    lelg,
    1,
    timestep_range,
)
print("\nv24 SPX N=1")
v24_scaling_N1.scaling_calculations()

v24_ranks_N2 = [1, 2]
v24_files_N2 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_2.tsv"
    for rank in v24_ranks_N2
]
v24_scaling_N2 = StrongScalingCase(
    v24_ranks_N2,
    SPX_ranks_per_gpu,
    v24_files_N2,
    lelg,
    2,
    timestep_range,
)
print("\nv24 SPX N=2")
v24_scaling_N2.scaling_calculations()

v24_ranks_N3 = [1, 2, 4, 6]
v24_files_N3 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_3.tsv"
    for rank in v24_ranks_N3
]
v24_scaling_N3 = StrongScalingCase(
    v24_ranks_N3,
    SPX_ranks_per_gpu,
    v24_files_N3,
    lelg,
    3,
    timestep_range,
)
print("\nv24 SPX N=3")
v24_scaling_N3.scaling_calculations()

v24_ranks_N4 = [1, 2, 4, 6]
v24_files_N4 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_4.tsv"
    for rank in v24_ranks_N4
]
v24_scaling_N4 = StrongScalingCase(
    v24_ranks_N4,
    SPX_ranks_per_gpu,
    v24_files_N4,
    lelg,
    4,
    timestep_range,
)
print("\nv24 SPX N=4")
v24_scaling_N4.scaling_calculations()

v24_ranks_N5 = [1, 2, 4, 6, 8, 16]
v24_files_N5 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_5.tsv"
    for rank in v24_ranks_N5
]
v24_scaling_N5 = StrongScalingCase(
    v24_ranks_N5,
    SPX_ranks_per_gpu,
    v24_files_N5,
    lelg,
    5,
    timestep_range,
)
print("\nv24 SPX N=5")
v24_scaling_N5.scaling_calculations()

v24_ranks_N6 = [1, 2, 4, 6, 8, 16]
v24_files_N6 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_6.tsv"
    for rank in v24_ranks_N6
]
v24_scaling_N6 = StrongScalingCase(
    v24_ranks_N6,
    SPX_ranks_per_gpu,
    v24_files_N6,
    lelg,
    6,
    timestep_range,
)
print("\nv24 SPX N=6")
v24_scaling_N6.scaling_calculations()

v24_ranks_N7 = [1, 2, 4, 6, 8, 16]
v24_files_N7 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_7.tsv"
    for rank in v24_ranks_N7
]
v24_scaling_N7 = StrongScalingCase(
    v24_ranks_N7,
    SPX_ranks_per_gpu,
    v24_files_N7,
    lelg,
    7,
    timestep_range,
)
print("\nv24 SPX N=7")
v24_scaling_N7.scaling_calculations()

v24_ranks_N8 = [2, 4, 6, 8, 16]
v24_files_N8 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_8.tsv"
    for rank in v24_ranks_N8
]
v24_scaling_N8 = StrongScalingCase(
    v24_ranks_N8,
    SPX_ranks_per_gpu,
    v24_files_N8,
    lelg,
    8,
    timestep_range,
)
print("\nv24 SPX N=8")
v24_scaling_N8.scaling_calculations()

v24_ranks_N9 = [2, 4, 6, 8, 16]
v24_files_N9 = [
    v24_rootdir + str(rank) + "_ranks/" + v24_casedir + "/N_9.tsv"
    for rank in v24_ranks_N9
]
v24_scaling_N9 = StrongScalingCase(
    v24_ranks_N9,
    SPX_ranks_per_gpu,
    v24_files_N9,
    lelg,
    9,
    timestep_range,
)
print("\nv24 SPX N=9")
v24_scaling_N9.scaling_calculations()

v24_results = [
    v24_scaling_N1,
    v24_scaling_N2,
    v24_scaling_N3,
    v24_scaling_N4,
    v24_scaling_N5,
    v24_scaling_N6,
    v24_scaling_N7,
    v24_scaling_N8,
    v24_scaling_N9,
]


# load v26 SPX results

v26_ranks_N1 = [1, 2]
v26_files_N1 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_1.tsv"
    for rank in v26_ranks_N1
]
v26_scaling_N1 = StrongScalingCase(
    v26_ranks_N1,
    SPX_ranks_per_gpu,
    v26_files_N1,
    lelg,
    1,
    timestep_range,
)
print("\nv26 SPX N=1")
v26_scaling_N1.scaling_calculations()

v26_ranks_N2 = [1, 2]
v26_files_N2 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_2.tsv"
    for rank in v26_ranks_N2
]
v26_scaling_N2 = StrongScalingCase(
    v26_ranks_N2,
    SPX_ranks_per_gpu,
    v26_files_N2,
    lelg,
    2,
    timestep_range,
)
print("\nv26 SPX N=2")
v26_scaling_N2.scaling_calculations()

v26_ranks_N3 = [1, 2, 4, 6]
v26_files_N3 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_3.tsv"
    for rank in v26_ranks_N3
]
v26_scaling_N3 = StrongScalingCase(
    v26_ranks_N3,
    SPX_ranks_per_gpu,
    v26_files_N3,
    lelg,
    3,
    timestep_range,
)
print("\nv26 SPX N=3")
v26_scaling_N3.scaling_calculations()

v26_ranks_N4 = [1, 2, 4, 6]
v26_files_N4 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_4.tsv"
    for rank in v26_ranks_N4
]
v26_scaling_N4 = StrongScalingCase(
    v26_ranks_N4,
    SPX_ranks_per_gpu,
    v26_files_N4,
    lelg,
    4,
    timestep_range,
)
print("\nv26 SPX N=4")
v26_scaling_N4.scaling_calculations()

v26_ranks_N5 = [1, 2, 4, 6, 8, 16]
v26_files_N5 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_5.tsv"
    for rank in v26_ranks_N5
]
v26_scaling_N5 = StrongScalingCase(
    v26_ranks_N5,
    SPX_ranks_per_gpu,
    v26_files_N5,
    lelg,
    5,
    timestep_range,
)
print("\nv26 SPX N=5")
v26_scaling_N5.scaling_calculations()

v26_ranks_N6 = [1, 2, 4, 6, 8, 16]
v26_files_N6 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_6.tsv"
    for rank in v26_ranks_N6
]
v26_scaling_N6 = StrongScalingCase(
    v26_ranks_N6,
    SPX_ranks_per_gpu,
    v26_files_N6,
    lelg,
    6,
    timestep_range,
)
print("\nv26 SPX N=6")
v26_scaling_N6.scaling_calculations()

v26_ranks_N7 = [1, 2, 4, 6, 8, 16]
v26_files_N7 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_7.tsv"
    for rank in v26_ranks_N7
]
v26_scaling_N7 = StrongScalingCase(
    v26_ranks_N7,
    SPX_ranks_per_gpu,
    v26_files_N7,
    lelg,
    7,
    timestep_range,
)
print("\nv26 SPX N=7")
v26_scaling_N7.scaling_calculations()

v26_ranks_N8 = [1, 2, 4, 6, 8, 16]
v26_files_N8 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_8.tsv"
    for rank in v26_ranks_N8
]
v26_scaling_N8 = StrongScalingCase(
    v26_ranks_N8,
    SPX_ranks_per_gpu,
    v26_files_N8,
    lelg,
    8,
    timestep_range,
)
print("\nv26 SPX N=8")
v26_scaling_N8.scaling_calculations()

v26_ranks_N9 = [1, 2, 4, 6, 8, 16]
v26_files_N9 = [
    v26_rootdir + str(rank) + "_ranks/" + v26_casedir + "/N_9.tsv"
    for rank in v26_ranks_N9
]
v26_scaling_N9 = StrongScalingCase(
    v26_ranks_N9,
    SPX_ranks_per_gpu,
    v26_files_N9,
    lelg,
    9,
    timestep_range,
)
print("\nv26 SPX N=9")
v26_scaling_N9.scaling_calculations()

v26_results = [
    v26_scaling_N1,
    v26_scaling_N2,
    v26_scaling_N3,
    v26_scaling_N4,
    v26_scaling_N5,
    v26_scaling_N6,
    v26_scaling_N7,
    v26_scaling_N8,
    v26_scaling_N9,
]


# plots

# time-per-timestep

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            v24_results[i].qps_per_gpu,
            v24_results[i].time_per_timestep,
            marker="x",
            ls=v24_linestyle,
            color=colour,
            label=f"v24 SPX N={N}",
        )
        plt.plot(
            v26_results[i].qps_per_gpu,
            v26_results[i].time_per_timestep,
            marker="x",
            ls=v26_linestyle,
            color=colour,
            label=f"v26 SPX N={N}",
        )

# Legend for colors (N values)
legend_color_handles = [
    Line2D([0], [0], color=colours[i], lw=3, label=f"N={N}")
    for i, N in enumerate(N_values)
]
legend_color_handles = [
    h
    for h in legend_color_handles
    if int(h.get_label().split("=")[1]) in N_values_to_plot
]

# Legend for line styles (datasets)
legend_style_handles = [
    Line2D([0], [0], color="k", lw=2, linestyle=ls, label=f"{lbl}")
    for ls, lbl in zip(
        [v24_linestyle, v26_linestyle],
        ["v24 (SPX)", "v26 (SPX)"],
    )
]

# Add both legends
legend1 = plt.legend(
    handles=legend_color_handles,
    title="Polynomial Order",
    loc="lower left",
    ncol=2,
    frameon=False,
)
plt.legend(
    handles=legend_style_handles,
    title="GPU",
    bbox_to_anchor=(0.6, 1.0),
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.savefig(
    f"{savedir}/time_per_timestep_qps_gpu" + suffix + ".png",
    bbox_inches="tight",
)
plt.close()

# speedup

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            v24_results[i].qps_per_gpu,
            v24_results[i].speedup,
            marker="x",
            ls=v24_linestyle,
            color=colour,
            label=f"v24 SPX N={N}",
        )
        plt.plot(
            v26_results[i].qps_per_gpu,
            v26_results[i].speedup,
            marker="x",
            ls=v26_linestyle,
            color=colour,
            label=f"v26 SPX N={N}",
        )

# Legend for colors (N values)
legend_color_handles = [
    Line2D([0], [0], color=colours[i], lw=3, label=f"N={N}")
    for i, N in enumerate(N_values)
]
legend_color_handles = [
    h
    for h in legend_color_handles
    if int(h.get_label().split("=")[1]) in N_values_to_plot
]

# Legend for line styles (datasets)
legend_style_handles = [
    Line2D([0], [0], color="k", lw=2, linestyle=ls, label=f"{lbl}")
    for ls, lbl in zip(
        [v24_linestyle, v26_linestyle],
        ["v24 (SPX)", "v26 (SPX)"],
    )
]

# Add both legends
legend1 = plt.legend(
    handles=legend_color_handles,
    title="Polynomial Order",
    loc="upper left",
    ncol=2,
    frameon=False,
)
plt.legend(
    handles=legend_style_handles,
    title="GPU",
    bbox_to_anchor=(0.6, 1.0),
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.savefig(
    f"{savedir}/speedup_qps_gpu" + suffix + ".png", bbox_inches="tight"
)
plt.close()

# efficiency

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            v24_results[i].qps_per_gpu,
            v24_results[i].parallel_efficiency,
            marker="x",
            ls=v24_linestyle,
            color=colour,
            label=f"v24 SPX N={N}",
        )
        plt.plot(
            v26_results[i].qps_per_gpu,
            v26_results[i].parallel_efficiency,
            marker="x",
            ls=v26_linestyle,
            color=colour,
            label=f"v26 SPX N={N}",
        )

# Legend for colors (N values)
legend_color_handles = [
    Line2D([0], [0], color=colours[i], lw=3, label=f"N={N}")
    for i, N in enumerate(N_values)
]
legend_color_handles = [
    h
    for h in legend_color_handles
    if int(h.get_label().split("=")[1]) in N_values_to_plot
]

# Legend for line styles (datasets)
legend_style_handles = [
    Line2D([0], [0], color="k", lw=2, linestyle=ls, label=f"{lbl}")
    for ls, lbl in zip(
        [v24_linestyle, v26_linestyle],
        ["v24 (SPX)", "v26 (SPX)"],
    )
]

# Add both legends
legend1 = plt.legend(
    handles=legend_color_handles,
    title="Polynomial Order",
    loc="lower left",
    ncol=2,
    frameon=False,
)
plt.legend(
    handles=legend_style_handles,
    title="GPU",
    loc="lower center",
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.savefig(
    f"{savedir}/efficiency_qps_gpu" + suffix + ".png", bbox_inches="tight"
)
plt.close()
