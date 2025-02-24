#Skończone
import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()
W = "time."

def naive(S, W):
    m = 0
    matches = 0
    comparisons = 0
    while m < len(S) - len(W) + 1:
        i = 0
        while i < len(W) and S[m + i] == W[i]:
            i += 1
            comparisons += 1
        if i == len(W):
            matches += 1
        m += 1
        comparisons += 1
    return matches, comparisons

d = 256 
q = 101

def hash(word):
    N = len(word)
    hw = 0
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W):
    M = len(S)
    N = len(W)
    hW = hash(W)
    matches = 0
    comparisons = 0
    collisions = 0
    m = 0
    
    h = 1
    for i in range(N - 1):
        h = (h*d)%q
    
    hS = hash(S[m:m + N])
    for m in range(M - N + 1):
        comparisons += 1
        if hS == hW:
            if S[m:m + N] == W:
                matches += 1
            else:
                collisions += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
    return matches, comparisons, collisions


def main():
    t_start = time.perf_counter()
    matches, comparisons = naive(S, W)
    t_stop = time.perf_counter()
    print(f"{matches};{comparisons}")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    matches, comparisons, collisions = rabin_karp(S, W)
    t_stop = time.perf_counter()
    print(f"{matches};{comparisons};{collisions}")
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

if __name__ == '__main__':
    main()