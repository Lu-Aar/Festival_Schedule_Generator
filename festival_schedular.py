import os
import sys
import argparse
import csv
import tkinter as tk
from tkinter import ttk
from typing import List


def _get_schedule_data(csv_file: str) -> List[dict]:
    """Retrieving the to be scheduled data from the file

    Args:
        csv_file (str): The path to the file

    Returns:
        List[dict]: A list of dicts with all data
    """
    schedule_data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            schedule_data.append({
                'show': row['show'],
                'start': int(row['start'], 0),
                'end': int(row['end'], 0)
            })

    return schedule_data


def _sort_on_start_time(schedule_data: List[dict]) -> List[dict]:
    """Sorting all data on start time

    Args:
        schedule_data (List[dict]): The list of shows

    Returns:
        List[dict]: A sorted list with all shows
    """
    return sorted(schedule_data, key=lambda x: x['start'])


def _stage_divider(schedule_data: List[dict]) -> List[List[dict]]:
    """Dividing the bands over different stages
       in order to give all a chance to perform

    Args:
        schedule_data (List[dict]): A sorted list with all shows

    Returns:
        List[List[dict]]: The schedule for each stage
    """
    stages_schedules = [[schedule_data[0]]]
    num_of_stages = 1

    for ii in range(1, len(schedule_data)):
        for jj in range(num_of_stages):
            if schedule_data[ii]['start'] >= stages_schedules[jj][-1]['end']:
                stages_schedules[jj].append(schedule_data[ii])
                break
            else:
                if jj == num_of_stages - 1:
                    stages_schedules.append([schedule_data[ii]])
                    num_of_stages += 1
                    break
    return stages_schedules


def _print_in_window(schedule: List[List[dict]]) -> None:
    """Giving a nice overview of the schedule for each stage

    Args:
        schedule (List[List[dict]]): The shows divided for each stage
    """
    root = tk.Tk()
    root.title("Show Tables")

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    max_columns = 4
    for i, sublist in enumerate(schedule):
        row = i // max_columns
        col = i % max_columns

        frame = tk.LabelFrame(
            container, text=f"Stage {i+1}", width=200, height=200)
        frame.grid(row=row, column=col, padx=10, pady=10)
        frame.pack_propagate(False)

        tree = ttk.Treeview(frame, columns=(
            "Show", "Start", "End"), show="headings", height=6)
        tree.heading("Show", text="Show")
        tree.heading("Start", text="Start")
        tree.heading("End", text="End")

        tree.column("Show", width=80, anchor="center")
        tree.column("Start", width=50, anchor="center")
        tree.column("End", width=50, anchor="center")

        for item in sublist:
            tree.insert("", "end", values=(
                item["show"], item["start"], item["end"]))

        tree.pack(expand=True, fill="both")

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Festival Schedule Generator")
    parser.add_argument('--input', type=str, required=True,
                        help="Input CSV file with the schedule data")

    args = parser.parse_args()
    csv_file = args.input

    if not os.path.exists(csv_file):
        print(f"Error: the file {csv_file} does not exist.")
        return 1

    schedule_data = _get_schedule_data(csv_file)
    sorted_schedule_data = _sort_on_start_time(schedule_data)
    stage_divided_schedule = _stage_divider(sorted_schedule_data)
    _print_in_window(stage_divided_schedule)

    return 0


if __name__ == "__main__":
    sys.exit(main())
