import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.lines import Line2D
import numpy as np
from scaling import StrongScalingCase

savedir = "comparison_plots/hvt"

timestep_range = slice(100, 2000)
lelg = 1591954  # number of elements in .re2 mesh

N_values = [3, 5]
colours = ["red", "blue"]

N_values_to_plot = [3, 5]
suffix = ""
# suffix = f"_N_{N_values_to_plot[0]}"

SPX_ranks_per_gpu = 1
SPX_linestyle = "-"
SPX_points = "+"

CPX_ranks_per_gpu = 8
CPX_linestyle = "--"
CPX_points = "x"

QPX_ranks_per_gpu = 4
QPX_linestyle = ":"
QPX_points = "^"


# load SPX results

SPX_ranks_N3 = [8]
SPX_files_N3 = ["SPX/hvt/N3_1_node/summary.tsv"]
SPX_scaling_N3 = StrongScalingCase(
    SPX_ranks_N3, SPX_ranks_per_gpu, SPX_files_N3, lelg, 3, timestep_range
)
print(f"\nSPX N=3")
SPX_scaling_N3.scaling_calculations()

SPX_ranks_N5 = [16]
SPX_files_N5 = ["SPX/hvt/N5_2_nodes/summary.tsv"]
SPX_scaling_N5 = StrongScalingCase(
    SPX_ranks_N5, SPX_ranks_per_gpu, SPX_files_N5, lelg, 5, timestep_range
)
print(f"\nSPX N=5")
SPX_scaling_N5.scaling_calculations()

SPX_results = [
    SPX_scaling_N3,
    SPX_scaling_N5,
]

# load CPX results

CPX_ranks_N3 = [64]
CPX_files_N3 = ["CPX/hvt/N3_1_node/summary.tsv"]
CPX_scaling_N3 = StrongScalingCase(
    CPX_ranks_N3, CPX_ranks_per_gpu, CPX_files_N3, lelg, 3, timestep_range
)
print(f"\nCPX N=3")
CPX_scaling_N3.scaling_calculations()

CPX_ranks_N5 = [128]
CPX_files_N5 = ["CPX/hvt/N5_2_nodes/summary.tsv"]
CPX_scaling_N5 = StrongScalingCase(
    CPX_ranks_N5, CPX_ranks_per_gpu, CPX_files_N5, lelg, 5, timestep_range
)
print(f"\nCPX N=5")
CPX_scaling_N5.scaling_calculations()

CPX_results = [
    CPX_scaling_N3,
    CPX_scaling_N5,
]

# load QPX results

# QPX_ranks_N5 = [10, 12, 16, 24, 32]
QPX_ranks_N5 = [12, 16, 24, 32]
QPX_files_N5 = ["QPX/hvt/N5_" + str(ranks) + "_ranks/summary.tsv" for ranks in QPX_ranks_N5]
QPX_scaling_N5 = StrongScalingCase(
    QPX_ranks_N5, QPX_ranks_per_gpu, QPX_files_N5, lelg, 5, timestep_range
)
print(f"\nQPX N=5")
QPX_scaling_N5.scaling_calculations()

QPX_results = [None, QPX_scaling_N5]

# plots

# time-per-timestep

fig, ax = plt.subplots(figsize=(8, 5), dpi=160)

for i, N in enumerate(N_values):
    if N in N_values_to_plot:
        colour = colours[i]
        if SPX_results[i]:
            plt.plot(
                SPX_results[i].qps_per_gpu,
                SPX_results[i].time_per_timestep,
                marker=SPX_points,
                ls=SPX_linestyle,
                color=colour,
                label=f"SPX N={N}",
            )
        if CPX_results[i]:
            plt.plot(
                CPX_results[i].qps_per_gpu,
                CPX_results[i].time_per_timestep,
                marker=CPX_points,
                ls=CPX_linestyle,
                color=colour,
                label=f"CPX N={N}",
            )
        if QPX_results[i]:
            plt.plot(
                QPX_results[i].qps_per_gpu,
                QPX_results[i].time_per_timestep,
                marker=QPX_points,
                ls=QPX_linestyle,
                color=colour,
                label=f"QPX N={N}",
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
    Line2D([0], [0], color="k", lw=2, linestyle=ls, marker=mkr, label=f"{lbl}")
    for ls, mkr, lbl in zip([CPX_linestyle, QPX_linestyle, SPX_linestyle],
                            [CPX_points, QPX_points, SPX_points],
                            ["CPX (8 partitions)", "QPX (4 partitions)", "SPX (full GPU)"])
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
        if SPX_results[i]:
            plt.plot(
                SPX_results[i].qps_per_gpu,
                SPX_results[i].speedup,
                marker=SPX_points,
                ls=SPX_linestyle,
                color=colour,
                label=f"SPX N={N}",
            )
            plt.plot(
                SPX_results[i].qps_per_gpu,
                SPX_results[i].ideal_speedup,
                "k-."
            )
        if CPX_results[i]:
            plt.plot(
                CPX_results[i].qps_per_gpu,
                CPX_results[i].speedup,
                marker=CPX_points,
                ls=CPX_linestyle,
                color=colour,
                label=f"CPX N={N}",
            )
            plt.plot(
                CPX_results[i].qps_per_gpu,
                CPX_results[i].ideal_speedup,
                "k-."
            )
        if QPX_results[i]:
            plt.plot(
                QPX_results[i].qps_per_gpu,
                QPX_results[i].speedup,
                marker=QPX_points,
                ls=QPX_linestyle,
                color=colour,
                label=f"QPX N={N}",
            )
            plt.plot(
                QPX_results[i].qps_per_gpu,
                QPX_results[i].ideal_speedup,
                "k-."
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
    Line2D([0], [0], color="k", lw=2, linestyle=ls, marker=mkr, label=f"{lbl}")
    for ls, mkr, lbl in zip([CPX_linestyle, QPX_linestyle, SPX_linestyle, "-."],
                            [CPX_points, QPX_points, SPX_points, None],
                            ["CPX (8 partitions)", "QPX (4 partitions)", "SPX (full GPU)", "Ideal"])
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
    loc="upper right",
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
        if SPX_results[i]:
            plt.plot(
                SPX_results[i].qps_per_gpu,
                SPX_results[i].parallel_efficiency,
                marker=SPX_points,
                ls=SPX_linestyle,
                color=colour,
                label=f"SPX N={N}",
            )
        if CPX_results[i]:
            plt.plot(
                CPX_results[i].qps_per_gpu,
                CPX_results[i].parallel_efficiency,
                marker=CPX_points,
                ls=CPX_linestyle,
                color=colour,
                label=f"CPX N={N}",
            )
        if QPX_results[i]:
            plt.plot(
                QPX_results[i].qps_per_gpu,
                QPX_results[i].parallel_efficiency,
                marker=QPX_points,
                ls=QPX_linestyle,
                color=colour,
                label=f"QPX N={N}",
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
    Line2D([0], [0], color="k", lw=2, linestyle=ls, marker=mkr, label=f"{lbl}")
    for ls, mkr, lbl in zip([CPX_linestyle, QPX_linestyle, SPX_linestyle],
                            [CPX_points, QPX_points, SPX_points],
                            ["CPX (8 partitions)", "QPX (4 partitions)", "SPX (full GPU)"])
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
