def fizzbuzz_counts(n):
    counts = {"fizz": 0, "buzz": 0, "fizzbuzz": 0}
    
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            counts["fizzbuzz"] += 1
        elif number % 3 == 0:
            counts["fizz"] += 1
        elif number % 5 == 0:
            counts["buzz"] += 1

    return counts