"""
Utility functions and helpers for SDS/2 API
"""

import time
from typing import Dict, List, Any, Set, Tuple


class ProgressTracker:
    def __init__(self, total_steps: int):
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        self.phase_times: Dict[str, float] = {}

    def start_phase(self, name: str) -> None:
        self.phase_times[name] = time.time()

    def advance(self, step_name: str = None) -> float:
        self.current_step += 1
        now = time.time()
        if step_name:
            self.phase_times[step_name] = now
        elapsed = now - self.start_time
        completed = self.current_step
        if self.current_step == 0:
            return 0.0

        avg_time = elapsed / self.current_step
        remaining = self.total_steps - self.current_step
        estimated = avg_time * remaining
        return {
            "current": self.current_step,
            "total": self.total_steps,
            "percent": min((self.current_step / self.total_steps) * 100, 1),
            "elapsed": elapsed,
            "estimated_remaining": estimated,
            "phase": step_name,
        }

    def format_time(self, seconds: float) -> str:
        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            return f"{int(seconds / 60)}m {int(seconds % 60)}s"
        return f"{int(seconds / 3600)}h {int((seconds % 3600) // 60)}"

    def print_progress(self, message: str) -> None:
        elapsed = time.time() - self.start_time
        print(
            f"  [{self.current_step}/{self.total_steps}] {self.format_time(elapsed)} - {message}"
        )
        print(f"  Estimated time remaining: {self.format_time(estimated)}")
        if estimated > 0:
            print(
                f"  Progress: {self.current_step / self.total_steps * 100:.0%} complete"
            )
