import math
import string
import json
import time


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1)):
        if n != x and n % x == 0:
            return False
    return True


start = time.time()
primes = [p for p in range(3, 150) if is_prime(p)]


def calculate_prime_value(string_value):
    prod = -1
    for l in string_value:
        try:
            idx = string.ascii_lowercase.index(l)
            prime_value = primes[idx]
        except Exception:
            # print('Trouble with: {} in {} because {}'.format(l, str, ex))
            prime_value = 0
        if prod < 0:
            prod = prime_value
        else:
            prod *= prime_value
    return prod


# reverse lookup dictionary - anagrams with same value keyed by value
anagram_primes_reverse = {}

with open('20k.txt') as fd:
    complete = False
    loaded_words = []
    while not complete:
        try:
            for line in fd:
                word = line.strip()
                if "'" not in word and word not in loaded_words:
                    loaded_words.append(word)
                    prime = calculate_prime_value(word)
                    if prime != 0:
                        # print('{} {}'.format(word, prime))
                        if prime in anagram_primes_reverse:
                            words = anagram_primes_reverse[prime]
                            words.append(word)
                        else:
                            words = list()
                            words.append(word)
                        anagram_primes_reverse[prime] = words
        except UnicodeDecodeError as err:
            print('error {} '.format(err))
            pass
        else:
            complete = True

with open('c:/tmp/anagrams_reverse.json', 'w') as fd:
    prime_anagram = []
    x = 0
    for reverse in anagram_primes_reverse:
        if x < 25:
            PutRequest = {}
            pjson = {"N": str(reverse)}
            wjson = {"S": ",".join(anagram_primes_reverse[reverse])}
            PutRequest["Item"] = {"prime": pjson, "words": wjson}
            prime_anagram.append({"PutRequest": PutRequest})
            x += 1
        else:
            fd.write('{}\n'.format(json.dumps({"prime_anagram": prime_anagram}, sort_keys=True,
                                              indent=4, separators=(',', ': '))))
            prime_anagram = []
            x = 0


end = time.time()
print('start={} end={} elapsed={}'.format(start, end, end - start))
