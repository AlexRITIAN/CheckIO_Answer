'''
 * @Author: yuhao 
 * @Date: 2018-01-30 14:00:49 
 * @Last Modified by:   yuhao 
 * @Last Modified time: 2018-01-30 14:00:49 
'''


def checkio(data):
    results = []
    results_index = []
    final_list_index = 0
    max_lent = 0
    results_string = ""
    for i in range(len(data)):
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(data):
            # if data[i] == data[i+1]:
            left_str = data[j:i+1]
            right_str = data[i+1:k+2]
            if left_str == right_str[::-1]:
                index_list = []
                results.append(left_str + right_str)
                index_list.append(j)
                index_list.append(k+2)
                results_index.append(index_list)
            # else:
            left_str = data[j:i]
            right_str = data[i+1:k+1]
            if left_str == right_str[::-1]:
                index_list = []
                results.append(left_str + right_str)
                index_list.append(j)
                index_list.append(k+1)
                results_index.append(index_list)
            j = j - 1
            k = k + 1
    i = 0
    if 0 == len(results_index):
        return data[0]
    else:
        for in_list in results_index:
            lent = in_list[1] - in_list[0]
            if max_lent < lent:
                max_lent = lent
                final_list_index = i
            i = i + 1
        results_string = data[results_index[final_list_index][0]:results_index[final_list_index][1]]
        return results_string

#this is so gooder than me.I forget who code this,but it's awesome.

def substrings(string):
    l = len(string)
    for n in range(l, 0, -1):
        for i in range(l - n + 1):
            yield string[i:n+i]

def longest_palindromic(string):
    return next(sub for sub in substrings(string) if sub == sub[::-1])

if __name__ == "__main__":
    print(checkio("abarada"))
    print(checkio("artrartrt"))
    print(checkio("aaaa"))
    print(checkio("abc"))
    print(checkio("aaaaa"))

    print(longest_palindromic("abarada"))
    print(longest_palindromic("artrartrt"))
    print(longest_palindromic("aaaa"))
    print(longest_palindromic("abc"))
    print(longest_palindromic("aaaaa"))

    
