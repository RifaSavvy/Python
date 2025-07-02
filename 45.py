def are_anagrams_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(are_anagrams_sort("listen", "silent"))  

