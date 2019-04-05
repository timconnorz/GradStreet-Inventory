import os
import stat
import shutil

import inventory
import helper

def deleteAllStores():
    paths = []
    folders = helper.getFolders(inventory.root_inventory)
    for name in folders:
        paths.append(inventory.root_inventory + "\\" + name)
    print("deleting stores...")
    for path in paths:
        os.chmod(path, stat.S_IWRITE)
        shutil.rmtree(path)
        print(path)
    f = open("stores.txt", "w+").close()
    return
