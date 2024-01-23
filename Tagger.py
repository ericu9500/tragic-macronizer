import spacy
import csv
from tqdm import tqdm

# Load the Greek language model
nlp = spacy.load("grc_odycy_joint_trf")

# Path to your text file
file_path = "/Users/ericu950/Documents/GitHub/DionysiusRecomposed/Source2/Tragedies.txt"

# Open the file to read lines
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Open a file to write the output
with open('Tragedies_tagged.tsv', mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter='\t')
    
    # Write the header
    writer.writerow(["POS", "Token", "Tag", "Lemma"])

    # Process each line in the file
    for line in tqdm(lines):
        doc = nlp(line.strip())  # Strip to remove newline characters

        # Iterate through sentences and tokens
        for sent in doc.sents:
            for token in sent:
                # Write the token details to the file
                writer.writerow([token.pos_, token.text, token.tag_, token.lemma_])

print("Processing complete!")
