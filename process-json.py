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

process()