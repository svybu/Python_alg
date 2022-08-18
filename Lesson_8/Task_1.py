"""Определение количества различных подстрок с использованием хэш-функции.
 Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
  Требуется найти количество различных подстрок в этой строке."""
import hashlib

S = 'wlobgstogjldvrkpogkdcvvp'
N = int(len(S))

def find_them_all(S):
    s_arr, h_arr = [], []
    for i in range(1, N):
        for j in range(N - i + 1):
            k = hashlib.sha1(S[j:j + i].encode('utf-8')).hexdigest()
            if k not in h_arr:
                h_arr.append(k)
                s_arr.append(S[j:j + i])
    return f'в {S} найдено {len(s_arr)} подстрок: \n{s_arr}'

print(find_them_all(S))



