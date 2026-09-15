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

savedir = "orig_vs_hRefine"
hRefine2_rootdir = ""
hRefine2_casedir = ""
unrefined_rootdir = "../SPX/"
unrefined_casedir = ""

timestep_range = slice(100, 2000)
lelg_unrefined = 54000  # number of elements in .re2 mesh
lelg_hRefine2 = 432000  # number of elements in .re2 mesh

N_values = range(1, 10)
colours = cm.tab10(np.linspace(0, 1, len(N_values)))

N_values_to_plot = N_values
suffix = ""

# min_N = 8
# max_N = 9
# N_values_to_plot = range(min_N, max_N+1)
# suffix = f"_N_{N_values_to_plot[0]}-{N_values_to_plot[-1]}"

# N_values_to_plot = [7]
# suffix = f"_N_{N_values_to_plot[0]}"

# if align_cpx_with_spx:
#     suffix += f"_aligned"

SPX_ranks_per_gpu = 1

unrefined_linestyle = "--"
hRefine2_linestyle = "-"

# load unrefined SPX results

unrefined_ranks_N1 = [1, 2]
unrefined_files_N1 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_1.tsv"
    for rank in unrefined_ranks_N1
]
unrefined_scaling_N1 = StrongScalingCase(
    unrefined_ranks_N1,
    SPX_ranks_per_gpu,
    unrefined_files_N1,
    lelg_unrefined,
    1,
    timestep_range,
)
print("\nunrefined SPX N=1")
unrefined_scaling_N1.scaling_calculations()

unrefined_ranks_N2 = [1, 2]
unrefined_files_N2 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_2.tsv"
    for rank in unrefined_ranks_N2
]
unrefined_scaling_N2 = StrongScalingCase(
    unrefined_ranks_N2,
    SPX_ranks_per_gpu,
    unrefined_files_N2,
    lelg_unrefined,
    2,
    timestep_range,
)
print("\nunrefined SPX N=2")
unrefined_scaling_N2.scaling_calculations()

unrefined_ranks_N3 = [1, 2, 4, 6]
unrefined_files_N3 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_3.tsv"
    for rank in unrefined_ranks_N3
]
unrefined_scaling_N3 = StrongScalingCase(
    unrefined_ranks_N3,
    SPX_ranks_per_gpu,
    unrefined_files_N3,
    lelg_unrefined,
    3,
    timestep_range,
)
print("\nunrefined SPX N=3")
unrefined_scaling_N3.scaling_calculations()

unrefined_ranks_N4 = [1, 2, 4, 6]
unrefined_files_N4 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_4.tsv"
    for rank in unrefined_ranks_N4
]
unrefined_scaling_N4 = StrongScalingCase(
    unrefined_ranks_N4,
    SPX_ranks_per_gpu,
    unrefined_files_N4,
    lelg_unrefined,
    4,
    timestep_range,
)
print("\nunrefined SPX N=4")
unrefined_scaling_N4.scaling_calculations()

unrefined_ranks_N5 = [1, 2, 4, 6, 8, 16]
unrefined_files_N5 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_5.tsv"
    for rank in unrefined_ranks_N5
]
unrefined_scaling_N5 = StrongScalingCase(
    unrefined_ranks_N5,
    SPX_ranks_per_gpu,
    unrefined_files_N5,
    lelg_unrefined,
    5,
    timestep_range,
)
print("\nunrefined SPX N=5")
unrefined_scaling_N5.scaling_calculations()

unrefined_ranks_N6 = [1, 2, 4, 6, 8, 16]
unrefined_files_N6 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_6.tsv"
    for rank in unrefined_ranks_N6
]
unrefined_scaling_N6 = StrongScalingCase(
    unrefined_ranks_N6,
    SPX_ranks_per_gpu,
    unrefined_files_N6,
    lelg_unrefined,
    6,
    timestep_range,
)
print("\nunrefined SPX N=6")
unrefined_scaling_N6.scaling_calculations()

unrefined_ranks_N7 = [1, 2, 4, 6, 8, 16]
unrefined_files_N7 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_7.tsv"
    for rank in unrefined_ranks_N7
]
unrefined_scaling_N7 = StrongScalingCase(
    unrefined_ranks_N7,
    SPX_ranks_per_gpu,
    unrefined_files_N7,
    lelg_unrefined,
    7,
    timestep_range,
)
print("\nunrefined SPX N=7")
unrefined_scaling_N7.scaling_calculations()

unrefined_ranks_N8 = [1, 2, 4, 6, 8, 16]
unrefined_files_N8 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_8.tsv"
    for rank in unrefined_ranks_N8
]
unrefined_scaling_N8 = StrongScalingCase(
    unrefined_ranks_N8,
    SPX_ranks_per_gpu,
    unrefined_files_N8,
    lelg_unrefined,
    8,
    timestep_range,
)
print("\nunrefined SPX N=8")
unrefined_scaling_N8.scaling_calculations()

unrefined_ranks_N9 = [1, 2, 4, 6, 8, 16]
unrefined_files_N9 = [
    unrefined_rootdir + str(rank) + "_ranks/" + unrefined_casedir + "/N_9.tsv"
    for rank in unrefined_ranks_N9
]
unrefined_scaling_N9 = StrongScalingCase(
    unrefined_ranks_N9,
    SPX_ranks_per_gpu,
    unrefined_files_N9,
    lelg_unrefined,
    9,
    timestep_range,
)
print("\nunrefined SPX N=9")
unrefined_scaling_N9.scaling_calculations()

unrefined_results = [
    unrefined_scaling_N1,
    unrefined_scaling_N2,
    unrefined_scaling_N3,
    unrefined_scaling_N4,
    unrefined_scaling_N5,
    unrefined_scaling_N6,
    unrefined_scaling_N7,
    unrefined_scaling_N8,
    unrefined_scaling_N9,
]


# load hRefine = 2 SPX results

# hRefine2_ranks_N1 = [1, 2]
hRefine2_ranks_N1 = []
hRefine2_files_N1 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_1.tsv"
    for rank in hRefine2_ranks_N1
]
hRefine2_scaling_N1 = StrongScalingCase(
    hRefine2_ranks_N1,
    SPX_ranks_per_gpu,
    hRefine2_files_N1,
    lelg_hRefine2,
    1,
    timestep_range,
)
print("\nhRefine = 2 SPX N=1")
hRefine2_scaling_N1.scaling_calculations()

hRefine2_ranks_N2 = [1, 2]
hRefine2_files_N2 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_2.tsv"
    for rank in hRefine2_ranks_N2
]
hRefine2_scaling_N2 = StrongScalingCase(
    hRefine2_ranks_N2,
    SPX_ranks_per_gpu,
    hRefine2_files_N2,
    lelg_hRefine2,
    2,
    timestep_range,
)
print("\nhRefine = 2 SPX N=2")
hRefine2_scaling_N2.scaling_calculations()

hRefine2_ranks_N3 = [1, 2, 4, 6]
hRefine2_files_N3 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_3.tsv"
    for rank in hRefine2_ranks_N3
]
hRefine2_scaling_N3 = StrongScalingCase(
    hRefine2_ranks_N3,
    SPX_ranks_per_gpu,
    hRefine2_files_N3,
    lelg_hRefine2,
    3,
    timestep_range,
)
print("\nhRefine = 2 SPX N=3")
hRefine2_scaling_N3.scaling_calculations()

hRefine2_ranks_N4 = [1, 2, 4, 6]
hRefine2_files_N4 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_4.tsv"
    for rank in hRefine2_ranks_N4
]
hRefine2_scaling_N4 = StrongScalingCase(
    hRefine2_ranks_N4,
    SPX_ranks_per_gpu,
    hRefine2_files_N4,
    lelg_hRefine2,
    4,
    timestep_range,
)
print("\nhRefine = 2 SPX N=4")
hRefine2_scaling_N4.scaling_calculations()

# hRefine2_ranks_N5 = [1, 2, 4, 6, 8, 16]
hRefine2_ranks_N5 = [2, 4, 6, 8, 16, 32]
hRefine2_files_N5 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_5.tsv"
    for rank in hRefine2_ranks_N5
]
hRefine2_scaling_N5 = StrongScalingCase(
    hRefine2_ranks_N5,
    SPX_ranks_per_gpu,
    hRefine2_files_N5,
    lelg_hRefine2,
    5,
    timestep_range,
)
print("\nhRefine = 2 SPX N=5")
hRefine2_scaling_N5.scaling_calculations()

# hRefine2_ranks_N6 = [1, 2, 4, 6, 8, 16]
hRefine2_ranks_N6 = [4, 6, 8, 16, 32]
hRefine2_files_N6 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_6.tsv"
    for rank in hRefine2_ranks_N6
]
hRefine2_scaling_N6 = StrongScalingCase(
    hRefine2_ranks_N6,
    SPX_ranks_per_gpu,
    hRefine2_files_N6,
    lelg_hRefine2,
    6,
    timestep_range,
)
print("\nhRefine = 2 SPX N=6")
hRefine2_scaling_N6.scaling_calculations()

# hRefine2_ranks_N7 = [1, 2, 4, 6, 8, 16]
hRefine2_ranks_N7 = [4, 6, 8, 16, 32]
hRefine2_files_N7 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_7.tsv"
    for rank in hRefine2_ranks_N7
]
hRefine2_scaling_N7 = StrongScalingCase(
    hRefine2_ranks_N7,
    SPX_ranks_per_gpu,
    hRefine2_files_N7,
    lelg_hRefine2,
    7,
    timestep_range,
)
print("\nhRefine = 2 SPX N=7")
hRefine2_scaling_N7.scaling_calculations()

# hRefine2_ranks_N8 = [1, 2, 4, 6, 8, 16]
hRefine2_ranks_N8 = [6, 8, 16, 32]
hRefine2_files_N8 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_8.tsv"
    for rank in hRefine2_ranks_N8
]
hRefine2_scaling_N8 = StrongScalingCase(
    hRefine2_ranks_N8,
    SPX_ranks_per_gpu,
    hRefine2_files_N8,
    lelg_hRefine2,
    8,
    timestep_range,
)
print("\nhRefine = 2 SPX N=8")
hRefine2_scaling_N8.scaling_calculations()

# hRefine2_ranks_N9 = [1, 2, 4, 6, 8, 16]
hRefine2_ranks_N9 = [8, 16, 32]
hRefine2_files_N9 = [
    hRefine2_rootdir + str(rank) + "_ranks/" + hRefine2_casedir + "/N_9.tsv"
    for rank in hRefine2_ranks_N9
]
hRefine2_scaling_N9 = StrongScalingCase(
    hRefine2_ranks_N9,
    SPX_ranks_per_gpu,
    hRefine2_files_N9,
    lelg_hRefine2,
    9,
    timestep_range,
)
print("\nhRefine = 2 SPX N=9")
hRefine2_scaling_N9.scaling_calculations()

hRefine2_results = [
    hRefine2_scaling_N1,
    hRefine2_scaling_N2,
    hRefine2_scaling_N3,
    hRefine2_scaling_N4,
    hRefine2_scaling_N5,
    hRefine2_scaling_N6,
    hRefine2_scaling_N7,
    hRefine2_scaling_N8,
    hRefine2_scaling_N9,
]


# plots

# time-per-timestep

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            unrefined_results[i].qps_per_gpu,
            unrefined_results[i].time_per_timestep,
            marker="x",
            ls=unrefined_linestyle,
            color=colour,
            label=f"unrefined SPX N={N}",
        )
        plt.plot(
            hRefine2_results[i].qps_per_gpu,
            hRefine2_results[i].time_per_timestep,
            marker="x",
            ls=hRefine2_linestyle,
            color=colour,
            label=f"hRefine = 2 SPX N={N}",
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
        [unrefined_linestyle, hRefine2_linestyle],
        ["unrefined (SPX)", "hRefine = 2 (SPX)"],
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
            unrefined_results[i].qps_per_gpu,
            unrefined_results[i].speedup,
            marker="x",
            ls=unrefined_linestyle,
            color=colour,
            label=f"unrefined SPX N={N}",
        )
        plt.plot(
            hRefine2_results[i].qps_per_gpu,
            hRefine2_results[i].speedup,
            marker="x",
            ls=hRefine2_linestyle,
            color=colour,
            label=f"hRefine = 2 SPX N={N}",
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
        [unrefined_linestyle, hRefine2_linestyle],
        ["unrefined (SPX)", "hRefine = 2 (SPX)"],
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
            unrefined_results[i].qps_per_gpu,
            unrefined_results[i].parallel_efficiency,
            marker="x",
            ls=unrefined_linestyle,
            color=colour,
            label=f"unrefined SPX N={N}",
        )
        plt.plot(
            hRefine2_results[i].qps_per_gpu,
            hRefine2_results[i].parallel_efficiency,
            marker="x",
            ls=hRefine2_linestyle,
            color=colour,
            label=f"hRefine = 2 SPX N={N}",
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
        [unrefined_linestyle, hRefine2_linestyle],
        ["unrefined (SPX)", "hRefine = 2 (SPX)"],
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
