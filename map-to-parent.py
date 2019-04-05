import csv

IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"


parent_children = {}

with open(CREATED_folder_path + "generic-product-organizer.csv", 'r') as csv_file:
    fin = csv.reader(csv_file, delimiter=',')
    for row in fin:
        if row[0] == 'H':
            continue
        else:
            
