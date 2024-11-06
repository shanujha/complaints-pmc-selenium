import json

def update_peth_type(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Update the Peth values and add pethType accordingly
    for obj in data:
        if 'showPeth' in obj:
            if obj['showPeth'] == 'BldgPer-Peth':
                obj['showPeth'] = True
                obj['pethType'] = 'BUILDING_PERMISSION_PETH'
            elif obj['showPeth'] == 'Ptax-Peth':
                obj['showPeth'] = True
                obj['pethType'] = 'PROPERTY_TAX_PETH'
            elif obj['showPeth'] == 'Y':
                obj['showPeth'] = True
                obj['pethType'] = 'NORMAL'
            else: 
                obj['showPeth'] = False
                obj['pethType'] = 'NONE'


    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Peth values in {json_file} have been updated and saved to {output_file}")

# Example usage
# update_peth_type('input.json', 'output.json')
