import csv
import json
from collections import defaultdict

# Function to process the CSV data and convert it to JSON
def convert_csv_to_json(csv_file_path, json_file_path):
    # Read the CSV data
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        dictionary_data = defaultdict(dict)

        # Process each row in the CSV
        for row in reader:
            word_key = row['word']
            edition_key = row['edition']
            description = row['description'].replace('~', word_key)  # Replace '~' with the word
            phonetic = row['phonetic']
            jawi = row['jawi']

            # Store phonetic and jawi for each word
            if word_key not in dictionary_data:
                dictionary_data[word_key]['phonetic'] = phonetic
                dictionary_data[word_key]['jawi'] = jawi
                dictionary_data[word_key]['editions'] = defaultdict(list)

            # Group descriptions by edition
            dictionary_data[word_key]['editions'][edition_key].append(description)

        # Convert the grouped data into the desired JSON format
        json_data = []
        for word, data in dictionary_data.items():
            phonetic = data['phonetic']
            jawi = data['jawi']
            outputs = []
            for edition, descriptions in data['editions'].items():
                # Join all descriptions for the same edition with ' atau '
                combined_descriptions = ' atau '.join(descriptions)
                outputs.append(f'Menurut {edition}, "{word}" {phonetic} atau {jawi} bermaksud {combined_descriptions}')
            
            # Modify the entry as you like
            entry = {
                'instruction': f'apa erti perkataan {word}?',
                'input': '',
                'output': "\n\n".join(outputs)
            }
            json_data.append(entry)

        # Append the new data to the existing JSON file
        try:
            with open(json_file_path, 'r+', encoding='utf-8') as jsonfile:
                # Load existing data
                existing_data = json.load(jsonfile)
                # Append new data
                existing_data.extend(json_data)
                # Move the cursor to the beginning of the file
                jsonfile.seek(0)
                # Write the updated data
                json.dump(existing_data, jsonfile, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            print(f'File {json_file_path} not found. Creating a new file.')
            with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(json_data, jsonfile, indent=2, ensure_ascii=False)

# Replace 'cleaned_V3_filled.csv' with the path to your CSV file
csv_file_path = 'cleaned_V3_filled.csv'
json_file_path = 'alpaca_dataV4.json'
convert_csv_to_json(csv_file_path, json_file_path)

print(f'The updated JSON data has been saved to {json_file_path}')
