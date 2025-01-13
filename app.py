import zipfile
import os
import chardet

# Function to read CSV or text files and process the symbol-value pairs
def process_file(file_path, encoding, delimiter=','):
    total_sum = 0
    with open(file_path, mode='r', encoding=encoding) as file:
        # Read each line in the file
        for line in file:
            # Print the raw line to inspect the data
            print(f"Raw line: {repr(line)}")
            # Split the line based on the delimiter (comma for CSV, tab for TXT)
            parts = line.strip().split(delimiter)
            if len(parts) != 2:
                continue  # Skip lines that don't have exactly two parts
            symbol, value = parts[0], parts[1]
            
            # Print symbols and values to inspect the correct characters
            print(f"Symbol: {repr(symbol)}, Value: {repr(value)}")
            
            try:
                value = float(value)  # Convert value to a float
            except ValueError:
                continue  # Skip lines where the value isn't a valid number
            
            # Check if the symbol matches ’ or ˆ (handling Unicode correctly)
            if symbol == '’' or symbol == 'ˆ':
                total_sum += value
    return total_sum

# Function to detect encoding using chardet
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

# Extract files from the ZIP archive
zip_file = 'q-unicode-data.zip'
output_dir = 'data_files'
os.makedirs(output_dir, exist_ok=True)

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

# File paths
file1 = os.path.join(output_dir, 'data1.csv')
file2 = os.path.join(output_dir, 'data2.csv')
file3 = os.path.join(output_dir, 'data3.txt')

# Detect encoding for each file using chardet
encoding1 = detect_encoding(file1)
encoding2 = detect_encoding(file2)
encoding3 = detect_encoding(file3)

print(f"Detected encoding for data1.csv: {encoding1}")
print(f"Detected encoding for data2.csv: {encoding2}")
print(f"Detected encoding for data3.txt: {encoding3}")

# Process the files with the detected encodings and delimiters
sum_data1 = process_file(file1, encoding1, delimiter=',')  # CSV, detected encoding for data1.csv
sum_data2 = process_file(file2, encoding2, delimiter=',')   # CSV, detected encoding for data2.csv
sum_data3 = process_file(file3, encoding3, delimiter='\t')  # Tab-separated, detected encoding for data3.txt

# Total sum across all files
total_sum = sum_data1 + sum_data2 + sum_data3

print(f"Sum of values for symbols ’ and ˆ: {total_sum}")
