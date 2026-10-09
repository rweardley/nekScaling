import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("../")
from pyscaling.scaling import StrongScalingCase
from pyscaling.scaling import WeakScalingCases

savedir = "scaling_plots"
casedir = ""

# get reference data
# time-per-timestep for each N for 1 full node of MI355X
# plot it as a horizontal line for each case

timestep_range = slice(100, 2000)
lelg = 54000  # number of elements in .re2 mesh

# device = "socket"
device = "node"

if device == "socket":
    ranks_per_device = 56
elif device == "node":
    ranks_per_device = 112

reference_ranks = 8
reference_dir = f"../../../zenith_mi355x/laminarPipe/SPX/{reference_ranks}_ranks/"
polynomial_orders = [5, 6, 7, 8, 9]
reference_time_per_timestep = []
for order in polynomial_orders:
    scaling = StrongScalingCase(
        [reference_ranks], 1, [f"{reference_dir}/N_{order}.tsv"], lelg, order, timestep_range
    )
    scaling.scaling_calculations()
    reference_time_per_timestep.append(scaling.time_per_timestep[0])
N_to_ref_time = dict(zip(polynomial_orders, reference_time_per_timestep))
print(N_to_ref_time)

# N=1 runs failed - unlikely to ever want to run this, so not a big problem
# ranks_N1 = [1, 2]
# files_N1 = [str(rank)+"_ranks/"+casedir+"/N_1.tsv" for rank in ranks_N1]
# scaling_N1 = StrongScalingCase(ranks_N1, ranks_per_device, files_N1, lelg, 1, timestep_range)
# print(f"\nN=1")
# scaling_N1.scaling_calculations()

# ranks_N2 = [1, 2]
# files_N2 = [str(rank)+"_ranks/"+casedir+"/N_2.tsv" for rank in ranks_N2]
# scaling_N2 = StrongScalingCase(ranks_N2, ranks_per_device, files_N2, lelg, 2, timestep_range)
# print(f"\nN=2")
# scaling_N2.scaling_calculations()

# ranks_N3 = [8, 14, 28, 56, 112, 224]
ranks_N3 = [28, 56]
files_N3 = [str(rank)+"_ranks/"+casedir+"/N_3.tsv" for rank in ranks_N3]
scaling_N3 = StrongScalingCase(ranks_N3, ranks_per_device, files_N3, lelg, 3, timestep_range)
print(f"\nN=3")
scaling_N3.scaling_calculations()

# ranks_N4 = [8, 14, 28, 56, 112, 224]
ranks_N4 = [28, 56]
files_N4 = [str(rank)+"_ranks/"+casedir+"/N_4.tsv" for rank in ranks_N4]
scaling_N4 = StrongScalingCase(ranks_N4, ranks_per_device, files_N4, lelg, 4, timestep_range)
print(f"\nN=4")
scaling_N4.scaling_calculations()

# ranks_N5 = [8, 14, 28, 56, 112, 224]
ranks_N5 = [28, 56, 112]
files_N5 = [str(rank)+"_ranks/"+casedir+"/N_5.tsv" for rank in ranks_N5]
scaling_N5 = StrongScalingCase(ranks_N5, ranks_per_device, files_N5, lelg, 5, timestep_range)
print(f"\nN=5")
scaling_N5.scaling_calculations()

# ranks_N6 = [8, 14, 28, 56, 112, 224]
ranks_N6 = [28, 56, 112]
files_N6 = [str(rank)+"_ranks/"+casedir+"/N_6.tsv" for rank in ranks_N6]
scaling_N6 = StrongScalingCase(ranks_N6, ranks_per_device, files_N6, lelg, 6, timestep_range)
print(f"\nN=6")
scaling_N6.scaling_calculations()

# ranks_N7 = [8, 14, 28, 56, 112, 224]
ranks_N7 = [28, 56, 112]
files_N7 = [str(rank)+"_ranks/"+casedir+"/N_7.tsv" for rank in ranks_N7]
scaling_N7 = StrongScalingCase(ranks_N7, ranks_per_device, files_N7, lelg, 7, timestep_range)
print(f"\nN=7")
scaling_N7.scaling_calculations()

# ranks_N8 = [8, 14, 28, 56, 112, 224]
ranks_N8 = [28, 56, 112]
files_N8 = [str(rank)+"_ranks/"+casedir+"/N_8.tsv" for rank in ranks_N8]
scaling_N8 = StrongScalingCase(ranks_N8, ranks_per_device, files_N8, lelg, 8, timestep_range)
print(f"\nN=8")
scaling_N8.scaling_calculations()

# ranks_N9 = [8, 14, 28, 56, 112, 224]
ranks_N9 = [28, 56, 112]
files_N9 = [str(rank)+"_ranks/"+casedir+"/N_9.tsv" for rank in ranks_N9]
scaling_N9 = StrongScalingCase(ranks_N9, ranks_per_device, files_N9, lelg, 9, timestep_range)
print(f"\nN=9")
scaling_N9.scaling_calculations()

fig, ax = plt.subplots()
plt.plot(ranks_N3, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(ranks_N4, scaling_N4.time_per_timestep, "x-", label=r"$N=4$")
plt.plot(ranks_N5, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(ranks_N6, scaling_N6.time_per_timestep, "x-", label=r"$N=6$")
plt.plot(ranks_N7, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(ranks_N8, scaling_N8.time_per_timestep, "x-", label=r"$N=8$")
plt.plot(ranks_N9, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel("Ranks")
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(np.array(ranks_N3)/ranks_per_device, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(np.array(ranks_N4)/ranks_per_device, scaling_N4.time_per_timestep, "x-", label=r"$N=4$")
plt.plot(np.array(ranks_N5)/ranks_per_device, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(np.array(ranks_N6)/ranks_per_device, scaling_N6.time_per_timestep, "x-", label=r"$N=6$")
plt.plot(np.array(ranks_N7)/ranks_per_device, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(np.array(ranks_N8)/ranks_per_device, scaling_N8.time_per_timestep, "x-", label=r"$N=8$")
plt.plot(np.array(ranks_N9)/ranks_per_device, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(f"{device.capitalize()}s")
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_{device}s.png", bbox_inches="tight")
plt.close()


for N_val in polynomial_orders:
    fig, ax = plt.subplots()
    time_per_timestep = globals()[f"scaling_N{N_val}"].time_per_timestep
    ranks = globals()[f"ranks_N{N_val}"]
    plt.plot(
        ranks,
        time_per_timestep,
        "x-",
        label=rf"$N={N_val}$",
    )
    plt.axhline(N_to_ref_time[N_val])
    plt.xlabel("Ranks")
    plt.ylabel("Walltime per timestep [s]")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(
        f"{savedir}/time_per_timestep_ranks_N{N_val}.png", bbox_inches="tight"
    )
    plt.close()

    fig, ax = plt.subplots()
    time_per_timestep = globals()[f"scaling_N{N_val}"].time_per_timestep
    ranks = globals()[f"ranks_N{N_val}"]
    plt.plot(
        np.array(ranks) / ranks_per_device,
        time_per_timestep,
        "x-",
        label=rf"$N={N_val}$",
    )
    plt.axhline(N_to_ref_time[N_val])
    plt.xlabel(f"{device.capitalize()}s")
    plt.ylabel("Walltime per timestep [s]")
    plt.yscale("log")
    plt.legend(frameon=False)
    plt.savefig(
        f"{savedir}/time_per_timestep_{device}s_N{N_val}.png",
        bbox_inches="tight",
    )
    plt.close()

fig, ax = plt.subplots()
plt.plot(ranks_N3, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(ranks_N4, scaling_N4.speedup, "x-", label=r"$N=4$")
plt.plot(ranks_N5, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(ranks_N6, scaling_N6.speedup, "x-", label=r"$N=6$")
plt.plot(ranks_N7, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(ranks_N8, scaling_N8.speedup, "x-", label=r"$N=8$")
plt.plot(ranks_N9, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(ranks_N3, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(ranks_N4, scaling_N4.ideal_speedup, "k--")
plt.plot(ranks_N5, scaling_N5.ideal_speedup, "k--")
plt.plot(ranks_N6, scaling_N6.ideal_speedup, "k--")
plt.plot(ranks_N7, scaling_N7.ideal_speedup, "k--")
plt.plot(ranks_N8, scaling_N8.ideal_speedup, "k--")
plt.plot(ranks_N9, scaling_N9.ideal_speedup, "k--")
plt.xlabel("Ranks")
plt.ylabel("Speedup")
plt.ylim(0, None)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_ranks.png", bbox_inches="tight")
plt.close()

plt.plot(ranks_N3, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(ranks_N4, scaling_N4.parallel_efficiency, "x-", label=r"$N=4$")
plt.plot(ranks_N5, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(ranks_N6, scaling_N6.parallel_efficiency, "x-", label=r"$N=6$")
plt.plot(ranks_N7, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(ranks_N8, scaling_N8.parallel_efficiency, "x-", label=r"$N=8$")
plt.plot(ranks_N9, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel("Ranks")
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_rank, scaling_N4.time_per_timestep, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_rank, scaling_N6.time_per_timestep, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_rank, scaling_N8.time_per_timestep, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_qps_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_device, scaling_N4.time_per_timestep, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_device, scaling_N6.time_per_timestep, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_device, scaling_N8.time_per_timestep, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_device, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(rf"Quadrature Points per {device} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(
    f"{savedir}/time_per_timestep_qps_{device}.png", bbox_inches="tight"
)
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_rank, scaling_N4.speedup, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_rank, scaling_N6.speedup, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_rank, scaling_N8.speedup, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(scaling_N3.qps_per_rank, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(scaling_N4.qps_per_rank, scaling_N4.ideal_speedup, "k--")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.ideal_speedup, "k--")
plt.plot(scaling_N6.qps_per_rank, scaling_N6.ideal_speedup, "k--")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.ideal_speedup, "k--")
plt.plot(scaling_N8.qps_per_rank, scaling_N8.ideal_speedup, "k--")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.ideal_speedup, "k--")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.ylim(0, 5)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_qps_rank.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_device, scaling_N4.speedup, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_device, scaling_N6.speedup, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_device, scaling_N8.speedup, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_device, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(scaling_N3.qps_per_device, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(scaling_N4.qps_per_device, scaling_N4.ideal_speedup, "k--")
plt.plot(scaling_N5.qps_per_device, scaling_N5.ideal_speedup, "k--")
plt.plot(scaling_N6.qps_per_device, scaling_N6.ideal_speedup, "k--")
plt.plot(scaling_N7.qps_per_device, scaling_N7.ideal_speedup, "k--")
plt.plot(scaling_N8.qps_per_device, scaling_N8.ideal_speedup, "k--")
plt.plot(scaling_N9.qps_per_device, scaling_N9.ideal_speedup, "k--")
plt.xlabel(rf"Quadrature Points per {device} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.ylim(0, 5)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_qps_{device}.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_rank, scaling_N4.parallel_efficiency, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_rank, scaling_N6.parallel_efficiency, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_rank, scaling_N8.parallel_efficiency, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_qps_rank.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_device, scaling_N4.parallel_efficiency, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_device, scaling_N6.parallel_efficiency, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_device, scaling_N8.parallel_efficiency, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_device, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel(rf"Quadrature Points per {device} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_qps_{device}.png", bbox_inches="tight")
plt.close()

# # weak scaling

# strong_scaling_cases = [scaling_N1, scaling_N2, scaling_N3, scaling_N4, scaling_N5, scaling_N6, scaling_N7, scaling_N8, scaling_N9]
# weak_scaling_cases = WeakScalingCases(strong_scaling_cases)

# qps_per_rank_range = [0.81e6, 0.88e6]
# ranks, scaled_speedup = weak_scaling_cases.weak_scaling_calculations(*qps_per_rank_range)
# plt.plot(ranks, scaled_speedup, "x-", label=f"{qps_per_rank_range}")

# qps_per_rank_range = [0.0, 0.2e6]
# ranks, scaled_speedup = weak_scaling_cases.weak_scaling_calculations(*qps_per_rank_range)
# plt.plot(ranks, scaled_speedup, "x-", label=f"{qps_per_rank_range}")

# plt.xlabel("Ranks")
# plt.ylabel("Scaled Speedup")
# plt.legend(frameon=False)
# plt.savefig(f"{savedir}/weak_scaling.png", bbox_inches="tight")
# plt.close()
