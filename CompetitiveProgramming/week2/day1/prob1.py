import unittests
def find_unique_delivery_id(lists):
    d1 = {}
    d2 = {}
    for id in lists:
        if id not in d2:
            if id in d1:
                del d1[id]
                d2[id] = True
            else:
                d1[id] = True
    for key in d1.keys():
        return key
    return None