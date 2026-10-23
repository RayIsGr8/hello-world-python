from pathlib import Path


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)


def process_data(data):
    # Example processing: convert text to uppercase
    return data.upper()


def main():
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / 'input.txt'
    output_path = base_dir / 'output.txt'

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    # Read from the input file
    data = read_file(input_path)

    # Process the data
    processed_data = process_data(data)

    # Write to the output file
    write_file(output_path, processed_data)


if __name__ == "__main__":
    main()