def next_greatest_letter(letters, target):
    
    left, right = 0, len(letters)

    while left < right:
        mid = (left + right) // 2

        if letters[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return letters[left % len(letters)]
        

print(next_greatest_letter(['c', 'f', 'j'], 'z'))
