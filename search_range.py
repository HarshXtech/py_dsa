def search_range(nums, target):

    # To find the range using binary tree, we will split the function in two parts. 1) find first occurence, 2) find the last occurence. 

    def find_first_occurence(arr, target):
        start = 0
        end = len(arr) - 1 
        index = -1
    

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                index = mid
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                

        return index
    
    def find_last_occurence(arr, target):
        start = 0
        end = len(arr) - 1
        index = -1

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                index = mid
                start = mid + 1
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        
        return index

    first = find_first_occurence(nums, target)
    last = find_last_occurence(nums, target)

    return [first, last]





print(search_range([5, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9,10], 9))
