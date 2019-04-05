import inventory
import argparse
import dev_tools

def doNothing():
    pass

func_mapping = {
    # dev_menu
    "Delete all Stores" : dev_tools.deleteAllStores,

    # menuA option 2
    "Update/View Inventory" : doNothing,

    "Update/View a Store" : doNothing,
    "Update/View a Collection" : doNothing,
    "Update/View a Product" : doNothing,
    "Update/View an Option" : doNothing,
    "Update/View a Variant" : doNothing,

    "Create a Store" : inventory.createStore,
    "Create a Collection" : inventory.createCollection,
    "Create a Product" : inventory.createProduct,
    "Create an Option" : inventory.createOption,
    "Create a Variant" : inventory.createVariant,

    "Delete a Store" : inventory.deleteStore,
    #"Delete a Collection" : inventory.deleteCollection, # <------------------------[ TO DO ]
    #"Delete a Product" : inventory.deleteProduct,# <------------------------[ TO DO ]
    #"Delete an Option" : inventory.deleteOption,# <------------------------[ TO DO ]
    #"Delete a Variant" : inventory.deleteVariant,# <------------------------[ TO DO ]

    #"Edit/View a Store" : editViewStore, # <------------------------[ TO DO ]
    #"Edit/View a Collection" : editViewCollection,  # <------------------------[ TO DO ]
    #"Edit/View a Product" : editViewProduct,  # <------------------------[ TO DO ]
    #"Edit/View an Option" : editViewOption,  # <------------------------[ TO DO ]
    #"Edit/View a Variant" : editViewVariant,  # <------------------------[ TO DO ]

    # menuA option 3
    "Update/View Orders" : doNothing,

    "Update/View Order Drafts" : doNothing,
    "Update/View Order Finals" : doNothing,

    #"Create an Order Draft" : createOrderDraft,  # <------------------------[ TO DO ]
    #"Create an Order Final" : createOrderFinal,  # <------------------------[ TO DO ]

    #"Delete an Order Draft" : deleteOrderDraft,  # <------------------------[ TO DO ]
    #"Delete an Order Final" : deleteOrderFinal,  # <------------------------[ TO DO ]

    #"Edit/View an Order Draft" : editViewOrderDraft,  # <------------------------[ TO DO ]
    #"Edit/View an Order Final" : editViewOrderFinal,  # <------------------------[ TO DO ]


    # menuA option 4
    "Update/View Reports" : doNothing,

    "Update/View Report Drafts" : doNothing,
    "Update/View Report Finals" : doNothing,

    #"Create a Report Draft" : createReportDraft,  # <------------------------[ TO DO ]
    #"Create a Report Final" : createReportFinal,  # <------------------------[ TO DO ]

    #"Delete a Report Draft" : deleteReportDraft,  # <------------------------[ TO DO ]
    #"Delete a Report Final" : deleteReportFinal,  # <------------------------[ TO DO ]

    #"Edit/View a Report Draft" : editViewReportDraft,  # <------------------------[ TO DO ]
    #"Edit/View a Report Final" : editViewReportFinal,  # <------------------------[ TO DO ]

    # menuA option 5
    "Update/View Store Settings" : doNothing,

    #"Edit/View Store Details" : editViewStoreDetails, <<------------------------[ TO DO ]
    #"Edit/View Tax Rates" : editViewTaxRates, <<------------------------[ TO DO ]

    #menuA option 6 <<------------------------[ TO DO ]
    "Update/View Manufacturers" : doNothing,

    #"Create new Manufacturer" : createManufacturer, <<------------------------[ TO DO ]
    #"Delete a Manufacturer" : deleteManufacturer, <<------------------------[ TO DO ]
    #"Edit/View a Manufacturer" : editViewManufacturer, <<------------------------[ TO DO ]

    #menuA option 7
    "Update/View Finances" : doNothing

    #"Edit/View Loans & Investments" : editViewLoansInvestments <<------------------------[ TO DO ]

}

### CORE CLASSES ###
class Session():
    current_menu_title = "menuA" # is a STRING
    menus = {

        "dev_menu" : ["Quit", "Back", "Delete all Stores"],

        ### MENUS ###
        "menuA" : ["Quit", "Back", "Update/View Inventory", "Update/View Orders", "Update/View Reports", "Update/View Store Settings", "Update/View Manufacturers", "Update/View Finances"],

        # Update/View Inventory
        "menuA_2" : ["Quit", "Back", "Update/View a Store", "Update/View a Collection", "Update/View a Product", "Update/View an Option", "Update/View a Variant"],
        # Update/View a Store
        "menuA_2_2" : ["Quit", "Back", "Create a Store", "Delete a Store", "Edit/View a Store"],
        # Update/View a Collection
        "menuA_2_3" : ["Quit", "Back", "Create a Collection", "Delete a Collection", "Edit/View a Collection"],
        # Update/View a Product
        "menuA_2_4" : ["Quit", "Back", "Create a Product", "Delete a Product", "Edit/View a Product"],
        # Update/View an Option
        "menuA_2_5" : ["Quit", "Back", "Create an Option", "Delete an Option", "Edit/View an Option"],
        # Update/View a Variant
        "menuA_2_6" : ["Quit", "Back", "Create a Variant", "Delete a Variant", "Edit/View a Variant"],

        # Update/View Orders
        "menuA_3" : ["Quit", "Back", "Update/View Order Drafts", "Update/View Order Finals"],
        # Update/View Order Drafts
        "menuA_3_2" : ["Quit", "Back", "Create an Order Draft", "Delete an Order Draft", "Edit/View an Order Draft"],
        # Update/View Order Finals
        "menuA_3_3" : ["Quit", "Back", "Create an Order Final", "Delete an Order Final", "Edit/View an Order Final"],

        # Update/View Projections
        "menuA_4" : ["Quit", "Back", "Update/View Report Drafts", "Update/View Report Finals"],
        # Update/View Report Drafts
        "menuA_4_2" : ["Quit", "Back", "Create a Report Draft", "Delete a Report Draft", "Edit/View a Report Draft"],
        # Update/View Report Finals
        "menuA_4_3" : ["Quit", "Back", "Create a Report Final", "Delete a Report Final", "Edit/View a Report Final"],

        # Update/View Store Settings
        "menuA_5" : ["Quit", "Back", "Edit/View Store Details", "Edit/View Tax Rates"],

        # Update/View Manufacturers
        "menuA_6" : ["Quit", "Back", "Create new Manufacturer", "Delete a Manufacturer", "Edit/View a Manufacturer"],

        # Update/View Finances
        "menuA_7" : ["Quit", "Back", "Edit/View Expenses", "Edit/View Revenue", "Update/View Loans & Investments"],
        # Update/View Loans & Investments
        "menuA_7_4" : ["Quit", "Back", "Active Loans & Investments", "Closed Loans & Investments"]
    }


### CORE FUNCTIONS ###


def menuPrint(some_session):
    count = 0
    new_menu = []
    if some_session.current_menu_title not in some_session.menus:
        print(".")
        return
    for x in some_session.menus[some_session.current_menu_title]:
        name = str(count) + "-" + x
        count += 1
        new_menu.append(name)
    print(new_menu)
    return

def priorMenuTitle(some_session):    # returns a string
    new_menu_title = some_session.current_menu_title[:-2]
    if len(new_menu_title) < 5:
        exit()
    return new_menu_title

def nextMenuTitle(some_session, some_number):
    if some_number == "0":
        exit()
    new_menu_title = some_session.current_menu_title + "_" + some_number
    return new_menu_title

def getMenuLength(some_session):
    return len(some_session.menus[some_session.current_menu_title])

def isValid(some_session, some_number):
    try:
        if (int(some_number) < 0) or (int(some_number) >= getMenuLength(some_session)):
            print("Selection is out of bounds")
            return False
        else:
            return True
    except:
        return False

def main(*some_session):
    if len(some_session) > 0:
        mySession = some_session[0]
    else:
        mySession = Session()
    menuPrint(mySession)
    ans = input()
    while isValid(mySession, ans):
        if ans == "0":
            exit()
        elif ans == "1":
            mySession.current_menu_title = priorMenuTitle(mySession)
            menuPrint(mySession)
            ans = input()
        else:
            selection = mySession.menus[mySession.current_menu_title][int(ans)]
            print("running" + str(func_mapping[selection]))
            func_mapping[selection]() # runs the selected function
            if func_mapping[selection] == doNothing:
                mySession.current_menu_title = nextMenuTitle(mySession,ans)
            menuPrint(mySession)
            ans = input()
    if ans == "d": # developer menu
        prior_menu = mySession.current_menu_title
        mySession.current_menu_title = "dev_menu"
        menuPrint(mySession)
        ans = input()
        while isValid(mySession, ans):
            if ans == "0":
                exit()
            elif ans == "1":
                mySession.current_menu_title = prior_menu
                main(mySession)
            else:
                selection = mySession.menus[mySession.current_menu_title][int(ans)]
                print("running" + str(func_mapping[selection]))
                func_mapping[selection]() # runs the selected function
                if func_mapping[selection] == doNothing:
                    mySession.current_menu_title = nextMenuTitle(mySession,ans)
                menuPrint(mySession)
                ans = input()
        print("Option not valid!")


main()
