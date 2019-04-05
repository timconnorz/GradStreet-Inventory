import os
import shutil
import stat
import helper

import inventory

def setDefaultStore(session, store_name):
    session.defaultStore = store_name
    f = open("default.txt", "w+")
    f.write(store_name)
    f.close()

def getDefaultStore():
    fin = open("default.txt", "r")
    myStore = inventory.Store(fin.readline())
    #myStore.collections = fin.readline()
    #myStore.collection_skus = fin.readline()
    return myStore

def initializeStore(some_store):
    myStore = some_store
    # create / update stores file
    os.mkdir("./Inventory/" + myStore.name, 0o777)
    f = open("stores.txt","a+")
    f.write(myStore.name + '\n')
    f.close()
    # create collections file
    f = open("./Inventory/" + myStore.name + "/" + "collections.txt", "a+")
    f.close()

def initializeCollection(some_collection):
    myCollection = some_collection
    # create / update collection file
    store_path = "./Inventory/" + myCollection.store.name
    os.mkdir(store_path + "/" + myCollection.name, 0o777)
    f = open(store_path + "/collections.txt", "a+")
    f.write(myCollection.name + '\n')
    f.close()
    # create products file
    collection_path = store_path + "/" + myCollection.name
    f = open(collection_path + "/products.txt", "a+")
    f.close()

def getFolders(parent_path): # returns a list of folder names
    folders = []
    for item in os.listdir(parent_path):
        if os.path.isdir(parent_path + "\\" + item):
            folders.append(item)
    return folders

def getStores():
    try:
        f = open("stores.txt", "r+")
        return f.readlines()
    except:
        return []

def getCollections(some_store):
    f = open("./" + some_store + "/collections.txt", "r+")
    return f.readlines()

def getProducts(some_collection):
    f = open("./" + some_collection.store + some_collection + "/products.txt", "r+")
    return f.readlines()

def getOptions(some_product):
    f = open("./" + some_product.store + some_product.collection + some_product + "/options.txt", "r+")
    return f.readlines()

def getVariants(some_option):
    f = open("./" + some_option.store + some_option.collection + some_option.product + some_option + "/variants.txt", "r+")
    return f.readlines()

def checkStore(*some_thing):
    if len(some_thing) < 1:
        stores = getStores()
        stores.append("0-Create New Store")
        default_store = getDefaultStore()
        if default_store == "":
            print(stores)
            chosen_store = input("To which store does this apply? ")
            while chosen_store not in stores:
                chosen_store = input("Error! Please pick an option")
            if chosen_store == "0":
                return inventory.createStore()
            else:
                return loadStore(chosen_store)
        else:
            return getDefaultStore()
    elif len(some_thing) > 0:
        try:
            return some_thing[0].store
        except:
            stores = getStores()
            stores.append("0-Create New Store")
            default_store = getDefaultStore()
            if default_store == "":
                print(stores)
                chosen_store = input("To which store does this apply? ")
                while (chosen_store not in stores) and (chosen_store != "0"):
                    chosen_store = input("Error! Please pick an option")
                if chosen_store == "0":
                    return inventory.createStore()
                else:
                    return loadStore(chosen_store)
            else:
                return getDefaultStore()

def checkCollection(*some_thing):
    if len(some_thing) < 1 or (len(some_thing) > 0 and some_thing[0].collection == ""):
        myStore = checkStore()
        collections = myStore.collections
        if "0-Create New Collection" not in collections:
            collections.append("0-Create New Collection")
        print(collections)
        chosen_collection = input("To which collection does this apply? ")
        while (chosen_collection not in myStore.collections) and (chosen_collection != "0"):
            chosen_collection = input("Error! Please pick an option from above: ")
        if chosen_collection == "0":
            return inventory.createCollection(myStore)
        else:
            return loadCollection(chosen_collection)
    else:
        return some_thing[0].collection


def printStore(some_store):
    print("Store Name: " + some_store.name)
    print("Collections--------")
    for item in some_store.collections:
        print(item)
    return
