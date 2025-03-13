def factorial(n):
    if not isinstance(n, int):
        return "вводимое должно быть целым числом"
    if n < 0:
        return "Факториал не определен"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_unique(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    for item, count in counts.items():
        if count == 1:
            return item
    return None


def group_by_length(words):
    grouped = {}
    for word in words:
        length = len(word)
        if length not in grouped:
            grouped[length] = []
        grouped[length].append(word)
    return grouped
