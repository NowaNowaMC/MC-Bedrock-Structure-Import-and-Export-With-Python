from leveldb import LevelDB
import os,sys

# grab world path from command line arguments
world_path = sys.argv[1]
if not os.path.exists(world_path):
    print(f'Could not find world at "{world_path}"')
    exit(1)
else:
    db = LevelDB(world_path+'/db')

# grab structure file path from command line arguments
structure_file_path = sys.argv[2]
if not os.path.exists(structure_file_path):
    print(f'Could not find structure file at "{structure_file_path}"')
    exit(1)
else:
    print(f'Inserting structure file "{structure_file_path}" into world "{world_path}"')
    try:
        with open(structure_file_path, 'rb') as f:
            data = f.read()
            db.put(b'structuretemplate_'+os.path.basename(structure_file_path).replace('.mcstructure','').encode('utf-8'), data)
    except Exception as e:
        print(f'Error occurred while inserting structure file: {e}')