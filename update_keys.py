import json

def update_key_in_json(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Function to recursively replace keys
    def replace_key(obj, old_key, new_key):
        if isinstance(obj, dict):
            new_obj = {}
            for k, v in obj.items():
                if k == old_key:
                    new_obj[new_key] = replace_key(v, old_key, new_key)
                else:
                    new_obj[k] = replace_key(v, old_key, new_key)
            return new_obj
        elif isinstance(obj, list):
            return [replace_key(item, old_key, new_key) for item in obj]
        else:
            return obj

    # Update the keys in the JSON data
    updated_data1 = replace_key(data, 'Ward', 'showWard')
    updated_data2 = replace_key(updated_data1, 'Prabhag', 'showPrabhag')
    updated_data3 = replace_key(updated_data2, 'Peth', 'showPeth')
    updated_data4 = replace_key(updated_data3, 'HeadOffice', 'showHeadOffice')

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(updated_data4, f, indent=4)

    print(f"Keys in {json_file} have been updated and saved to {output_file}")

# Example usage
# update_key_in_json('input.json', 'output.json')
