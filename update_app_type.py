import json

def add_app_type(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Update the Peth values and add pethType accordingly
    for obj in data:
        if 'startCode' in obj:
            obj['applicationType'] = obj['startCode']

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Application Type values in {json_file} have been updated and saved to {output_file}")

# Example usage
# update_ward_value('input.json', 'output.json')
