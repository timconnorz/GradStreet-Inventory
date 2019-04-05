import csv
import random

IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"

class Product:
    def __init__(self, title, school, package):
        self.title = title
        self.school = school
        self.package = package

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

class Line:
    dict = { #default values for a custom photography product
        field_names[0] : "",  #Handle
        field_names[1] : "",   #Title
        field_names[2] : "",    #Body (HTML)
        field_names[3] : "GradStreet", #vendor
        field_names[4] : "photography", #type
        field_names[5] : "",  #Tags
        field_names[6] : "TRUE", #Published
        field_names[7] : "School", #Option1 Name
        field_names[8] : "",  #Option1 Value
        field_names[9] : "Shoot Type", #Option2 Name
        field_names[10] : "",  #Option2 Value
        field_names[11] : "",   #Option3 Name
        field_names[12] : "",   #Option3 Value
        field_names[13] : "",  #Variant SKU
        field_names[14] : "", #Variant Grams
        field_names[15] : "shopify", #Variant Inventory Tracker (options: shopify, amazon_marketplace_web)
        field_names[16] : "continue", #Variant Inventory Policy (options: continue, deny)
        field_names[17] : "manual", #Variant Fulfilment Service (options: amazon_marketplace_web, manual)
        field_names[18] : "", #Variant Price
        field_names[19] : "", #Variant Compare at Price
        field_names[20] : "FALSE", #Variant Requires Shipping
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
        field_names[43] : "", #Variant Weight Unit
        field_names[44] : "", #Variant Tax code
        field_names[45] : "" #Cost per item
    }

photo_packages = {}
schools = []
products = []

def customPhotoOrganizer():
    #read in the different schools
    with open(IMPORTANTcsv_folder_path + "School_Mapping.csv", 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            if row[0] not in schools and row[0] != "School":
                schools.append(row[0])

    #read in packages and prices
    with open(IMPORTANTcsv_folder_path + "Photography_Prices.csv",'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            photo_packages[row[0]] = row[1]

    #create products
    for school in schools:
        for package in photo_packages:
            newProduct = Product("Graduation Photography Custom Reservation",school,package)
            products.append(newProduct)


    with open(CREATED_folder_path + "custom-photography-organizer.csv", 'w', newline='') as csv_file:
        fout = csv.DictWriter(csv_file, fieldnames=field_names, restval="", extrasaction="ignore", delimiter=",")
        fout.writeheader()
        previous_handle = ""
        for product in products:
            newLine = Line()
            newLine.dict["Handle"] = product.title.replace(' ','-').lower()
            newLine.dict["Body (HTML)"] = "Request a time and date for photography here. We'll match you up with a local photographer. If no photographer is available to take your booking, your money will be refunded within 48 hours."
            if newLine.dict["Handle"] != previous_handle:
                newLine.dict["Title"] = product.title
                newLine.dict["Tags"] = "meta-related-collection-graduation-accessories, photography"
            else:
                newLine.dict["Title"] = ""
                newLine.dict["Tags"] = ""
            newLine.dict["Option1 Value"] = product.school
            newLine.dict["Option2 Value"] = product.package
            newLine.dict["Variant Price"] = photo_packages[product.package]
            fout.writerow(newLine.dict)
            previous_handle = newLine.dict["Handle"]

customPhotoOrganizer()
