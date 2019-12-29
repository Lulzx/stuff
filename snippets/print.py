def print_keeper(stuff):
    keeper = INTERESTED_ITEMS
    print("=" * 20)
    for k,v in stuff.items():
        if k in keeper.keys() and not (k == 'size' == '0'):
            print(f"{k} => {v}")


def print_item(item):
    for k, v in item.items():
        print(f"{k} => {v}")
