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
# json_to_excel('json/output/checked.json', 'updated_status_check_category_subcategory.xlsx')

def print_usage():
    """Print usage instructions for the Excel-JSON conversion utilities"""
    print("""
Usage Examples for Excel-JSON Conversion:

1. Convert Excel to JSON:
   python main.py excel-to-json <input_excel> <output_json>
   
   Example:
   python main.py excel-to-json data.xlsx output.json

2. Convert JSON to Excel:  
   python main.py json-to-excel <input_json> <output_excel>
   
   Example:
   python main.py json-to-excel data.json output.xlsx
""")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
        
    command = sys.argv[1]
    
    if command == "excel-to-json" and len(sys.argv) == 4:
        excel_to_json(sys.argv[2], sys.argv[3])
    elif command == "json-to-excel" and len(sys.argv) == 4:
        json_to_excel(sys.argv[2], sys.argv[3])
    else:
        print("Invalid command or arguments")
        print_usage()
        sys.exit(1)
