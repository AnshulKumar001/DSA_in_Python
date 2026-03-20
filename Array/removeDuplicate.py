def removeDuplicates(arr):
    seen = set()
    result = []
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example
print(removeDuplicates([1, 2, 2, 3, 4, 4]))   