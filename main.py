import os
import json
import pandas as pd

def main(sheet):
    df = pd.read_excel(sheet, sheet_name="SERVIDORES")
    df.to_csv("servidores.csv", index=False, encoding="utf-8")

    inventory = {"all": {"hosts": {}}}
    for row in df.itertuples(index=False):
        inventory["all"]["hosts"][str(row.NOME)] = {
            "ansible_host": str(row.IP_PRODUCAO),
            "resp": str(row.RESPONSAVEL),
            "sistema": str(row.SO),
        }

    with open("inventory.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=4, ensure_ascii=False)

    if os.environ.get("ENABLE_GIT_PUSH") == "1":
        os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = "/usr/bin/git"
        from git import Repo
        repo = Repo.clone_from(REMOTE_URL, LOCAL_PATH)

if __name__ == "__main__":
    main("/fileserver/temp/doc.xlsx")
