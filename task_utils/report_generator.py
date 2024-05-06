import jinja2
import seaborn as sns
import pandas as pd


def color_negative_red(val):
    color = 'red' if val else 'black'
    return f'color: {color}'


def generate_html_report(df, runs_number, start, stop, step):
    # Styling
    styler = df.style.applymap(color_negative_red)

    # Aggregation
    avg_time = df.groupby(["Array Type", "Array Size", "Algorithm"])["Time"].mean().reset_index()
    avg_time.sort_values(by=["Array Type", "Array Size", "Algorithm"], inplace=True)
    algorithm_list = avg_time["Algorithm"].unique().tolist()
    array_types = avg_time["Array Type"].unique().tolist()

    # Find algorithm with maximum time
    max_time_index = avg_time["Time"].idxmax()
    algorithm_max_time = avg_time.loc[max_time_index, "Algorithm"]

    # Find algorithm with minimum time
    min_time_index = avg_time["Time"].idxmin()
    algorithm_min_time = avg_time.loc[min_time_index, "Algorithm"]

    # Template handling
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('./task_utils/template.html')
    html_content = template.render(my_table=avg_time.to_html(index=False),
                                   algorithms=algorithm_list,
                                   array_types=array_types,
                                   runs_number=runs_number,
                                   max_size=stop,
                                   min_size=start,
                                   step=step,
                                   best_algorithm=algorithm_min_time,
                                   worst_algorithm=algorithm_max_time,
                                   )

    # Plot
    plot = sns.relplot(x="Array Size", y="Time", hue="Algorithm", col="Array Type", kind="line", data=avg_time)
    plot.savefig('plot.svg')
    return html_content


def save_html_report(html_content, filename='report.html'):
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"HTML report saved as '{filename}'")


def open_html_report_in_browser(filename='report.html'):
    import webbrowser
    webbrowser.open_new_tab(filename)
