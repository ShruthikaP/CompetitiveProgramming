import unittest
import re
def word_cloud(input):
    end = r"\.|!|\?"
    s = re.split(end, input)
    freq = {}
    for i in s:
        words = re.split(r"[^a-zA-Z0-9-]+", i)
        for j in words:
            count = freq.get(j, 0)
            freq[j] = count + 1
    def is_cap(j):
        ch = j[0:1]
        return ch in j.upper()
    for j, count in freq.items():
        if is_cap(j) and j.lower() in freq:
            count = freq[j]
            freq[j.lower()] += count
            del freq[j]
    return freq