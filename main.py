import pandas as pd
import sys
import json
from git import Repo
import shutil
json_string = '{ "all": {"hosts": {}}}'
python_object = json.loads(json_string)
python_object["all"]["hosts"] = []
df = pd.read_excel(sys.argv[1], sheet_name='SERVIDORES')
df.to_csv('servidores.csv', index=False, encoding='utf-8')

def main():

for row in df.itertuples():
    python_object["all"]["hosts"].append({row.NOME: {'ansible_host': row.IP_PRODUCAO, 'ansible_host': row.IP_PRODUCAO, 'resp': row.RESPONSAVEL, 'sistema': row.SO}})

filename = "inventory.json"
COMMIT_MESSAGE = 'A descriptive message for your commit'
# Open the file in write mode ('w') and use json.dump()
with open(filename, 'w') as json_file:
    json.dump(python_object, json_file, indent=4) #

REMOTE_URL='https://x:x-x.01.x@x.x/x/x.py.git'
LOCAL_PATH='x-playbook'
#repo = Repo.clone_from(REMOTE_URL, LOCAL_PATH)
#shutil.move(filename, LOCAL_PATH)
#repo.index.add([filename])
#repo.index.commit(COMMIT_MESSAGE)
#origin = repo.remote(name='origin')
#origin.push()
if __name__ == "__main__":
    main()
