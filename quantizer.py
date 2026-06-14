def map_to_scalar_bin(sensor_reading, grid_resolution=0.5):
    """Normalizes raw decimal readings into scaled integer buckets."""
    return int(sensor_reading // grid_resolution)
