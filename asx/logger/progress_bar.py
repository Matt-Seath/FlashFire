import sys
import colorama

def bar(task, current, total, optional=" "):
    percentage_complete = round((current / total) * 100)
    bar_full = round(percentage_complete / 2)
    full_pixels = "=" * bar_full
    bar_empty = 50 - bar_full
    empty_pixels = " " * bar_empty
    if (current + 1) == total:
        print(f"{task}  (100% Completed)")
    else:
        print(f"  {task}  [{full_pixels}{empty_pixels}]   {current} of {total} ({percentage_complete}% Complete.) {optional}", end="\r")
    

def bar2(progress, total, color=colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%")
