import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("../")
from scaling import StrongScalingCase
from scaling import WeakScalingCases

savedir = "scaling_plots/run3"
casedir = "run3"

timestep_range = slice(100, 2000)
lelg = 54000  # number of elements in .re2 mesh

ranks_N1 = [8, 12, 16]
files_N1 = [str(rank)+"_ranks/"+casedir+"/N_1.tsv" for rank in ranks_N1]
scaling_N1 = StrongScalingCase(ranks_N1, 8, files_N1, lelg, 1, timestep_range)
print(f"\nN=1")
scaling_N1.scaling_calculations()

ranks_N2 = [8, 12, 16]
files_N2 = [str(rank)+"_ranks/"+casedir+"/N_2.tsv" for rank in ranks_N2]
scaling_N2 = StrongScalingCase(ranks_N2, 8, files_N2, lelg, 2, timestep_range)
print(f"\nN=2")
scaling_N2.scaling_calculations()

ranks_N3 = [8, 12, 16, 24, 32, 40, 48]
files_N3 = [str(rank)+"_ranks/"+casedir+"/N_3.tsv" for rank in ranks_N3]
scaling_N3 = StrongScalingCase(ranks_N3, 8, files_N3, lelg, 3, timestep_range)
print(f"\nN=3")
scaling_N3.scaling_calculations()

# ranks_N4 = [8, 12, 16, 24, 32, 40, 48]
ranks_N4 = [8, 12, 16, 24, 40, 48]
files_N4 = [str(rank)+"_ranks/"+casedir+"/N_4.tsv" for rank in ranks_N4]
scaling_N4 = StrongScalingCase(ranks_N4, 8, files_N4, lelg, 4, timestep_range)
print(f"\nN=4")
scaling_N4.scaling_calculations()

# ranks_N5 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
ranks_N5 = [8, 12, 16, 24, 40, 48, 56, 64, 128]
files_N5 = [str(rank)+"_ranks/"+casedir+"/N_5.tsv" for rank in ranks_N5]
scaling_N5 = StrongScalingCase(ranks_N5, 8, files_N5, lelg, 5, timestep_range)
print(f"\nN=5")
scaling_N5.scaling_calculations()

ranks_N6 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
# ranks_N6 = [16, 24, 32, 40, 48, 56, 64, 128] # to align with SPX cases
files_N6 = [str(rank)+"_ranks/"+casedir+"/N_6.tsv" for rank in ranks_N6]
scaling_N6 = StrongScalingCase(ranks_N6, 8, files_N6, lelg, 6, timestep_range)
print(f"\nN=6")
scaling_N6.scaling_calculations()

ranks_N7 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
# ranks_N7 = [16, 24, 32, 40, 48, 56, 64, 128] # to align with SPX cases
files_N7 = [str(rank)+"_ranks/"+casedir+"/N_7.tsv" for rank in ranks_N7]
scaling_N7 = StrongScalingCase(ranks_N7, 8, files_N7, lelg, 7, timestep_range)
print(f"\nN=7")
scaling_N7.scaling_calculations()

ranks_N8 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
# ranks_N8 = [32, 40, 48, 56, 64, 128] # to align with SPX cases
files_N8 = [str(rank)+"_ranks/"+casedir+"/N_8.tsv" for rank in ranks_N8]
scaling_N8 = StrongScalingCase(ranks_N8, 8, files_N8, lelg, 8, timestep_range)
print(f"\nN=8")
scaling_N8.scaling_calculations()

ranks_N9 = [8, 12, 16, 24, 32, 40, 48, 56, 64, 128]
# ranks_N9 = [32, 40, 48, 56, 64, 128] # to align with SPX cases
files_N9 = [str(rank)+"_ranks/"+casedir+"/N_9.tsv" for rank in ranks_N9]
scaling_N9 = StrongScalingCase(ranks_N9, 8, files_N9, lelg, 9, timestep_range)
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
plt.plot(scaling_N3.qps_per_gpu, scaling_N3.time_per_timestep, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_gpu, scaling_N4.time_per_timestep, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_gpu, scaling_N5.time_per_timestep, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_gpu, scaling_N6.time_per_timestep, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_gpu, scaling_N7.time_per_timestep, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_gpu, scaling_N8.time_per_timestep, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_gpu, scaling_N9.time_per_timestep, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Walltime per timestep [s]")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/time_per_timestep_qps_gpu.png", bbox_inches="tight")
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
plt.plot(scaling_N3.qps_per_gpu, scaling_N3.speedup, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_gpu, scaling_N4.speedup, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_gpu, scaling_N5.speedup, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_gpu, scaling_N6.speedup, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_gpu, scaling_N7.speedup, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_gpu, scaling_N8.speedup, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_gpu, scaling_N9.speedup, "x-", label=r"$N=9$")
plt.plot(scaling_N3.qps_per_gpu, scaling_N3.ideal_speedup, "k--", label=r"Ideal")
plt.plot(scaling_N4.qps_per_gpu, scaling_N4.ideal_speedup, "k--")
plt.plot(scaling_N5.qps_per_gpu, scaling_N5.ideal_speedup, "k--")
plt.plot(scaling_N6.qps_per_gpu, scaling_N6.ideal_speedup, "k--")
plt.plot(scaling_N7.qps_per_gpu, scaling_N7.ideal_speedup, "k--")
plt.plot(scaling_N8.qps_per_gpu, scaling_N8.ideal_speedup, "k--")
plt.plot(scaling_N9.qps_per_gpu, scaling_N9.ideal_speedup, "k--")
plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Speedup")
plt.ylim(0, 5)
plt.legend(frameon=False)
plt.savefig(f"{savedir}/speedup_qps_gpu.png", bbox_inches="tight")
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
plt.plot(scaling_N3.qps_per_gpu, scaling_N3.parallel_efficiency, "x-", label=r"$N=3$")
plt.plot(scaling_N4.qps_per_gpu, scaling_N4.parallel_efficiency, "x-", label=r"$N=4$")
plt.plot(scaling_N5.qps_per_gpu, scaling_N5.parallel_efficiency, "x-", label=r"$N=5$")
plt.plot(scaling_N6.qps_per_gpu, scaling_N6.parallel_efficiency, "x-", label=r"$N=6$")
plt.plot(scaling_N7.qps_per_gpu, scaling_N7.parallel_efficiency, "x-", label=r"$N=7$")
plt.plot(scaling_N8.qps_per_gpu, scaling_N8.parallel_efficiency, "x-", label=r"$N=8$")
plt.plot(scaling_N9.qps_per_gpu, scaling_N9.parallel_efficiency, "x-", label=r"$N=9$")
plt.xlabel(r"Quadrature Points per GPU ($n=EN^3$)")
plt.gca().invert_xaxis()
plt.ylabel("Parallel Efficiency")
plt.legend(frameon=False)
plt.savefig(f"{savedir}/efficiency_qps_gpu.png", bbox_inches="tight")
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
