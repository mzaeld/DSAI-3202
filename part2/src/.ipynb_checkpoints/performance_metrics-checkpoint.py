def compute_performance(T1, Tp, p=4, f=None):
    if f is None:
        f = 1 - (1 / (T1 / Tp))  # Calculate parallelizable fraction

    speedup = T1 / Tp
    efficiency = speedup / p
    amdahl_speedup = 1 / ((1 - f) + (f / p))
    gustafson_speedup = p - (p - 1) * (1 - f)
    
    return {
        "speedup": speedup,
        "efficiency": efficiency,
        "amdahl_speedup": amdahl_speedup,
        "gustafson_speedup": gustafson_speedup
    }
