#reads in packing GUIDE
# exports the palletizing GUIDE
# must be manually entered into the palletizing guide on google sheets

import csv
IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"

def palletize(packing_guide_path):
    # boxes is a dictionary with each box paired with it's fulfiller (manual or amazon)
    boxes = {}
    with open(packing_guide_path, 'r') as csv_file:
        fin = csv.reader(csv_file,delimiter=',')
        for row in fin:
            #print(row)
            try:
                if int(row[0]) not in boxes:
                    if len(row[6]) == 10:
                        boxes[int(row[0])] = "Amazon"
                    else:
                        boxes[int(row[0])] = "Tim"
            except:
                continue
    #print(boxes)
    with open(CREATED_folder_path + "manual-palletizing-guide.csv",'w',newline='') as csv_file:
        fout = csv.writer(csv_file,delimiter=',')
        counter = 0
        pallet_num = 1
        prior_fulfiller = "Amazon" #default value
        fout.writerow(["Pallet Number","Box Number","Label"])
        for box in boxes:
            if boxes[box] != prior_fulfiller:
                counter = 0
                pallet_num += 1
            fout.writerow([pallet_num,box,"Pallet Label " + str(pallet_num)])
            counter += 1
            if counter == 24:
                counter = 0
                pallet_num += 1
            prior_fulfiller = boxes[box]

palletize(IMPORTANTcsv_folder_path + "MANUAL_PACKING_GUIDE.csv")
