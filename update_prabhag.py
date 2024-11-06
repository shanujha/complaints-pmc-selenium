import json

def update_prabhag_value(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Update the Peth values and add pethType accordingly
    for obj in data:
        if 'showPrabhag' in obj:
            if obj['showPrabhag'] == 'Prabhag':
                obj['showPrabhag'] = True
            else:
                obj['showPrabhag'] = False

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Prabhag values in {json_file} have been updated and saved to {output_file}")

# Example usage
# update_ward_value('input.json', 'output.json')
