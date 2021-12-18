import os
from pathlib import Path

from pymongo import MongoClient
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.errors import EncryptionError
from bson import json_util


# Create data for database
data = {"_id" : ['6341', '3712', '2264', '7649', '2493', '7642', '3495', '5648', '1679', '8466'],
		"full_name" : ['Robin Williams', 'Betty White', 'Denzel Washington', 'Tom Hanks','Morgan Freeman',
						'Lucille Ball', 'Harrison Ford', 'Sandra Bullock', 'Sean Connery', 'Jackie Chan'],
 		"idnp" : ['9971547838863', '2224421516531', '2353025570757', '9856834950942', '3033833542061', 
		 			'3722118777380', '5439655233307' , '0799705818532', '3364451541028', '2981225163973']}


# Load the master key from 'key_bytes.bin':
key_bin = Path("key_bytes.bin").read_bytes()

# Load the 'person' schema from "json_schema.json":
collection_schema = json_util.loads(Path("json_schema.json").read_text())


# Configure a single, local KMS provider, with the saved key:
kms_providers = {"local": {"key": key_bin}}

# Create a configuration for PyMongo, specifying the local master key,
# the collection used for storing key data, and the json schema specifying
# field encryption:
csfle_opts = AutoEncryptionOpts(
   kms_providers,
   "lab7.__keystore",
   schema_map={"lab7.people": collection_schema},
)

username = 'popescupaula'
password = 'PacCB9PqDru6Ep34'

# Add a new document to the "people" collection, and then read it back out
# to demonstrate that the idnp field is automatically decrypted by PyMongo:
with MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0.quxiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", auto_encryption_opts=csfle_opts) as client:
	client.lab7.people.delete_many({})

	for index in range(len(data['full_name'])):
		client.lab7.people.insert_one({
				"_id": data['_id'][index],
   			"full_name": data['full_name'][index],
   			"idnp": data['idnp'][index],
			})
