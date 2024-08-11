#1 Tìm phần tử xuất hiện duy nhất (count)
def xuatHienDuyNhat(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return "không có trong mảng"

a = [2, 4, 2, 8, 6, 8]
print(xuatHienDuyNhat(a))

#2 Liệt kê số chính phương
def chinhPhuong(arr):
    cp = [x for x in arr if x == int(x**0.5)**2]
    return cp

a = [15, 4, 9, 16, 3, 6]
print("Số chính phương là:",chinhPhuong(a))

#3 Xóa phần tử trùng lắp trong mảng (set)
a = [2, 4, 6, 8, 5, 8, 1, 8]
a=set(a)
print(a)

#4 Thêm vào vị trí cụ thể (insert)
a = [1, 3, 4, 6, 7]
vi_tri = 3
x = 8
a.insert(vi_tri,x)
print(a)

