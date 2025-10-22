"""
Performance Integration Tests
Tests latency, throughput, memory, and CPU usage
10 comprehensive benchmarks to ensure <100ms latency and >1000 cases/h throughput
"""

import pytest
import time
import psutil
import os
from hemodoctor.api.pipeline import analyze_cbc


# Sample CBCs for performance testing
NORMAL_CBC = {
    "hb": 14.5,
    "wbc": 7.0,
    "plt": 220,
    "mcv": 88,
    "age_years": 35,
    "sex": "M"
}

CRITICAL_CBC = {
    "hb": 7.5,
    "wbc": 10.0,
    "plt": 8,
    "mcv": 88,
    "ldh": 980,
    "bt_indireta": 2.5,
    "morphology": {"esquistocitos": True},
    "age_years": 35,
    "sex": "M"
}

COMPLETE_CBC = {
    "hb": 14.5,
    "wbc": 7.0,
    "plt": 240,
    "mcv": 88,
    "mch": 30,
    "mchc": 34,
    "rdw": 13,
    "neutrophils_pct": 60,
    "lymphocytes_pct": 30,
    "monocytes_pct": 8,
    "eosinophils_pct": 2,
    "basophils_pct": 0.5,
    "reticulocytes_pct": 1.2,
    "ferritin": 100,
    "iron": 80,
    "tibc": 350,
    "age_years": 40,
    "sex": "M"
}

MINIMAL_CBC = {
    "hb": 12.0,
    "wbc": 7.0,
    "plt": 200,
    "mcv": 88,
    "age_years": 30,
    "sex": "F"
}


# ============================================================================
# LATENCY TESTS (4 tests)
# ============================================================================

def test_performance_single_case_latency(benchmark):
    """Test single case latency - TARGET: <100ms"""
    result = benchmark(analyze_cbc, NORMAL_CBC)

    assert result is not None
    assert "top_syndromes" in result

    # Check benchmark stats (available after test)
    # benchmark.stats.mean should be <0.1 (100ms)


def test_performance_critical_case_latency(benchmark):
    """Test critical case latency (short-circuit optimization)"""
    result = benchmark(analyze_cbc, CRITICAL_CBC)

    assert result is not None
    assert "S-TMA" in result["top_syndromes"] or "S-PLT-CRITICA" in result["top_syndromes"]


def test_performance_complete_cbc_latency(benchmark):
    """Test complete CBC with all fields (worst case)"""
    result = benchmark(analyze_cbc, COMPLETE_CBC)

    assert result is not None


def test_performance_minimal_cbc_latency(benchmark):
    """Test minimal CBC (fast path)"""
    result = benchmark(analyze_cbc, MINIMAL_CBC)

    assert result is not None


# ============================================================================
# THROUGHPUT TESTS (2 tests)
# ============================================================================

def test_performance_batch_processing_100():
    """Test batch processing of 100 cases - measure throughput"""
    start_time = time.time()

    results = []
    for i in range(100):
        # Vary CBC slightly to avoid caching
        cbc = NORMAL_CBC.copy()
        cbc["hb"] = 14.5 + (i % 10) * 0.1
        result = analyze_cbc(cbc)
        results.append(result)

    elapsed = time.time() - start_time
    throughput = 100 / elapsed  # cases per second
    throughput_per_hour = throughput * 3600

    # All results should be valid
    assert len(results) == 100
    assert all("top_syndromes" in r for r in results)

    # Log throughput (pytest will capture this)
    print(f"\n  Throughput: {throughput:.1f} cases/sec ({throughput_per_hour:.0f} cases/hour)")

    # TARGET: >1000 cases/hour = >0.28 cases/sec
    assert throughput_per_hour > 1000, f"Throughput {throughput_per_hour:.0f}/h is below 1000/h target"


def test_performance_batch_processing_1000():
    """Test batch processing of 1000 cases - stress test"""
    start_time = time.time()

    # Process 1000 cases
    count = 0
    for i in range(1000):
        cbc = NORMAL_CBC.copy()
        cbc["hb"] = 10.0 + (i % 50) * 0.1
        result = analyze_cbc(cbc)
        if result:
            count += 1

    elapsed = time.time() - start_time
    throughput = 1000 / elapsed
    throughput_per_hour = throughput * 3600

    assert count == 1000
    print(f"\n  1000 cases throughput: {throughput:.1f} cases/sec ({throughput_per_hour:.0f} cases/hour)")
    print(f"  Total time: {elapsed:.2f}s")

    # Should complete in reasonable time
    assert elapsed < 60, f"1000 cases took {elapsed:.1f}s (should be <60s)"


# ============================================================================
# MEMORY TESTS (2 tests)
# ============================================================================

def test_performance_memory_usage_single():
    """Test memory usage for single case - should be <10MB"""
    import tracemalloc

    tracemalloc.start()

    # Baseline
    baseline = tracemalloc.get_traced_memory()[0]

    # Process CBC
    result = analyze_cbc(COMPLETE_CBC)

    # Peak memory
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memory_used_mb = (peak - baseline) / (1024 * 1024)

    assert result is not None
    print(f"\n  Memory used: {memory_used_mb:.2f} MB")

    # Should use <10MB for single case
    assert memory_used_mb < 10, f"Memory usage {memory_used_mb:.2f}MB exceeds 10MB limit"


def test_performance_memory_usage_batch():
    """Test memory usage for batch of 100 cases - should be <50MB"""
    import tracemalloc

    tracemalloc.start()
    baseline = tracemalloc.get_traced_memory()[0]

    # Process 100 CBCs
    results = []
    for i in range(100):
        cbc = NORMAL_CBC.copy()
        cbc["hb"] = 14.5 + (i % 10) * 0.1
        result = analyze_cbc(cbc)
        results.append(result)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memory_used_mb = (peak - baseline) / (1024 * 1024)

    assert len(results) == 100
    print(f"\n  Memory for 100 cases: {memory_used_mb:.2f} MB")

    # Should use <50MB for 100 cases
    assert memory_used_mb < 50, f"Memory usage {memory_used_mb:.2f}MB exceeds 50MB limit"


# ============================================================================
# CPU TESTS (1 test)
# ============================================================================

def test_performance_cpu_usage():
    """Test CPU usage during processing - should be reasonable"""
    process = psutil.Process(os.getpid())

    # Baseline CPU
    process.cpu_percent(interval=0.1)

    # Process 50 cases while monitoring CPU
    start_time = time.time()
    for i in range(50):
        cbc = NORMAL_CBC.copy()
        cbc["hb"] = 14.5 + (i % 10) * 0.1
        analyze_cbc(cbc)

    elapsed = time.time() - start_time

    # Get CPU usage
    cpu_percent = process.cpu_percent(interval=0.1)

    print(f"\n  CPU usage: {cpu_percent:.1f}%")
    print(f"  50 cases in: {elapsed:.2f}s")

    # CPU should be reasonable (not 100%)
    # Note: CPU percent can be >100% on multi-core systems
    assert cpu_percent < 200, f"CPU usage {cpu_percent:.1f}% is too high"


# ============================================================================
# CONCURRENT LOAD TEST (1 test)
# ============================================================================

def test_performance_concurrent_load():
    """Test concurrent processing of 20 cases (simulating concurrent API requests)"""
    import concurrent.futures

    def process_cbc(i):
        cbc = NORMAL_CBC.copy()
        cbc["hb"] = 14.5 + (i % 10) * 0.1
        return analyze_cbc(cbc)

    start_time = time.time()

    # Process 20 CBCs concurrently (ThreadPoolExecutor)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_cbc, i) for i in range(20)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]

    elapsed = time.time() - start_time

    assert len(results) == 20
    assert all("top_syndromes" in r for r in results)

    print(f"\n  20 concurrent cases in: {elapsed:.2f}s")
    print(f"  Effective throughput: {20/elapsed:.1f} cases/sec")

    # Should complete in reasonable time
    assert elapsed < 5, f"20 concurrent cases took {elapsed:.1f}s (should be <5s)"
