import csv

# Path to your input file
input_file_path = "/Users/ericu950/Documents/GitHub/tragic macronizer/1_Tragedies_tagged.txt"

# Path for the output file
output_file_path = "/Users/ericu950/Documents/GitHub/tragic macronizer/1_Tragedies_tagged_sorted.txt"

# Read the file and store the data
with open(input_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    data = list(reader)

# Reorder the columns (POS, Lemma, Tag, Token)
data_reordered = [(row[0], row[3], row[2], row[1]) for row in data if len(row) >= 4]

# Sort by POS (column 1), then Lemma (column 2), then Tag (column 3), then Token (column 4)
data_sorted = sorted(data_reordered, key=lambda x: (x[0], x[1], x[2], x[3]))

# Remove duplicates
seen = set()
data_unique = []
for row in data_sorted:
    if row not in seen:
        seen.add(row)
        data_unique.append(row)

# Write the processed data to a new file
with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='\t')
    for row in data_unique:
        writer.writerow(row)

print("File processed and saved as:", output_file_path)
