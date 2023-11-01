words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6

def check_len(words):
    return len(words) >= min_len

op = list(filter(check_len,words))
print(op)