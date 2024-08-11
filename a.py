#1 Đảo ngược mảng (reverse)
a = [2,4,6,8]
a.reverse()
print(a)

#2 sắp xếp chẵn lẻ theo thứ tự chẵn trc lẻ sau (sort)
a = [3,8,1,6,7,4,2,5]
a.sort(key=lambda x: (x % 2, x))
print(a)

#3 Đếm số lượng phẩn tử lớn nhất
def soLuongPhanTuMax(arr):
    if not arr:
        return print("Mảng rỗng, không có phần tử")
    return print(f"Số lớn nhất: {max(arr)}, số lượng: {arr.count(max(arr))}")

a = [2, 4, 6, 8, 5, 8, 1, 8]
print(soLuongPhanTuMax(a))

#4 Xóa phần tử cụ thể ra khỏi mảng(remove)
a = [2, 4, 6, 8, 5, 8, 1, 8]
x = 2
if x in a:
    a.remove(x)
    print(f"Xoá phần tử {x} thành công")
else:
    print(f"Không có phần tử {x} cần xoá")




#5 Thêm vào mảng theo thứ tự (insert)
a5 = [1,3,4,6,7]
x5 = 2
a5.insert(1,x5)
print(a5)

#6
class Nguoi:
    def __init__(self, ma_dinh_danh, ten_nguoi):
        self.ma_dinh_danh = ma_dinh_danh
        self.ten_nguoi = ten_nguoi

    def nhap_thong_tin(self):
        self.ma_dinh_danh = input("Nhập mã định danh: ")
        self.ten_nguoi = input("Nhập tên người: ")

    def hien_thi_thong_tin(self):
        print("Mã định danh:", self.ma_dinh_danh)
        print("Tên người:", self.ten_nguoi)


class NhanVien(Nguoi):
    tien_phu_cap = 500  # Tiền phụ cấp

    def __init__(self, ma_dinh_danh, ten_nguoi, nam_sinh, he_so_luong):
        super().__init__(ma_dinh_danh, ten_nguoi)
        self.nam_sinh = nam_sinh
        self.he_so_luong = he_so_luong

    def nhap_thong_tin(self):
        super().nhap_thong_tin()
        self.nam_sinh = int(input("Nhập năm sinh: "))
        self.he_so_luong = float(input("Nhập hệ số lương: "))

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print("Năm sinh:", self.nam_sinh)
        print("Hệ số lương:", self.he_so_luong)
        print("Lương:", self.tinh_luong())

    def tinh_luong(self):
        return self.he_so_luong * 1550 + NhanVien.tien_phu_cap

    def __gt__(self, other):
        return self.he_so_luong > other.he_so_luong


def main():
    # Nhập thông tin của một người
    print("Nhập thông tin của một người:")
    nguoi = Nguoi("", "")
    nguoi.nhap_thong_tin()
    print("\nThông tin người:")
    nguoi.hien_thi_thong_tin()

    # Nhập thông tin cho n nhân viên
    n = int(input("\nNhập số lượng nhân viên: "))
    nhan_viens = []
    for i in range(n): 
        
        print(f"\nNhập thông tin nhân viên thứ {i+1}:")
        nhan_vien = NhanVien("", "", 0, 0.0)
        nhan_vien.nhap_thong_tin()
        nhan_viens.append(nhan_vien)

    # In thông tin của n nhân viên cù
    print("\nThông tin của n nhân viên cùng với lương:")
    for nhan_vien in nhan_viens:
        nhan_vien.hien_thi_thong_tin()

    # Sắp xếp danh sách nhân viên theo thứ tự giảm dần theo hệ số lương
    nhan_viens.sort(reverse=True)
    print("\nDanh sách nhân viên sau khi sắp xếp theo hệ số lương giảm dần:")
    for nhan_vien in nhan_viens:
        nhan_vien.hien_thi_thong_tin()

if __name__ == "__main__":
    main()