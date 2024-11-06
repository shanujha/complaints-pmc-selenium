import json

def update_ward_value(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Update the Peth values and add pethType accordingly
    for obj in data:
        if 'showWard' in obj:
            if obj['showWard'] == 'WO':
                obj['showWard'] = True
                obj['showInWard'] = 'WARD_OFFICE_LIST'
            elif obj['showWard'] == 'HO':
                obj['showInWard'] = True
                obj['showWard'] = 'HEAD_OFFICE_ONLY'
            else:
                obj['showWard'] = False

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Ward values in {json_file} have been updated and saved to {output_file}")

# Example usage
# update_ward_value('input.json', 'output.json')
