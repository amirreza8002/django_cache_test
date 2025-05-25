from time import perf_counter_ns

from django.core.cache import cache

from django_project.settings import cache as new_cache


N = 10000

old_total_time = 0
new_total_time = 0


def test_getsetdel_old():
    global old_total_time
    print(f"\n\033[35mrunning {N} rounds of cache calls for stable cache\033[0m")
    old_start_time = perf_counter_ns()
    for _ in range(N):
        cache.set("hi", 1)
        cache.get("hi")
        cache.delete("hi")

    old_total_time = perf_counter_ns() - old_start_time
    cache.clear()
    print("\n\033[96mcache times:\033[0m")
    print(f"total time: \033[92m{old_total_time}\033[0m ns")
    print(f"avg time:   \033[92m{old_total_time / N}\033[0m ns per call")


def test_getsetdel_new():
    print(
        f"\n\n\033[35mrunning {N} rounds of cache calls for experimental cache\033[0m"
    )
    global new_total_time
    new_start_time = perf_counter_ns()
    for _ in range(N):
        new_cache.set("hi", 1)
        new_cache.get("hi")
        new_cache.delete("hi")

    new_total_time = perf_counter_ns() - new_start_time
    new_cache.clear()

    print("\n\033[96mexperimental cache times:\033[0m")
    print(f"total time: \033[92m{new_total_time}\033[0m ns")
    print(f"avg time:   \033[92m{new_total_time / N}\033[0m ns per call")

    print(
        f"\ndiff: \033[94m{(old_total_time / N) - (new_total_time / N)}\033[0m ns per call on avg"
    )

    assert old_total_time > new_total_time
