from rich.console import Console
import time
import sys
console = Console()
def progress_bar(iteration, total, color):
    bar_max_width = 70 #45
    bar_current_width = bar_max_width * iteration // total
    bar = "█" * bar_current_width + "-" * (bar_max_width - bar_current_width)
    progress = "%.1f" % (iteration / total * 100)
    console.print(f"|{bar}| {progress} %", end="\r", style=color)
    if iteration == total:
        print()

