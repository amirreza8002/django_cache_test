from time import perf_counter_ns

from django.core.cache import cache

from django_project.settings import cache as new_cache


N = 10000


def test_getsetdel():
    print(f"\nrunning {N} rounds of cache calls for both stable and experimental cache")
    old_start_time = perf_counter_ns()
    for _ in range(N):
        cache.set("hi", 1)
        cache.get("hi")
        cache.delete("hi")

    old_total_time = perf_counter_ns() - old_start_time
    cache.clear()

    new_start_time = perf_counter_ns()
    for _ in range(N):
        new_cache.set("hi", 1)
        new_cache.get("hi")
        new_cache.delete("hi")

    new_total_time = perf_counter_ns() - new_start_time
    new_cache.clear()

    print("\n\033[96mcache times:\033[0m")
    print(f"total time: \033[92m{old_total_time}\033[0m ns")
    print(f"avg time:   \033[92m{old_total_time / N}\033[0m ns per call")

    print("\n\033[96mexperimental cache times:\033[0m")
    print(f"total time: \033[92m{new_total_time}\033[0m ns")
    print(f"avg time:   \033[92m{new_total_time / N}\033[0m ns per call")

    print(
        f"\ndiff: \033[94m{(old_total_time / N) - (new_total_time / N)}\033[0m ns per call on avg"
    )

    assert old_total_time > new_total_time
