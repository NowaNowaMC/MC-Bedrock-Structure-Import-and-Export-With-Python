# MC-Bedrock-Structure-Import-and-Export-With-Python
Two very bare bones python files to insert and extract .mcstructure files to and from minecraft bedrock db world data.

# Exporting Structures with Get_Structure_Files.py
Extract all structures: `python3 Get_Structure_Files.py <world folder path>`.

Extract a specific structure: `python3 Get_Structure_Files.py <world folder path> <structure name>`.

Extracted structures will be saved to `<world folder path>/structures/<structure name>.mcstructure`.

# Importing Structures with Insert_Structure_File.py
Insert a structure into a world: `python3 Insert_Structure_File.py <world folder path> <structure file path>`.

# Note
I recommend using a python virtual environment, for example using venv. The only dependency is amulet-leveldb which can be installed through pip. This worked for me with no issues using python version 3.14.3, pip version 26.0.1, and amulet-leveldb version 1.0.3. Minecraft version 1.26.0.2 using mcpelauncher from https://github.com/minecraft-linux/mcpelauncher-manifest.

Inspiration from https://github.com/destruc7i0n/extract-mcstructure. I was having trouble getting their code to work for me, and I wanted the ability to import as well.
