def sequence_a(n):
    if n == 0:
        return 1
    return 2*sequence_a(n-1) + 1