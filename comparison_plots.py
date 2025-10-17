import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.lines import Line2D
import numpy as np
from scaling import StrongScalingCase
from scaling import WeakScalingCases

align_cpx_with_spx = True  # limit number of points plotted so they cover the same range
# align_cpx_with_spx = False  # limit number of points plotted so they cover the same range

savedir = "comparison_plots/comp1"
SPX_casedir = "run1"
CPX_casedir = "run3"

savedir = "comparison_plots/comp2_exclusive"
SPX_casedir = "run3"
CPX_casedir = "run4"

timestep_range = slice(100, 2000)
lelg = 54000  # number of elements in .re2 mesh

N_values = range(1, 10)
colours = cm.tab10(np.linspace(0, 1, len(N_values)))

# N_values_to_plot = N_values
# suffix = ""

# min_N = 8
# max_N = 9
# N_values_to_plot = range(min_N, max_N+1)
# suffix = f"_N_{N_values_to_plot[0]}-{N_values_to_plot[-1]}"

N_values_to_plot = [9]
suffix = f"_N_{N_values_to_plot[0]}"

if align_cpx_with_spx:
    suffix += f"_aligned"

SPX_ranks_per_gpu = 1
SPX_linestyle = "-"

CPX_ranks_per_gpu = 8
CPX_linestyle = "--"


# load SPX results

SPX_ranks_N1 = [1, 2]
SPX_files_N1 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_1.tsv" for rank in SPX_ranks_N1
]
SPX_scaling_N1 = StrongScalingCase(
    SPX_ranks_N1, SPX_ranks_per_gpu, SPX_files_N1, lelg, 1, timestep_range
)
print(f"\nSPX N=1")
SPX_scaling_N1.scaling_calculations()

SPX_ranks_N2 = [1, 2]
SPX_files_N2 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_2.tsv" for rank in SPX_ranks_N2
]
SPX_scaling_N2 = StrongScalingCase(
    SPX_ranks_N2, SPX_ranks_per_gpu, SPX_files_N2, lelg, 2, timestep_range
)
print(f"\nSPX N=2")
SPX_scaling_N2.scaling_calculations()

SPX_ranks_N3 = [1, 2, 4, 6]
SPX_files_N3 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_3.tsv" for rank in SPX_ranks_N3
]
SPX_scaling_N3 = StrongScalingCase(
    SPX_ranks_N3, SPX_ranks_per_gpu, SPX_files_N3, lelg, 3, timestep_range
)
print(f"\nSPX N=3")
SPX_scaling_N3.scaling_calculations()

SPX_ranks_N4 = [1, 2, 4, 6]
SPX_files_N4 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_4.tsv" for rank in SPX_ranks_N4
]
SPX_scaling_N4 = StrongScalingCase(
    SPX_ranks_N4, SPX_ranks_per_gpu, SPX_files_N4, lelg, 4, timestep_range
)
print(f"\nSPX N=4")
SPX_scaling_N4.scaling_calculations()

SPX_ranks_N5 = [1, 2, 4, 6, 8, 16]
SPX_files_N5 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_5.tsv" for rank in SPX_ranks_N5
]
SPX_scaling_N5 = StrongScalingCase(
    SPX_ranks_N5, SPX_ranks_per_gpu, SPX_files_N5, lelg, 5, timestep_range
)
print(f"\nSPX N=5")
SPX_scaling_N5.scaling_calculations()

SPX_ranks_N6 = [2, 4, 6, 8, 16]
SPX_files_N6 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_6.tsv" for rank in SPX_ranks_N6
]
SPX_scaling_N6 = StrongScalingCase(
    SPX_ranks_N6, SPX_ranks_per_gpu, SPX_files_N6, lelg, 6, timestep_range
)
print(f"\nSPX N=6")
SPX_scaling_N6.scaling_calculations()

SPX_ranks_N7 = [2, 4, 6, 8, 16]
SPX_files_N7 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_7.tsv" for rank in SPX_ranks_N7
]
SPX_scaling_N7 = StrongScalingCase(
    SPX_ranks_N7, SPX_ranks_per_gpu, SPX_files_N7, lelg, 7, timestep_range
)
print(f"\nSPX N=7")
SPX_scaling_N7.scaling_calculations()

SPX_ranks_N8 = [4, 6, 8, 16]
SPX_files_N8 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_8.tsv" for rank in SPX_ranks_N8
]
SPX_scaling_N8 = StrongScalingCase(
    SPX_ranks_N8, SPX_ranks_per_gpu, SPX_files_N8, lelg, 8, timestep_range
)
print(f"\nSPX N=8")
SPX_scaling_N8.scaling_calculations()

SPX_ranks_N9 = [4, 6, 8, 16]
SPX_files_N9 = [
    "SPX/" + str(rank) + "_ranks/" + SPX_casedir + "/N_9.tsv" for rank in SPX_ranks_N9
]
SPX_scaling_N9 = StrongScalingCase(
    SPX_ranks_N9, SPX_ranks_per_gpu, SPX_files_N9, lelg, 9, timestep_range
)
print(f"\nSPX N=9")
SPX_scaling_N9.scaling_calculations()

SPX_results = [
    SPX_scaling_N1,
    SPX_scaling_N2,
    SPX_scaling_N3,
    SPX_scaling_N4,
    SPX_scaling_N5,
    SPX_scaling_N6,
    SPX_scaling_N7,
    SPX_scaling_N8,
    SPX_scaling_N9,
]

# load CPX results

CPX_ranks_N1 = [8, 12, 16]
CPX_files_N1 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_1.tsv" for rank in CPX_ranks_N1
]
CPX_scaling_N1 = StrongScalingCase(
    CPX_ranks_N1, CPX_ranks_per_gpu, CPX_files_N1, lelg, 1, timestep_range
)
print(f"\nCPX N=1")
CPX_scaling_N1.scaling_calculations()

CPX_ranks_N2 = [8, 12, 16]
CPX_files_N2 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_2.tsv" for rank in CPX_ranks_N2
]
CPX_scaling_N2 = StrongScalingCase(
    CPX_ranks_N2, CPX_ranks_per_gpu, CPX_files_N2, lelg, 2, timestep_range
)
print(f"\nCPX N=2")
CPX_scaling_N2.scaling_calculations()

CPX_ranks_N3 = [8, 12, 16, 24, 32, 40, 48]
CPX_files_N3 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_3.tsv" for rank in CPX_ranks_N3
]
CPX_scaling_N3 = StrongScalingCase(
    CPX_ranks_N3, CPX_ranks_per_gpu, CPX_files_N3, lelg, 3, timestep_range
)
print(f"\nCPX N=3")
CPX_scaling_N3.scaling_calculations()

CPX_ranks_N4 = [8, 12, 16, 24, 32, 40, 48]
CPX_files_N4 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_4.tsv" for rank in CPX_ranks_N4
]
CPX_scaling_N4 = StrongScalingCase(
    CPX_ranks_N4, CPX_ranks_per_gpu, CPX_files_N4, lelg, 4, timestep_range
)
print(f"\nCPX N=4")
CPX_scaling_N4.scaling_calculations()

CPX_ranks_N5 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
CPX_files_N5 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_5.tsv" for rank in CPX_ranks_N5
]
CPX_scaling_N5 = StrongScalingCase(
    CPX_ranks_N5, CPX_ranks_per_gpu, CPX_files_N5, lelg, 5, timestep_range
)
print(f"\nCPX N=5")
CPX_scaling_N5.scaling_calculations()

if align_cpx_with_spx:
    CPX_ranks_N6 = [16, 24, 32, 40, 48, 56, 64, 128]  # to align with SPX cases
else:
    CPX_ranks_N6 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]

CPX_files_N6 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_6.tsv" for rank in CPX_ranks_N6
]
CPX_scaling_N6 = StrongScalingCase(
    CPX_ranks_N6, CPX_ranks_per_gpu, CPX_files_N6, lelg, 6, timestep_range
)
print(f"\nCPX N=6")
CPX_scaling_N6.scaling_calculations()

if align_cpx_with_spx:
    CPX_ranks_N7 = [16, 24, 32, 40, 48, 56, 64, 128]  # to align with SPX cases
else:
    CPX_ranks_N7 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]

CPX_files_N7 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_7.tsv" for rank in CPX_ranks_N7
]
CPX_scaling_N7 = StrongScalingCase(
    CPX_ranks_N7, CPX_ranks_per_gpu, CPX_files_N7, lelg, 7, timestep_range
)
print(f"\nCPX N=7")
CPX_scaling_N7.scaling_calculations()

if align_cpx_with_spx:
    # CPX_ranks_N8 = [32, 40, 48, 56, 64, 128]  # to align with SPX cases
    CPX_ranks_N8 = [32, 40, 56, 64, 128]  # to align with SPX cases; 48 failed due to timeout?
else:
    # CPX_ranks_N8 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
    CPX_ranks_N8 = [8, 12, 16, 24, 32, 40, 56, 64, 128] # 48 failed due to timeout?

CPX_files_N8 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_8.tsv" for rank in CPX_ranks_N8
]
CPX_scaling_N8 = StrongScalingCase(
    CPX_ranks_N8, CPX_ranks_per_gpu, CPX_files_N8, lelg, 8, timestep_range
)
print(f"\nCPX N=8")
CPX_scaling_N8.scaling_calculations()

if align_cpx_with_spx:
    CPX_ranks_N9 = [32, 40, 48, 56, 64, 128]  # to align with SPX cases
else:
    CPX_ranks_N9 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]

CPX_files_N9 = [
    "CPX/" + str(rank) + "_ranks/" + CPX_casedir + "/N_9.tsv" for rank in CPX_ranks_N9
]
CPX_scaling_N9 = StrongScalingCase(
    CPX_ranks_N9, CPX_ranks_per_gpu, CPX_files_N9, lelg, 9, timestep_range
)
print(f"\nCPX N=9")
CPX_scaling_N9.scaling_calculations()

CPX_results = [
    CPX_scaling_N1,
    CPX_scaling_N2,
    CPX_scaling_N3,
    CPX_scaling_N4,
    CPX_scaling_N5,
    CPX_scaling_N6,
    CPX_scaling_N7,
    CPX_scaling_N8,
    CPX_scaling_N9,
]

# plots

# time-per-timestep

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            SPX_results[i].qps_per_gpu,
            SPX_results[i].time_per_timestep,
            marker="x",
            ls=SPX_linestyle,
            color=colour,
            label=f"SPX N={N}",
        )
        plt.plot(
            CPX_results[i].qps_per_gpu,
            CPX_results[i].time_per_timestep,
            marker="x",
            ls=CPX_linestyle,
            color=colour,
            label=f"CPX N={N}",
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
    for ls, lbl in zip([CPX_linestyle, SPX_linestyle], ["CPX (8 partitions)", "SPX (full GPU)"])
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
    title="Partitioning",
    bbox_to_anchor=(0.6, 1.0),
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.savefig(f"{savedir}/time_per_timestep_qps_gpu"+suffix+".png", bbox_inches="tight")
plt.close()

# speedup

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            SPX_results[i].qps_per_gpu,
            SPX_results[i].speedup,
            marker="x",
            ls=SPX_linestyle,
            color=colour,
            label=f"SPX N={N}",
        )
        plt.plot(
            CPX_results[i].qps_per_gpu,
            CPX_results[i].speedup,
            marker="x",
            ls=CPX_linestyle,
            color=colour,
            label=f"CPX N={N}",
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
    for ls, lbl in zip([CPX_linestyle, SPX_linestyle], ["CPX (8 partitions)", "SPX (full GPU)"])
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
    title="Partitioning",
    bbox_to_anchor=(0.6, 1.0),
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.savefig(f"{savedir}/speedup_qps_gpu"+suffix+".png", bbox_inches="tight")
plt.close()

# efficiency

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        plt.plot(
            SPX_results[i].qps_per_gpu,
            SPX_results[i].parallel_efficiency,
            marker="x",
            ls=SPX_linestyle,
            color=colour,
            label=f"SPX N={N}",
        )
        plt.plot(
            CPX_results[i].qps_per_gpu,
            CPX_results[i].parallel_efficiency,
            marker="x",
            ls=CPX_linestyle,
            color=colour,
            label=f"CPX N={N}",
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
    for ls, lbl in zip([CPX_linestyle, SPX_linestyle], ["CPX (8 partitions)", "SPX (full GPU)"])
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
    title="Partitioning",
    loc="lower center",
    frameon=False,
)
plt.gca().add_artist(legend1)  # Keep the first legend

plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.savefig(f"{savedir}/efficiency_qps_gpu"+suffix+".png", bbox_inches="tight")
plt.close()
