"""Measure the execution time of a callable."""
import time


def running_2000(function, *args, **kwargs):
    """Call function once and return elapsed seconds; propagate its exceptions.

    Lazy return values such as zip objects are not consumed.
    """
    start = time.perf_counter()
    function(*args, **kwargs)
    return time.perf_counter() - start


timer = running_2000


if __name__ == "__main__":
    print(timer(print, "Hello"))
