import json
import pandas as pd
from git import Repo
import shutil

REMOTE_URL = 'https://x:x-x.01.x@x.x/x/x.py.git'
LOCAL_PATH = 'x-playbook'
COMMIT_MESSAGE = 'Add inventory generated from Excel'

def main(sheet):
    df = pd.read_excel(sheet, sheet_name='SERVIDORES')
    df.to_csv('servidores.csv', index=False, encoding='utf-8')

    inventory = {"all": {"hosts": {}}}

    for row in df.itertuples(index=False):
        inventory["all"]["hosts"][str(row.NOME)] = {
            "ansible_host": str(row.IP_PRODUCAO),
            "resp": str(row.RESPONSAVEL),
            "sistema": str(row.SO),
        }

    filename = "inventory.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(inventory, json_file, indent=4, ensure_ascii=False)

    # repo = Repo.clone_from(REMOTE_URL, LOCAL_PATH)
    # shutil.copy(filename, f"{LOCAL_PATH}/{filename}")
    # repo.index.add([filename])
    # repo.index.commit(COMMIT_MESSAGE)
    # repo.remote(name='origin').push()

if __name__ == "__main__":
    main("/fileserver/temp/doc.xlsx")
