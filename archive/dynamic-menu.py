import types
import classes_and_functions
def create_menu(module):
    menu = (','.join([str(module.__dict__.get(a).__name__)
    for a in dir(classes_and_functions)
        if isinstance(module.__dict__.get(a), types.FunctionType)])).split(',')
    main_menu = { "0" : "Quit" }
    count = 1
    for x in menu:
        main_menu.update( {str(count) : x} )
        count += 1
    return main_menu

main_menu = create_menu(classes_and_functions)
print(main_menu)
