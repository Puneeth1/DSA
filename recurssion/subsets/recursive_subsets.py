# TC : O(2^n)
# SC : O(n) -> At max n recursive calls can be in a stack
def return_subsequences(arr, index, subsequence):
    # Base case: if we've reached the end of the array, print the current subsequence
    if index == len(arr):
        return [subsequence]
    
    # Case 1: Exclude the current element and move to the next
    exclude = return_subsequences(arr, index + 1, subsequence)
    
    # Case 2: Include the current element in the subsequence and move to the next
    include = return_subsequences(arr, index + 1, subsequence + [arr[index]])
    
    # Combine both include and exclude results
    return exclude + include
    
    

# Example usage
arr = [1, 2, 3]
print(return_subsequences(arr, 0, []))