# reads in raw XX_Codes_2019 files to create the generic products
# output a csv file formatted for Shopify product import function
# meant to just add the generic parent BUNDLE products, nothing else

import csv


IMPORTANTcsv_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED_folder_path = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"

field_names = ["Handle", "Title", "Body (HTML)", "Vendor",
    "Type", "Tags", "Published", "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value",
    "Option3 Name", "Option3 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty",
    "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare at Price",
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position", "Image Alt Text",
    "Gift Card", "Seo Title", "Seo Description","Google Shopping / Google Product Category", "Google Shopping / Gender",
    "Google Shopping / Age Group", "Google Shopping / MPN", "Google Shopping / Adwords Grouping", "Google Shopping / Adwords Labels",
    "Google Shopping / Condition",  "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1",
    "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", "Variant Image",
    "Variant Weight Unit", "Variant Tax Code", "Cost per item" ]


class Line:
    dict = { #default values for a gown product
        field_names[0] : "",  #Handle
        field_names[1] : "",   #Title
        field_names[2] : "",    #Body (HTML)
        field_names[3] : "GradStreet", #vendor
        field_names[4] : "generic gown bundle", #type
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
        field_names[15] : "shopify", #Variant Inventory Tracker
        # field_names[16] : "0", #Variant Inventory Qty
        field_names[17] : "deny", #Variant Inventory Policy ("continue" allows sales after inventory of 0)
        field_names[18] : "manual", #Variant Fulfilment Service
        field_names[19] : "", #Variant Price
        field_names[20] : "", #Variant Compare at Price
        field_names[21] : "TRUE", #Variant Requires Shipping
        field_names[22] : "TRUE", #Variant Taxable
        field_names[23] : "", #Variant Barcode
        field_names[24] : "", #Image Src
        field_names[25] : "", #Image Position
        field_names[26] : "", #Image Alt Text
        field_names[27] : "FALSE", #Gift Card
        field_names[28] : "", #SEO Title
        field_names[29] : "", #SEO Description
        field_names[30] : "", #google shopping stuff --
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
        field_names[42] : "",
        field_names[43] : "", #Variant Image
        field_names[44] : "kg", #Variant Weight Unit
        field_names[45] : "", #Variant Tax code
        field_names[46] : "" #Cost per item
    }

colors = {}
sizes = {}
fits = {}
gownstyles = {}
degreetypes ={}
msku_fnsku = {}

def skuBuilder(degreetype,gownstyle,color,fit,size):
    sku = []
    sku.append("U")
    sku.append(degreetype)
    sku.append("C") # add a cap
    sku.append("017") # all gowns are black
    sku.append(gownstyle)
    sku.append(fit)
    sku.append(size)
    sku.append("T0") # with tassel
    sku.append(color)
    sku.append("0")
    sku.append("K01") # ALL YEAR TAGS
    return ''.join(sku)


def genericProductOrganizer():
    with open(IMPORTANTcsv_folder_path + "Color_Codes_2019.csv", 'r') as csv_file:   # read in the color codes
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            colors[row[0]] = row[1]
    with open(IMPORTANTcsv_folder_path + "Size_Codes_2019.csv", 'r') as csv_file: # read in the size codes
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            sizes[row[0]] = row[1]
    with open(IMPORTANTcsv_folder_path + "Fit_Codes_2019.csv", 'r') as csv_file: # read in the fit codes
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            fits[row[0]] = row[1]
    with open(IMPORTANTcsv_folder_path + "GownStyle_Codes_2019.csv", 'r') as csv_file: # read in the gown style codes
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            gownstyles[row[0]] = row[1]
    with open(IMPORTANTcsv_folder_path + "DegreeType_Codes_2019.csv", 'r') as csv_file: # read in degree type codes
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            degreetypes[row[0]] = row[1]

    # read in the MSKU_FNSKU mapping
    with open(IMPORTANTcsv_folder_path + "MSKU_FNSKU_ASIN.csv",'r') as csv_file: # now let's make the fnsku dictionary
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            msku_fnsku[row[0]] = row[1]

    # reads in ORDER_AGGREGATE_BUNDLED to get initial inventory quantities
    bundle_quantities = {}
    with open(IMPORTANTcsv_folder_path + "ORDER_AGGREGATE_BUNDLED (8).csv", 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        for row in fin:
            if row[0].isdigit():
                bundle_quantities[row[5]] = row[0]

    # now time to write the new file
    with open(CREATED_folder_path + "generic-product-organizer.csv", 'w', newline='') as csv_file:
        fout = csv.DictWriter(csv_file, fieldnames=field_names, restval="", extrasaction="ignore", delimiter=",")
        fout.writeheader()
        alt = "1"
        previous_handle = ""
        for degreetype in degreetypes:
            for gownstyle in gownstyles:
                for color in colors:
                    for fit in fits:
                        for size in sizes:
                            newLine = Line()

                            handle = "generic-" + degreetypes[degreetype].lower() + "-" + gownstyles[gownstyle].lower() + "-" + colors[color].lower()
                            newLine.dict["Handle"] = handle

                            title = "Generic " + degreetypes[degreetype] + " Cap and Gown " + gownstyles[gownstyle].lower() + " with " + colors[color] + " tassel"
                            if handle == previous_handle: newLine.dict["Title"] = ""
                            else: newLine.dict["Title"] = title

                            body = "This is a generic " + degreetypes[degreetype].lower() + " cap and gown (" + gownstyles[gownstyle].lower() + ") paired with a " + colors[color] + " tassel."
                            newLine.dict["Body (HTML)"] = body

                            tags = "\"generic, parent\""
                            if handle == previous_handle:
                                newLine.dict["Tags"] = ""
                            else:
                                newLine.dict["Tags"] = tags

                            newLine.dict["Option1 Value"] = sizes[size]
                            newLine.dict["Option2 Value"] = fits[fit]

                            variant_sku = skuBuilder(degreetype,gownstyle,color,fit,size)
                            newLine.dict["Variant SKU"] = variant_sku

                            try:
                                variant_barcode = msku_fnsku[variant_sku]
                            except:
                                variant_barcode = ""
                            newLine.dict["Variant Barcode"] = variant_barcode

                            if degreetypes[degreetype].lower() == "bachelors":
                                variant_price = 34.99
                            else:
                                variant_price = 44.99
                            newLine.dict["Variant Price"] = variant_price

                            image_src = "https://cdn.shopify.com/s/files/1/1766/6171/files/" + variant_sku[12:18] + "_" + alt + ".jpg?4286832225318832821"
                            newLine.dict["Image Src"] = image_src

                            fout.writerow(newLine.dict)

                            previous_handle = handle
                            if alt == "0": alt = "1"
                            else: alt = "0"

genericProductOrganizer()
