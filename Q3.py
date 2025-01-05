#Time: 30 Mins 44 Secs
def findMedianOfSortedArr(nums1, nums2):
    #O(log(m + n)) --> use binary search
    A, B = nums1, nums2
    
    #total length of both nums
    total = len(A) + len(B)
    #midpoint
    half = total // 2

    left, right = 0, len(A) - 1
    while True:
        midA = (right + left) // 2
        midB = half - (midA + 1) - 1

        leftA = A[midA] if midA >= 0 else float("-infinity")
        rightA = A[midA + 1] if midA + 1 < len(A) else float("infinity")
        leftB = B[midB] if midB >= 0 else float("-infinity")
        rightB = B[midB + 1] if midB + 1 < len(B) else float("infinity")

        if leftA <= rightB and leftB <= rightA: #if median is valid
            if total % 2: #if odd
                return min(rightA, rightB)
            else:
                return float(max(leftA, leftB) + min(rightA, rightB))/ 2
        elif leftA > rightB:
            right = midA - 1
        else:
            left = midA + 1

print(findMedianOfSortedArr([1,2,3,4,5,6,7,8],[1,2,3,4,5]))
#[1,1,2,2,3,3,4,4,5,5,6,7,8]

