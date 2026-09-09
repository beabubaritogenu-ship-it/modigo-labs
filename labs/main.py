def count_unique_visitors(visitors):
    results = []
    for visitor in visitors:
        if visitor not in results:
            results.append(visitor)
    return len(results)

count_unique_visitors(["Ada", "Bola", "Ada"])
count_unique_visitors([])
count_unique_visitors(["Chidi"])
count_unique_visitors(["Ada", "Ada", "Ada"])