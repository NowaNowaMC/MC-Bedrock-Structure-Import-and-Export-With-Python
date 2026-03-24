from leveldb import LevelDB
import os,sys

# grab world path from command line arguments
world_path = sys.argv[1]
if not os.path.exists(world_path):
    print(f'Could not find world at "{world_path}"')
    exit(1)

# grab data from leveldb database
db_path = world_path+'/db'
if not os.path.exists(db_path):
    print(f'Could not find leveldb database at "{db_path}"')
    exit(1)
else:
    db = LevelDB(db_path)

# if no structures folder exists, create it
if not os.path.exists(world_path+'/structures'):
    os.makedirs(world_path+'/structures')

# if no specific structure is specified, export all structures
structure_id = sys.argv[2] if len(sys.argv) > 2 else 'all'
for key, data in db.iterate():
    if key.startswith(b'structuretemplate_'):
        key = key[len(b'structuretemplate_'):].decode('utf-8').replace('/',':')
        if structure_id == 'all' or \
           key == structure_id or key == 'mystructure:'+structure_id:
            print(f'Exporting structure "{key}" to "{world_path}/structures/{key}.mcstructure"')
            try:
                with open(world_path+'/structures/'+key+'.mcstructure', 'wb') as f:
                    f.write(data)
            except Exception as e:
                print(f'Error occurred while exporting structure "{key}": {e}')