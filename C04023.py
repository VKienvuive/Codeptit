# low : cs bat dau . high : cs ket thuc 
def partition(arr, low, high):
    """""
    Hàm phân vùng: Chọn phần tử cuối cùng làm chốt (pivot),
    đưa các phần tử nhỏ hơn chốt về bên trái, lớn hơn về bên phải.
    """
    pivot = arr[high] # chon phan tu cuoi lam chot 
    i = low - 1  # chi so cua phan tu nho hon chot
    for j in range(low, high):
        if arr[j] <= pivot: # neu phan tu hien tai nho hon hoac bang chot
            i += 1 # tang chi so phan tu nho hon
            arr[i], arr[j] = arr[j], arr[i] # doi cho
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # doi cho phan tu chot ve vi tri giua hai phan vung
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi la chi so phan vung , arr[pi] da nam dung vi tri 
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1) # de quy mang ben trai
        quick_sort(arr, pi + 1, high) # de quy mang ben phai

n = int(input())
a = list(map(int, input().split()))
quick_sort(a, 0, n - 1)
print(*a)


