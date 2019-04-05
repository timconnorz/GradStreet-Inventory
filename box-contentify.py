# (c) 2019 Tim Connors | GradStreet
# reads in PACKING GUIDE and produces a tsv file formated for pasting into AMAZON box content template
# output: box-content.tsv
# NOTES #
# this out output must be MANUALLY pasted into the amazon template
# for some reason this only prints out the bundles, which is exactly what i want, but i don't understand why is does that

import csv

IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"

def boxContentify(packing_guide_path):
    # this is a list of dictionaries (boxes)
    # index + 1 = the box number
    shipment = []
    row_count = 0
    # get the total number of rows first
    with open(packing_guide_path, 'r') as csv_file:
        fin = csv.reader(csv_file,delimiter = ',')
        for row in fin:
            row_count += 1

    #first we gotta read in the packing list to create the shipment list
    with open(packing_guide_path, 'r') as csv_file:
        fin = csv.reader(csv_file,delimiter = ',')
        prior_box_number = 1
        box = {}
        it = 0
        for row in fin:
            it += 1
            try:
                box_number = int(row[0])
                # if we're now onto the next box, add the prior one to the list and empty the box
                if box_number != prior_box_number:
                    shipment.append(box)
                    box = {}
                # MISSES THE LAST BOX ^^ put this below, check if last box
                # add to box dict, the MSKU paired with the quantity
                print(row[1])
                box[row[5]] = row[1]
                prior_box_number = box_number
                if it == row_count:
                    shipment.append(box)
                    box = {}
            except:
                continue

    print("Read in Packing Guide. Total Box Count: " + str(len(shipment)))

    # get rid of empty boxes (ie. boxes that don't have FBA products in them)
    for box in shipment:
        if not bool(box): #if the box is empty (it returns false)
            shipment.remove(box)

    # print("Amazon boxes: " + str((shipment[len(shipment)-1])))

    # not we're going to prepare the header row of the tsv file
    tsv_headers = ["Merchant SKU","Title","ASIN","FNSKU","external-id","Condition","Who Will Prep?","Prep Type","Who Will Label?","Shipped"]
    for x in range(len(shipment)):
        tsv_headers.append("FBA15G5HKHCLU"+ '{:03}'.format(x+1) + " - Unit Quantity")
        tsv_headers.append("FBA15G5HKHCLU"+ '{:03}'.format(x+1) + " Expiration Date (mm/dd/yy)")

    # this is a list of rows in the tsv file
    sku_row = []

    # read in the AMAZONs list of MSKUs and other details to populate sku_rows
    with open(IMPORTANTcsv_folder_path + "Manual_Amazon-Skus.csv", 'r', encoding='utf-8-sig') as csv_file:
        fin = csv.reader(csv_file,delimiter=',')
        for row in fin:
            new_row = []
            for x in range(10):
                #print("writing to column " + str(x))
                new_row.append(row[x])
            for box in range(len(shipment)):
                #print(int(box))
                # if this sku is in box #x
                if new_row[0] in shipment[box]:
                    #print("wtf")
                    new_row.append(shipment[box][row[0]])
                #otherwise, it's zero
                else:
                    new_row.append("")
                #now append the expiration date
                new_row.append("Not Needed")
            sku_row.append(new_row)
    # now we're going to write the rows to the tsv file
    with open(CREATED_folder_path + "manual_box-content.tsv", 'w', newline='') as tsv_file:
        fin = csv.writer(tsv_file, delimiter    = '\t')
        fin.writerow(tsv_headers)
        for item in sku_row:
            fin.writerow(item)


boxContentify(IMPORTANTcsv_folder_path + "MANUAL_PACKING_GUIDE.csv")
