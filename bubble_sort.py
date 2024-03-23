def bubble_sort(arr):
    # Get the length of the input array
    n = len(arr)
    
    # Iterate over the entire array
    for i in range(n):
        # Last i elements are already in place, so no need to check them again
        # Inner loop iterates over the unsorted portion of the array
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
if __name__ == "__main__":
    # Input array to be sorted
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Call bubble_sort function to sort the array
    bubble_sort(arr)
    
    # Print the sorted array
    print("Sorted array is:", arr)
