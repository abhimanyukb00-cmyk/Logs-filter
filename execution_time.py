import time

class LogsTimer:
    def __init__(self, name: str="Logs processing execution timer"):
        self.name = name
        self.elapsed_time: float = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.perf_counter() - self.start_time
        print(f"\nCode block {self.name} executed in {self.elapsed_time:.4f} seconds")