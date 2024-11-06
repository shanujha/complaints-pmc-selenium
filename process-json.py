from update_keys import update_key_in_json
from update_peth import update_peth_type
from update_ward import update_ward_value
from update_nums import update_nums
from update_prabhag import update_prabhag_value
from update_app_type import add_app_type


def process():
    update_key_in_json("json/input/main.json", "json/output/1_keys.json")
    update_peth_type("json/output/1_keys.json", "json/output/2_peth.json")
    update_ward_value("json/output/2_peth.json", "json/output/3_ward.json")
    update_nums("json/output/3_ward.json", "json/output/4_nums.json")
    update_prabhag_value("json/output/4_nums.json", "json/output/5_prabhag.json")
    add_app_type("json/output/5_prabhag.json", "json/output/final.json")
    pass

def print_usage():
    """Print usage instructions for the JSON processing pipeline"""
    print("""
Usage:
    python process-json.py start

This script processes JSON data through multiple transformation steps:
1. Updates keys in the JSON
2. Updates peth type values
3. Updates ward values 
4. Updates numeric fields
5. Updates prabhag values
6. Adds application type

The script expects:
- Input JSON file at: json/input/main.json
- Generates intermediate files in: json/output/
- Final processed file at: json/output/final.json

To run this script's process run:
python process-json.py start
""")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
        
    process()
