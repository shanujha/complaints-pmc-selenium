import pandas as pd
import json

def excel_to_json(excel_file, json_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Replace NaN values with False
    df = df.fillna(False)

    # Convert DataFrame to JSON and write to file
    json_data = df.to_dict(orient='records')
    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"Excel file {excel_file} converted to JSON file {json_file}")

def json_to_excel(json_file, excel_file):
    # Read the JSON file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Convert JSON data to DataFrame
    df = pd.DataFrame(json_data)

    # Replace NaN values with False (though unlikely since JSON should not have NaN)
    df = df.fillna(False)

    # Write DataFrame to Excel
    df.to_excel(excel_file, index=False)
    print(f"JSON file {json_file} converted to Excel file {excel_file}")

# Example usage
# excel_to_json('main.xlsx', 'json/input/main.json')
json_to_excel('json/output/checked.json', 'updated_status_check_category_subcategory.xlsx')
