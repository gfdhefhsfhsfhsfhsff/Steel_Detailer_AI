"""
Utility functions and progress tracking
Author: John May
Version: 1.0.0-alpha
"""

import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class ProgressInfo:
    """Progress tracking information"""

    current: int
    total: int
    percent: float
    elapsed_seconds: float
    estimated_remaining: float
    phase: str


class ProgressTracker:
    """Tracks progress with time estimation"""

    def __init__(self, total_steps: int):
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        self.phase_times: Dict[str, float] = {}

    def start_phase(self, name: str) -> None:
        """Mark the start of a phase"""
        self.phase_times[name] = time.time()

    def advance(self, step_name: str = None) -> ProgressInfo:
        """Advance progress and return current status"""
        self.current_step += 1
        now = time.time()
        elapsed = now - self.start_time

        if step_name:
            self.phase_times[step_name] = now

        remaining = self.total_steps - self.current_step
        if self.current_step > 0:
            avg_time = elapsed / self.current_step
            estimated = avg_time * remaining
        else:
            estimated = 0

        return ProgressInfo(
            current=self.current_step,
            total=self.total_steps,
            percent=round((self.current_step / self.total_steps) * 100, 1),
            elapsed_seconds=elapsed,
            estimated_remaining=estimated,
            phase=step_name or "",
        )

    def format_time(self, seconds: float) -> str:
        """Format seconds into readable string"""
        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            secs = int(seconds % 60)
            return f"{minutes}m {secs}s"
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"

    def print_status(self, message: str) -> None:
        """Print current progress status"""
        info = self.advance()
        elapsed_str = self.format_time(info.elapsed_seconds)
        remaining_str = self.format_time(info.estimated_remaining)
        print(
            f"[{info.current}/{info.total}] {elapsed_str} elapsed, ~{remaining_str} remaining - {message}"
        )
