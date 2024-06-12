

import os

source_dir = "/Users/jamieclements/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
