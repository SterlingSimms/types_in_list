def list_types(aList):
    sentence = ""
    total = 0
    for item in aList:
        if isinstance(item, str):
            sentence += item + " "
        if isinstance(item, int) or isinstance(item, float):
            total += item
    if sentence == None:
        print "The list you entered is of integer type."
    if sentence == None:
        print "The list you entered is of a string type."
    else: 
        print "This list is of mixed type."
    print sentence
    print total
list_types(['magical unicorns',19,'hello',98.98,'world'])
