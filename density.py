from linear_map import ProbingHashMap

class TelemetryDensityEstimator:
    def __init__(self):
        self.frequency_table = ProbingHashMap(capacity=37)
        self.total_samples = 0

    def capture_stream(self, bin_id):
        self.frequency_table.log_observation(bin_id)
        self.total_samples += 1

    def compute_likelihood(self, bin_id):
        seen_count = self.frequency_table.get_count(bin_id)
        if self.total_samples == 0: return 0.0
        return seen_count / self.total_samples
