# Algorithm Performance Analysis

This script is designed to analyze the performance of sorting algorithms under different scenarios such as array types (reversed, unsorted, sorted) and array sizes. It generates a report detailing the time taken by each algorithm for various configurations.

## Requirements

- Python 3.x
- Pandas
- argparse

## Usage

1. Clone the repository:

    ```bash
    git clone git@github.com:Swingyboy/goit-algo-hw-04.git
    ```

2. Navigate to the directory:

    ```bash
    cd homework_04
    ```
3. Install the required packages:

    ```bash
    pip install -r requirements.txt
   ```

4. Run the script with optional arguments:

    ```bash
    python task_1.py --min-size 1000 --max-size 10001 --step 1000 --runs 3
    ```

    Optional arguments:
    - `--min-size`: Minimum array size (default: 1000)
    - `--max-size`: Maximum array size (default: 10001)
    - `--step`: Step size for increasing array size (default: 1000)
    - `--runs`: Number of runs for each configuration (default: 3)

## Output

The script generates an HTML report (`report.html`) which provides a detailed analysis of algorithm performance for different array types and sizes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

