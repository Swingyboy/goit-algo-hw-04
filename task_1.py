import argparse
import pandas as pd
from task_utils.perform_tests import run_tests
from task_utils.report_generator import generate_html_report, save_html_report, open_html_report_in_browser


def main(start: int = 1000, stop: int = 10001, step: int = 1000, runs_number: int = 3):
    arrays_types = ['Reversed', 'Unsorted', 'Sorted']
    res = pd.DataFrame(columns=['Algorithm', 'Array Type', 'Array Size', 'Time'])
    result = run_tests(res, arrays_types, runs_number=runs_number, start=start, stop=stop, step=step)
    html_content = generate_html_report(result,
                                        runs_number=runs_number,
                                        start=start,
                                        stop=stop,
                                        step=step
                                        )
    save_html_report(html_content)
    open_html_report_in_browser()


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--min-size", type=int, default=1000)
    args.add_argument("--max-size", type=int, default=10001)
    args.add_argument("--step", type=int, default=1000)
    args.add_argument("--runs", type=int, default=3)

    start = args.parse_args().min_size
    stop = args.parse_args().max_size
    step = args.parse_args().step
    runs_number = args.parse_args().runs

    main(start=start, stop=stop, step=step, runs_number=runs_number)
