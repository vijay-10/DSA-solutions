def searchInSorted(self,arr, N, K):
    start = 0
    end = N-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == K:
            return 1
        elif arr[mid] > K:
            end = mid-1
        else:
            start = mid+1
    return -1