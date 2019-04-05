# creates a file ready to be imported into Shopify to update inventory
# takes in initial inventory numbers from ORDER_AGGREGATE_BUNDLED
# also takes in manual bundles from MANUAL_BUNDLES
# also takes in 2019 orders thus far, beginning with #4025

# READS IN THE EXPORTED INVENTORY FILE AND UPDATES THE NUMBERS

import csv


IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"
inventory_file = "C:\\Users\\User\\Downloads\\inventory_export (2).csv"
orders_file = "C:\\Users\\User\\Downloads\\orders_export (1).csv"

field_names = ["Handle", "Title", "Option1 Name", "Option1 Value", "Option2 Name",
"Option2 Value", "Option3 Name", "Option3 Value", "SKU", "2437 Corinth Avenue", "Amazon Marketplace Web"]

class line:
    dict = {
    field_names[0] : "", #Handle
    field_names[1] : "", #Title
    field_names[2] : "", #Option1 Name
    field_names[3] : "", #Option1 Value
    field_names[4] : "", #Option2 Name
    field_names[5] : "", #Option2 Value
    field_names[6] : "", #Option3 Name
    field_names[7] : "", #Option3 Value
    field_names[8] : "", #SKU
    field_names[9] : "", #2437 Corinth Avenue (quantity) (number, or "not stocked")
    field_names[10] : "not stocked" #Amazon MArketplace Web (quantity) (number, or "not stocked")
    }

def productInventory(path):

    #key: SKU, value: Qty
    bundle_quantities = {}

    # reads in ORDER_AGGREGATE_BUNDLED to get initial inventory quantities
    with open(IMPORTANTcsv_folder_path + "ORDER_AGGREGATE_BUNDLED (8).csv", 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            if row[0].isdigit():
                bundle_quantities[row[5]] = row[0]

    #reads in Manual_Bundles to add the quantities of bundles that tim is going to do manually
    with open(IMPORTANTcsv_folder_path + "Manual_Bundles.csv", 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        num_header_rows = 2
        row_num = 0
        for row in fin:
            row_num += 1
            if row_num <= num_header_rows:
                continue
            else:
                try:
                    bundle_quantities[row[10]] = str(int(bundle_quantities[row[10]]) + int(row[9]))
                except:
                    bundle_quantities[row[10]] = row[9]


    #reads in shopify orders export
    with open(orders_file, 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            if row[0] == "Name": continue
            if row[20] != "":
                bundle_quantities[row[20]] = int(bundle_quantities[row[20]]) - 1

    #reads in shopify inventory file
    rows = []
    with open(inventory_file, 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            line = []
            for item in row:
                line.append(item)
            rows.append(line)

    with open(CREATED_folder_path + "product-inventory.csv", 'w', newline='') as csv_file:
        fout = csv.writer(csv_file,delimiter=',')
        for line in rows:
            if line[0] != "Handle":
                try:
                    line[9] = bundle_quantities[line[8]]
                except:
                    line[9] = "0"
            fout.writerow(line)

productInventory(IMPORTANTcsv_folder_path + "ORDER_AGGREGATE_BUNDLED (8).csv")
