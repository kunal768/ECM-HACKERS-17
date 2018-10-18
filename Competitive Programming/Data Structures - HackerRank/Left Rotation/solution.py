n,rot = map(int,input().split())
nums = [int(i) for i in input().split()]
# Left Rotations Should be Based On Indexing and Slicing Thanks to Python
def rotate(l, n):
    return l[n:] + l[:n]
print(*rotate(nums,rot))
