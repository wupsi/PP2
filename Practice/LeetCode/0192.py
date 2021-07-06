from collections import Counter
with open('words.txt') as txt:
    freq = dict(Counter(txt.read().split()))
    sorted_keys, sorted_freq = sorted(freq, key=freq.get), {}
    sorted_keys.reverse()
    for i in sorted_keys:
        sorted_freq[i] = freq[i]
    
    for key, value in sorted_freq.items():
        print(key, value)

# words.txt content:
'''
the day is sunny the the
the sunny is is
'''