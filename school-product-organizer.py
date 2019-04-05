# reads in "School Mapping 2019" file

#poop

# output a csv file formatted for Shopify product import function
# meant to just add the school gown BUNDLE products, not accessories, not photography
import csv
import random

IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"

mapping_file_path = IMPORTANTcsv_folder_path + "School_Mapping.csv"
bundle_quantities_file_path = IMPORTANTcsv_folder_path + "ORDER_AGGREGATE_BUNDLED (8).csv"
msku_fnsku_path =  IMPORTANTcsv_folder_path + "MSKU_FNSKU_ASIN.csv"

heights = ["4\'6\"-4\'8\"","4\'9\"-4\'11\"","5\'0\"-5\'2\"","5\'3\"-5\'5\"","5\'6\"-5\'8\"",
"5\'9\"-5\'11\"","6\'0\"-6\'2\"","6\'3\"-6\'5\"","6\'6\"-6\'8\""]
gown_heights = ["39","42","45","48","51","54","57","60","63"]
fits = ["Standard","Full"]
field_names = ["Handle", "Title", "Body (HTML)", "Vendor",
    "Type", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value",
    "Option3 Name", "Option3 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker",
    "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare at Price",
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position", "Image Alt Text",
    "Gift Card", "Seo Title", "Seo Description","Google Shopping / Google Product Category", "Google Shopping / Gender",
    "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / Adwords Grouping", "Google Shopping / Adwords Labels",
    "Google Shopping / Condition",  "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1",
    "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", "Variant Image",
    "Variant Weight Unit", "Variant Tax Code", "Cost per item" ]

class Product:
    def __init__(self, school, degree_type, study, green_light, title, msku):
        self.school = school
        self.degree_type = degree_type
        self.green_light = green_light
        self.study = study
        self.title = title
        self.msku = msku
    school = ""
    title = ""
    msku = ""
    qty = ""

class Line:
    dict = { #default values for a gown product
        field_names[0] : "",  #Handle
        field_names[1] : "",   #Title
        field_names[2] : "",    #Body (HTML)
        field_names[3] : "GradStreet", #vendor
        field_names[4] : "gown bundle", #type
        field_names[5] : "",  #Tags
        field_names[6] : "TRUE", #Published
        field_names[7] : "Height", #Option1 Name
        field_names[8] : "",  #Option1 Value
        field_names[9] : "Fit", #Option2 Name
        field_names[10] : "",  #Option2 Value
        field_names[11] : "",   #Option3 Name
        field_names[12] : "",   #Option3 Value
        field_names[13] : "",  #Variant SKU
        field_names[14] : 550, #Variant Grams
        field_names[15] : "shopify", #Variant Inventory Tracker (options: shopify, amazon_marketplace_web)
        field_names[16] : "deny", #Variant Inventory Policy
        field_names[17] : "manual", #Variant Fulfilment Service (options: amazon_marketplace_web, manual)
        field_names[18] : "", #Variant Price
        field_names[19] : "", #Variant Compare at Price
        field_names[20] : "TRUE", #Variant Requires Shipping
        field_names[21] : "TRUE", #Variant Taxable
        field_names[22] : "", #Variant Barcode
        field_names[23] : "", #Image Src
        field_names[24] : "", #Image Position
        field_names[25] : "", #Image Alt Text
        field_names[26] : "FALSE", #Gift Card
        field_names[27] : "", #SEO Title
        field_names[28] : "", #SEO Description
        field_names[29] : "", #google shopping stuff --
        field_names[30] : "",
        field_names[31] : "",
        field_names[32] : "",
        field_names[33] : "",
        field_names[34] : "",
        field_names[35] : "",
        field_names[36] : "",
        field_names[37] : "",
        field_names[38] : "",
        field_names[39] : "",
        field_names[40] : "",
        field_names[41] : "",
        field_names[42] : "", #Variant Image
        field_names[43] : "kg", #Variant Weight Unit
        field_names[44] : "", #Variant Tax code
        field_names[45] : "" #Cost per item
    }

product_image_links =  ["https://cdn.shopify.com/s/files/1/1766/6171/files/898000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/898000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/111000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/111000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/104000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/031000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/104000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/031000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/025019_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/025019_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/020000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/020000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/019000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/019000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/017031_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/017000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/015000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/017000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/017031_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/015000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/006000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/014000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/002000_0.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/006000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/002000_1.jpg?4286832225318832821",
    "https://cdn.shopify.com/s/files/1/1766/6171/files/014000_0.jpg?4286832225318832821"
    ]

def productOrganizer(mapping_file_path):
    products = []
    prices = {}
    bundle_quantities = {}
    msku_fnsku = {}

    with open(mapping_file_path, 'r') as csv_file:   # read in the mapping csv_file
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            if row[0] == "School":
                continue
            else:
                newProduct = Product(row[0],row[1],row[2],row[5],row[9],row[10])
                products.append(newProduct)

    with open(IMPORTANTcsv_folder_path + "Gown_Prices.csv",'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            prices[row[0] + row[1]] = row[2]

    with open(msku_fnsku_path,'r') as csv_file: # now let's make the fnsku dictionary
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            msku_fnsku[row[0]] = row[1]

    with open(CREATED_folder_path + "school-product-organizer.csv", 'w', newline='') as csv_file:   # write to the new csv_file
        height_counter = 0
        fit_counter = -1
        fout = csv.DictWriter(csv_file, fieldnames=field_names, restval="", extrasaction="ignore", delimiter=",")
        fout.writeheader()
        previous_handle = ""
        alt = "0"
        for product in products:
            for height in heights:
                for fit in fits:
                    newLine = Line()
                    handle = product.title.replace(' - ',' ').replace('.','').replace('(','').replace(')','').replace(' ','-').lower()
                    newLine.dict["Handle"] = handle
                    if handle == previous_handle: newLine.dict["Title"] = ""
                    else: newLine.dict["Title"] = product.title
                    if handle == previous_handle: newLine.dict["body"] = ""
                    else: newLine.dict["Body (HTML)"] = "We're not associated with " + product.school + ". That's the point! This cap, gown, and tassel package is exactly what you'd get at the bookstore, for way less!"
                    if handle == previous_handle:
                        newLine.dict["Tags"] = ""
                    else:
                        newLine.dict["Tags"] = (product.degree_type + ", " + product.degree_type + "-" +
                        product.study.replace(' & ','-').replace(',','').replace('.','').replace(' ','-') +  ", " +
                        "meta-related-collection-graduation-accessories").lower()
                        # newLine.dict["Tags"] = ("\"" + product.degree_type + "\"" + ", " + "\"" + product.degree_type + "\"" + "-" +
                        # "\"" + product.study.replace(' & ','-').replace(',','').replace('.','').replace(' ','-') + "\"" + ", " +
                        # "\"meta-related-collection-graduation-accessories\"").lower()
                    newLine.dict["Option1 Value"] = height
                    newLine.dict["Option2 Value"] = fit
                    newLine.dict["Variant SKU"] = product.msku[0:7] + fit[0].upper() + gown_heights[heights.index(height)] + product.msku[10:]
                    newLine.dict["Variant Price"] = prices[product.school + product.degree_type]
                    if product.green_light == "0" or newLine.dict["Variant SKU"] not in bundle_quantities:
                        newLine.dict["Variant Barcode"] = ""
                    else:
                        newLine.dict["Variant Barcode"] = msku_fnsku[newLine.dict["Variant SKU"]]
                    if product.green_light == "0":
                        newLine.dict["Image Src"] = random.choice(product_image_links)
                    else:
                        newLine.dict["Image Src"] = "https://cdn.shopify.com/s/files/1/1766/6171/files/" + product.msku[12:18] + "_" + alt + ".jpg?4286832225318832821"
                    fout.writerow(newLine.dict)
                    previous_handle = handle
                    if alt == "0": alt = "1"
                    else: alt = "0"

productOrganizer(mapping_file_path)
