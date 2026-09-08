def remove_duplicates(items):
    lists = []
    for item in items:
        if item not in lists:
            lists.append(item)

    return lists

remove_duplicates([1, 2, 2, 3, 1])
remove_duplicates(["a", "b", "a", "c"])
remove_duplicates([])
remove_duplicates([5, 5, 5])