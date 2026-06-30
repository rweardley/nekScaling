import numpy as np

class StrongScalingCase:
    def __init__(self, ranks_list, ranks_per_gpu, files_list, elements, polynomialorder, timestep_range):
        self.files_list = files_list
        self.elements = elements
        self.polynomialorder = polynomialorder
        self.time_per_timestep = []
        self.speedup = []
        self.ideal_speedup = []
        self.parallel_efficiency = []
        self.qps = polynomialorder**3 * elements
        self.ranks_list = ranks_list
        self.ranks_per_gpu = ranks_per_gpu
        self.qps_per_rank = [
            self.qps / rank for rank in self.ranks_list
        ]
        self.qps_per_gpu = [
            self.qps / (rank/ranks_per_gpu) for rank in self.ranks_list
        ]
        self.timestep_range = timestep_range

    def scaling_calculations(self):
        print(
            "Ranks\tGPUs\tQPs per rank\tQPs per GPU\tTime per timestep [s]\tSpeedup\tIdeal Speedup\tParallel Efficiency\tMean Iters (P, UVW)"
        )
        for i in range(len(self.ranks_list)):
            ranks = self.ranks_list[i]
            file = self.files_list[i]
            data = np.loadtxt(file, delimiter="\t", skiprows=1, usecols=range(7))
            time_per_timestep_column = 4
            time_per_timestep = data[self.timestep_range, time_per_timestep_column]
            mean_time_per_timestep = np.mean(time_per_timestep)
            if i == 0:
                reference_time = mean_time_per_timestep
                reference_ranks = ranks
            self.time_per_timestep.append(mean_time_per_timestep)
            speedup = reference_time / mean_time_per_timestep
            self.speedup.append(speedup)
            ideal_speedup = ranks / reference_ranks
            self.ideal_speedup.append(ideal_speedup)
            parallel_efficiency = (reference_time * reference_ranks) / (
                mean_time_per_timestep * ranks
            )
            self.parallel_efficiency.append(parallel_efficiency)
            print(
                f"{ranks}\t{ranks/self.ranks_per_gpu}"
                f"\t{self.qps_per_rank[i]:.2e}\t{self.qps_per_gpu[i]:.2e}"
                f"\t{mean_time_per_timestep:.3f}"
                f"\t\t\t{speedup:.3f}\t{ideal_speedup:.3f}"
                f"\t\t{parallel_efficiency:.3f}"
                f"\t\t\t{np.mean(data[self.timestep_range, 5]):.3f}"
                f"\t{np.mean(data[self.timestep_range, 6]):.3f}"
            )

class WeakScalingCases:
    def __init__(self, strong_scaling_cases):
        self.strong_scaling_cases = strong_scaling_cases
        polynomialorder = 0
        for case in self.strong_scaling_cases:
            if case.polynomialorder > polynomialorder:
                polynomialorder = case.polynomialorder
            else:
                raise Exception("WeakScalingCases: strong_scaling_cases must be in order of ascending polynomial order")

    def weak_scaling_calculations(self, qps_per_rank_lower, qps_per_rank_upper):
        print("\nFinding weak scaling set:")
        print(f"{qps_per_rank_lower:.2e} <= QPs per rank <= {qps_per_rank_upper:.2e}")
        ranks = []
        scaled_speedup = []
        reference_point = True

        for case in self.strong_scaling_cases:
            for i in range(len(case.ranks_list)):
                if qps_per_rank_lower <= case.qps_per_rank[i] <= qps_per_rank_upper:
                    if reference_point:
                        reference_time = case.time_per_timestep[i]
                        reference_qps = case.qps
                        reference_point = False
                        print(f"Found point: N={case.polynomialorder}, {case.ranks_list[i]} ranks\t<--- reference point")
                    else:
                        print(f"Found point: N={case.polynomialorder}, {case.ranks_list[i]} ranks")
                    ranks.append(case.ranks_list[i])
                    scaled_speedup.append((case.qps/reference_qps)*(reference_time/case.time_per_timestep[i]))

        return ranks, scaled_speedup
