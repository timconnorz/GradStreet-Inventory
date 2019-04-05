import csv
import sys
# packify takes in a csv file as input
#returns a separate csv as output

    # takes in "ORDER_AGGREGATE_BUNDLED.csv"
# order aggregate bundled has only one row per SKU
# outputs "PACKING GUIDE CSV"

##NOTES##
#"path" is the path to the order aggregate bundled

IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"
path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\Manual_Bundles - MANUAL_ORDER_AGGREGATE_BUNDLED.csv"

who_fulfills = {}
gowns_per_box = 25
tassels_per_box = 1500
yeartags_per_box = 10000

#manual break points where a new box will start AFTER this point
break_points = ["UMC0173S63T00250190K01","BC2194F63"]

def packify(path):
    # read in bundle
    products = []
    with open(path, 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        begin = False
        for row in fin:
            if row[0] == "Quantity":
                begin = True
                continue;
            if row[0] == "":
                continue;
            if begin == True:
                if row[6][0] == 'X': who_fulfills[row[5]] = "amazon_marketplace_web"
                else: who_fulfills[row[5]] = "manual"
                quantity = int(row[0])
                for x in range(quantity):
                    products.append(row[5])

    # make new file
    with open(CREATED_folder_path + "packing-guide.csv", 'w', newline='') as csv_file:
        fout = csv.writer(csv_file)
        limit = gowns_per_box
        index = -1
        box_num = 1
        counter = 0
        prior_fulfiller = ""
        current_fulfiller = ""
        prior_item = products[0]  #default is initial item
        quantity = 0 # default quantity
        box_content = []
        for item in products:
            if item[0] == "T":
                limit = tassels_per_box
            if item[0] == "Y":
                limit = yeartags_per_box
            current_fulfiller = who_fulfills[item]
            index += 1
            counter += 1
            #sys.stdout.write("fulfilled by " + current_fulfiller)
            if item == prior_item: # if its the same SKU
                quantity += 1
            else: # if it's a new SKU
                if quantity != 0:
                    box_content.append([str(quantity),str(prior_item)])
                quantity = 1
            # if we hit limit or end of the products...
            if counter == limit or index == len(products)-1 or item in break_points:
                box_content.append([str(quantity),str(item)])
                if box_content[0][1][0:1] == "U":
                    last_fit = box_content[0][1][7:8]
                    last_style = box_content[0][1][6:7]
                else:
                    last_fit = box_content[0][1][0:1]
                    last_style = box_content[0][1][0:1]
                for sku_count in box_content:
                    if sku_count[1][0:1] == "U":
                        current_fit = sku_count[1][7:8]
                        current_style = sku_count[1][6:7]
                    else:
                        current_fit = sku_count[1][0:1]
                        current_style = sku_count[1][0:1]
                    if current_fit != last_fit or current_style != last_style:
                        fout.writerow("") # skip a line between categories
                    fout.writerow([box_num, sku_count[0], sku_count[1]])
                    last_fit = current_fit
                    last_style = current_style
                if box_num%10 == 0: print("finished box #" + str(box_num))
                quantity = 0
                box_num += 1
                counter = 0
                box_content = []
            prior_item = item
            prior_fulfiller = current_fulfiller

packify(path)
