from quantizer import map_to_scalar_bin
from density import TelemetryDensityEstimator

if __name__ == "__main__":
    print("📊 Activating LinearHash-Quantile Continuous Stream Monitor...\n")

    estimator = TelemetryDensityEstimator()
    
    # Simulate a stream of steady motor temperature readings around 24.0°C-25.0°C
    raw_stream = [24.2, 24.4, 24.1, 25.8, 24.3, 24.2]
    
    for reading in raw_stream:
        bin_id = map_to_scalar_bin(reading)
        estimator.capture_stream(bin_id)

    target_test_reading = 24.2
    target_bin = map_to_scalar_bin(target_test_reading)
    density_probability = estimator.compute_likelihood(target_bin)

    print(f"📥 Processed Stream Samples: {raw_stream}")
    print(f"🔍 Analyzing Target Value: {target_test_reading}°C (Quantized Bin: {target_bin})")
    print(f"🔮 Estimated Operational Density Likelihood: {density_probability * 100:.1f}%")
