#reads in Shopify's exported orders, and creates a txt file formatted for amazon's bulk order upload
# if status is not "PAID" it DGAF about it and ignored it basically

import csv
from datetime import datetime
from pytz import timezone
import pytz
from pytz import utc
from pytz import tzinfo

IMPORTANTcsv = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\IMPORTANT\\csv_files\\"
CREATED = "C:\\Users\\User\\Google Drive\\GradStreet\\InventoryTracker\\CREATED\\"
DOWNLOADS = "C:\\Users\\User\\Downloads\\"
shopify_file = "orders_export (3).csv"

AmazonHeaders = ["MerchantFulfillmentOrderID","DisplayableOrderID","DisplayableOrderDate","MerchantSKU","Quantity","MerchantFulfillmentOrderItemID",
"GiftMessage","DisplayableComment","PerUnitDeclaredValue","DisplayableOrderComment","DeliverySLA","AddressName","AddressFieldOne","AddressFieldTwo",
"AddressFieldThree","AddressCity","AddressCountryCode","AddressStateOrRegion","AddressPostalCode","AddressPhoneNumber","NotificationEmail"]

class Order:
    MerchantFulfillmentOrderID = ""
    DisplayableOrderID = ""
    DisplayableOrderDate = ""
    MerchantSKU = ""
    Quantity = ""
    MerchantFulfillmentOrderItemID = ""
    GiftMessage = ""
    DisplayableComment = ""
    PerUnitDeclaredValue = ""
    DisplayableOrderComment = ""
    DeliverySLA = ""
    AddressName = ""
    Address1 = ""
    Address2 = ""
    Address3 = ""
    AddressCity = ""
    AddressCountryCode = ""
    AddressStateOrRegion = ""
    AddressPostalCode = ""
    AddressPhoneNumber = ""
    NotificationEmail = ""
def changeToAmazonTime(date_time):
    dt = datetime.strptime(date_time, '%Y-%m-%d %X %z')
    dt = dt.astimezone(utc)
    return(dt.replace(tzinfo=None).isoformat())


def amazonBulkOrderUploader():
    orders = []
    with open(DOWNLOADS + shopify_file, 'r') as csv_file:
        fin = csv.reader(csv_file, delimiter=',')
        prior_id = ""
        main_paid_status = ""
        for row in fin:
            if row[0][0] != "#":
                continue
            else:
                newOrder = Order()

                newOrder.MerchantFulfillmentOrderID = row[0].replace('#','')
                print(newOrder.MerchantFulfillmentOrderID)

                if prior_id != newOrder.MerchantFulfillmentOrderID:
                    main_paid_status = row[2]

                if main_paid_status != "paid":
                    continue

                if prior_id == newOrder.MerchantFulfillmentOrderID: newOrder.DisplayableOrderID = ""
                else: newOrder.DisplayableOrderID = row[0].replace('#','')

                if prior_id == newOrder.MerchantFulfillmentOrderID:  newOrder.DisplayableOrderID = ""
                else: newOrder.DisplayableOrderDate = changeToAmazonTime(row[3])

                newOrder.MerchantSKU = row[20]
                newOrder.Quantity =  row[16]
                newOrder.MerchantFulfillmentOrderItemID = row[0].replace('#','')+row[20]
                newOrder.GiftMessage = ""
                newOrder.DisplayableComment = ""
                newOrder.PerUnitDeclaredValue = ""

                if prior_id == newOrder.MerchantFulfillmentOrderID:
                    newOrder.DisplayableOrderComment = ""
                    newOrder.DeliverySLA = ""
                    newOrder.AddressName = ""
                    newOrder.AddressFieldOne = ""
                    newOrder.AddressFieldTwo = ""
                    newOrder.AddressFieldThree = ""
                    newOrder.AddressCity = ""
                    newOrder.AddressCountryCode = ""
                    newOrder.AddressStateOrRegion = ""
                    newOrder.AddressPostalCode = ""
                    newOrder.AddressPhoneNumber = ""
                    newOrder.NotificationEmail = ""
                else:
                    newOrder.DisplayableOrderComment = "Thanks for using GradStreet! We'd love to hear your questions and comment! Drop us a line at team@gradstreet.com. You can review our shipping policy here: https://gradstreet.com/policies/shipping-policy"
                    newOrder.DeliverySLA = row[14]
                    newOrder.AddressName = row[34]
                    newOrder.AddressFieldOne = row[36]
                    newOrder.AddressFieldTwo = row[37]
                    newOrder.AddressFieldThree = row[38]
                    newOrder.AddressCity = row[39]
                    newOrder.AddressCountryCode = row[42]
                    newOrder.AddressStateOrRegion = row[41]
                    newOrder.AddressPostalCode = row[40].replace('\'','')
                    newOrder.AddressPhoneNumber = row[43]
                    newOrder.NotificationEmail = row[1]

                prior_id = newOrder.MerchantFulfillmentOrderID
                orders.append(newOrder)

    with open(CREATED + "amazon-bulk-order-upload-file.csv", 'w', newline='') as csv_file:
        fout = csv.writer(csv_file)
        fout.writerow(AmazonHeaders)
        previous_line_order_number = ['0']
        for order in orders:
            line = []
            for column in AmazonHeaders:
                line.append(getattr(order,column))
            fout.writerow(line)
            previous_line_order_number = line[0]

amazonBulkOrderUploader()
