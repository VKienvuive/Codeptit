danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while i < len(danh_sach_so):
    so_hien_tai = danh_sach_so[i]
    chu_so_cuoi = so_hien_tai % 10    
    for so_tiep_theo in range(chu_so_cuoi - 1, -1, -1):
        so_moi = so_hien_tai * 10 + so_tiep_theo
        danh_sach_so.append(so_moi) # Thêm số mới tạo vào cuối mảng
        
    i += 1 
t = int(input()) 
for _ in range(t):
    a, b = map(int, input().split())
    dem = 0
    for so in danh_sach_so:
        if a <= so <= b:
            dem += 1
            
    print(dem)