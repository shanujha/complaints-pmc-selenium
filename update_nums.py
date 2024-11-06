import json

def update_nums(json_file, output_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Keys to update
    keys_to_update = ['grievanceSubDeptDetailId', 'categoryId', 'handleCode', 'startCode']

    # Function to convert floats to integers
    def convert_floats_to_int(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in keys_to_update and isinstance(value, float):
                    obj[key] = int(value)
                elif isinstance(value, (dict, list)):
                    convert_floats_to_int(value)
        elif isinstance(obj, list):
            for item in obj:
                convert_floats_to_int(item)
        return obj

    # Update the JSON data
    updated_data = convert_floats_to_int(data)

    # Write the updated JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(updated_data, f, indent=4)

    print(f"Float values updated in {json_file} and saved to {output_file}")

# Example usage
# update_nums('input.json', 'output.json')
