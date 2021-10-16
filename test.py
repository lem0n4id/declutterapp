from mongodb.mongodb_base import generate_objectid 
from mongodb.sample_requests import  add_entry_in_entries, add_entry_in_interests


def test_add_entry():
    obj=generate_objectid("6169fbefe8bf5d02d3488820")
    dictionary={
     "entry_id":"ObjectID('60c01917706af33ed8db96')",
     "name":"Why web3 matters", 
     "url":"https://blog.mcgee.cat/why-web3-matters",
     "importance":"",
     "created_date":"2021-10-15T18:28:23.382748", 
     "remind_on":"2021-10-16T18:28:23.382748",
     "read_status":False,
     "tags":["Tech","Web3"],
     "host":obj
    }
    add_entry_in_entries(dictionary)

def test_add_interests():
    obj=generate_objectid("6169fbefe8bf5d02d3488820")
    dictionary={
    "entry_id":"ObjectID(6798922vxvjhs882)",
    "category":"Tech", 
    "weight":{"casual": 0, "moderate":1,"important":0},
    "host":obj
    }
    add_entry_in_interests(dictionary)

if __name__ == "__main__":
    # test_add_entry()
    test_add_interests()