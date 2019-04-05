# (c) Tim Connors 2019
# Feb 23 2019
import os
import shutil
import stat
import csv
import helper
import dev_tools

class Session:
    current_store = "" # String
    default_store = "" #String

class Store:
    name = ""
    def __init__(self, name):
        self.name = name
        self.SkuTemplate = SkuTemplate()
    collections = []
    collection_skus = {}  # sku groups

class Collection:
    name = ""
    store = "" # Class
    def __init__(self, name, store):
         self.name = name
         self.store = store
    products = [] # List of Classes
    product_skus = {}  # sku groups

class Product:
    name = ""
    store = ""
    collection = ""
    def __init__(self, name, store, collection):
        self.name = name
        self.store = store
        self.collection = collection
    options = [] # options is a dictionary of option-attribute pairs
    option_skus = {}  # sku groups

class Option:
    # an option is a category of variants. ex: full fit gowns, or size 39 gowns
    name = ""
    store = ""
    collection = ""
    product = ""
    def __init__(self, name, store, collection, product):
        self.name = name
        self.store = store
        self.collection = collection
        self.product = product
    variants = []
    variant_skus = {} # sku groups

class Variant:
    name = ""
    store = ""
    collection = ""
    product = ""
    option = ""
    def __init__(self, name, store, collection, product, option):
        self.store = name
        self.store = store
        self.collection = collection
        self.product = product
        self.product = option
    sku = []

class SkuTemplate:
    store = ""
    # limit one SkuTemplate per store
    digits = 0
    max_attributes = 0;


### CORE VARIABLES ###

mySession = Session()
root = 'C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker'
root_inventory = root + "\\Inventory"

### CREATE FUNCTIONS ###

def createStore(*some_store_name):
    if len(some_store_name) < 1:
        store_name = input("What's the title of your store?")
    else:
        store_name = some_store_name[0]
    myStore = Store(store_name)
    helper.initializeStore(myStore)
    ans = input("Would you like to set this as the default store? (y/n) ").lower()
    if ans == 'y':
        helper.setDefaultStore(mySession,myStore.name)
    ans = input("Would you like to add a collection of products now? (y/n) ").lower()
    while ans == 'y':
        print("Adding a collection to the store: " + myStore.name)
        myStore.collections.append(createCollection(myStore))
        ans = input("Would you like to add another collection? (y/n) ").lower()
    return myStore
def createCollection(*some_store):
    if len(some_store) < 1:
        myStore = helper.checkStore()
    else:
        myStore = some_store[0]
    collections = myStore.collections
    name = input("What's the name of your collection?")
    while name in collections:
        print(collections)
        input("Collection already exists! Try again: ")
    myCollection = Collection(name,myStore)
    helper.initializeCollection(myCollection)
    os.mkdir(root + "\\Inventory\\" + myStore.name + myCollection.name)
    f = open("collections.txt", "a+")
    f.write(myCollection.name)
    f.close()
    ans = input("Would you like to add products to this collection now? (y/n) ").lower()
    while ans == 'y':
        myCollection.products.append(createProduct(myCollection))
        ans = input("Would you like to add another product? (y/n) ").lower()
    return myCollection
def createProduct(*some_collection):
    if len(some_collection) < 1:
        myCollection = helper.checkCollection()
    else:
        myCollection = some_collection[0]
    name = input("What's the title of your product? ")
    newProduct = Product(name, some_collection.store, some_collection)
    ans = input("Add options? (y/n) ").lower()
    while ans == 'y':
        newProduct.options.append(createOption(newProduct)).lower()
        ans = input("Would you like to add another option? (y/n) ").lower()
    return newProduct
def createOption(*some_product):
    if len(some_product) == 0:
        if defaultStore == "":
            print(mySession.stores)
            store = input("To which store does this apply?").lower()
        else:
            store = defaultStore
        for x in store.collections:
            print(x)
        collection = input("To which collection does this apply? ").lower()
        for x in collection.products:
            print(x)
        product = input("To which product does this apply? ").lower()
    name = input("What's the title of your option? ").lower()
    newOption = Option(name, some_product.store, some_product.collection, some_product)
    ans = input("Add variants? (y/n) ").lower()
    while ans == 'y':
        newOption.variants.append(createVariant(newOption))
        ans = input("Would you like to add another variant? (y/n) ").lower()
    return newOption
def createVariant(*some_option):
    if len(some_option) == 0:
        if defaultStore == "":
            print(mySession.stores)
            store = input("To which store does this apply?").lower()
        else:
            store = defaultStore
        for x in store.collections:
            print(x)
        collection = input("To which collection does this apply? ").lower()
        for x in collection.products:
            print(x)
        product = input("To which product does this apply? ").lower()
        for x in product.options:
            print(x)
        option = input("To which option does this apply? ").lower()
    names = input("Variant titles (separate by commas): ").split(',').lower()
    newVariantList = []
    for x in names:
        newVariantList.append(Variant(x, some_option.store, some_option.collection, some_option.product, some_option))
    return newVariantList

### DELETE FUNCTIONS ###

def deleteStore(*store):
    stores = []
    fin = open("stores.txt", "r+")
    for item in fin:
        stores.append(item.rstrip('\n'))
    fin.close()
    print(stores)
    if len(stores) < 1:
        print("There are no stores!")
        return
    if len(store) == 0:
        store = input("Which store would you like to delete?" )
    while store not in stores:
        store = input("No such store! Try again: ")
    path = root + "\\Inventory" + "\\" + store
    ans = input("Are you sure you want to delete " + store + "? If so, type 'delete': ")
    if ans == "delete":
        os.chmod(path, stat.S_IWRITE)
        shutil.rmtree(path)
        fout = open("stores.txt", "w+")
        stores.remove(store)
        for item in stores:
            fout.write(item + '\n')
        print("store deleted!")

# def deleteCollection(*collection):
#     collections []



### LOAD ###
def loadStore(*some_store_name):
    if len(some_store_name) < 0:

        store_name = input("Which store would you like to load?")
