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

reference_ranks = 1
reference_dir = f"../../../zenith_mi355x/laminarPipe/SPX/{reference_ranks}_ranks/"
polynomial_orders = [3, 5, 7, 9]
reference_time_per_timestep = []
print("Single-GPU reference data:")
for order in polynomial_orders:
    print(f"N={order}")
    scaling = StrongScalingCase(
        [reference_ranks], 1, [f"{reference_dir}/N_{order}.tsv"], lelg, order, timestep_range
    )
    scaling.scaling_calculations()
    reference_time_per_timestep.append(scaling.time_per_timestep[0])
N_to_ref_time = dict(zip(polynomial_orders, reference_time_per_timestep))

ranks_N3 = [8, 14, 28, 56, 112, 224, 336, 448]
files_N3 = [str(rank)+"_ranks/"+casedir+"/N_3.tsv" for rank in ranks_N3]
scaling_N3 = StrongScalingCase(ranks_N3, ranks_per_device, files_N3, lelg, 3, timestep_range, device_type=device)
print(f"\nN=3")
scaling_N3.scaling_calculations()

ranks_N5 = [8, 14, 28, 56, 112, 224, 336, 448]
files_N5 = [str(rank)+"_ranks/"+casedir+"/N_5.tsv" for rank in ranks_N5]
scaling_N5 = StrongScalingCase(
    ranks_N5,
    ranks_per_device,
    files_N5,
    lelg,
    5,
    timestep_range,
    device_type=device,
)
print(f"\nN=5")
scaling_N5.scaling_calculations()

ranks_N7 = [8, 14, 28, 56, 112, 224, 336, 448]
files_N7 = [str(rank)+"_ranks/"+casedir+"/N_7.tsv" for rank in ranks_N7]
scaling_N7 = StrongScalingCase(
    ranks_N7,
    ranks_per_device,
    files_N7,
    lelg,
    7,
    timestep_range,
    device_type=device,
)
print(f"\nN=7")
scaling_N7.scaling_calculations()

ranks_N9 = [112, 224, 336, 448]
files_N9 = [str(rank)+"_ranks/"+casedir+"/N_9.tsv" for rank in ranks_N9]
scaling_N9 = StrongScalingCase(
    ranks_N9,
    ranks_per_device,
    files_N9,
    lelg,
    9,
    timestep_range,
    device_type=device,
)
print(f"\nN=9")
scaling_N9.scaling_calculations()

fig, ax = plt.subplots()
plt.plot(ranks_N3, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(ranks_N5, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(ranks_N7, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(ranks_N9, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel("Ranks")
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(np.array(ranks_N3)/ranks_per_device, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(np.array(ranks_N5)/ranks_per_device, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(np.array(ranks_N7)/ranks_per_device, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
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
plt.plot(ranks_N5, N_to_ref_time[5]/scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(ranks_N7, N_to_ref_time[7]/scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(ranks_N9, N_to_ref_time[9]/scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel("Ranks")
plt.ylabel("Speedup vs GPU")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_vs_GPU_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(np.array(ranks_N5)/ranks_per_device, N_to_ref_time[5]/scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(np.array(ranks_N7)/ranks_per_device, N_to_ref_time[7]/scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(np.array(ranks_N9)/ranks_per_device, N_to_ref_time[9]/scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(f"{device.capitalize()}s")
plt.ylabel("Speedup vs GPU")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_vs_GPU_{device}s.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(ranks_N3, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(ranks_N5, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(ranks_N7, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(ranks_N9, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(ranks_N3, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(ranks_N5, scaling_N5.ideal_speedup, "k--")
plt.plot(ranks_N7, scaling_N7.ideal_speedup, "k--")
plt.plot(ranks_N9, scaling_N9.ideal_speedup, "k--")
plt.xlabel("Ranks")
plt.ylabel("Speedup")
plt.ylim(0, None)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_ranks.png", bbox_inches="tight")
plt.close()

plt.plot(ranks_N3, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(ranks_N5, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(ranks_N7, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(ranks_N9, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel("Ranks")
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_qps_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
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
plt.plot(scaling_N5.qps_per_rank, N_to_ref_time[5]/scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_rank, N_to_ref_time[7]/scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_rank, N_to_ref_time[9]/scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup vs GPU")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_vs_GPU_qps_ranks.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N5.qps_per_device, N_to_ref_time[5]/scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_device, N_to_ref_time[7]/scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_device, N_to_ref_time[9]/scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(rf"Quadrature Points per {device.capitalize()} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup vs GPU")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_vs_GPU_qps_{device}s.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(scaling_N3.qps_per_rank, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.ideal_speedup, "k--")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.ideal_speedup, "k--")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.ideal_speedup, "k--")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.ylim(0, 40)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_qps_rank.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_device, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(scaling_N3.qps_per_device, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(scaling_N5.qps_per_device, scaling_N5.ideal_speedup, "k--")
plt.plot(scaling_N7.qps_per_device, scaling_N7.ideal_speedup, "k--")
plt.plot(scaling_N9.qps_per_device, scaling_N9.ideal_speedup, "k--")
plt.xlabel(rf"Quadrature Points per {device} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.ylim(0, 40)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_qps_{device}.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_rank, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_rank, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_rank, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_rank, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per Rank ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_qps_rank.png", bbox_inches="tight")
plt.close()

fig, ax = plt.subplots()
plt.plot(scaling_N3.qps_per_device, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(scaling_N5.qps_per_device, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(scaling_N7.qps_per_device, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(scaling_N9.qps_per_device, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel(rf"Quadrature Points per {device} ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_qps_{device}.png", bbox_inches="tight")
plt.close()
