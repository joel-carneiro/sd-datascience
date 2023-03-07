#!/usr/bin/env python3

import os

with open('/home/jdspy/Documentos/sd-datascience/version.log', 'r') as f:
	version = int(f.read())

os.system('git add .')
os.system(f'git commit -m "v{version}.0"')
os.system('git push')

with open('/home/jdspy/Documentos/sd-datascience/version.log', 'w') as f:
	f.write(str(version + 1))
