class Nguoi:
    def __init__(self,maDinhDanh, tenNguoi):
        self.maDinhDanh=maDinhDanh
        self.tenNguoi=tenNguoi
    def nhapThongTin(self):
        self.maDinhDanh=input("Nhap ma dinh danh:")
        self.tenNguoi=input("Nhap ten:")
    def xuatThongTin(self):
        print("Ma dinh danh: ",self.maDinhDanh)
        print("Ten: ",self.tenNguoi)

class NhanVien(Nguoi):
    def __init__(self,maDinhDanh,tenNguoi,namSinh,heSoLuong):
        super().__init__(maDinhDanh,tenNguoi)
        self.namSinh=namSinh
        self.heSoLuong=heSoLuong

    tienPhuCap= 500

    def nhapThongTin(self):
        super().nhapThongTin()
        self.namSinh=int(input("Nhap nam sinh: "))
        self.heSoLuong=float(input("Nhap he so luong: "))

    def xuatThongTin(self):
        super().xuatThongTin()
        print("Nam sinh: ",self.namSinh)
        print("He so luong: ",self.heSoLuong)
        print("Luong",self.tinhLuong())

    def tinhLuong(self):

        return self.heSoLuong*1550+ self.tienPhuCap
    def __gt__(self,other):   
        return self.heSoLuong > other.heSoLuong
    
def main():
    # Nhập thông tin của một người
    print("Nhập thông tin của một người:")
    nguoi = Nguoi("", "")
    nguoi.nhapThongTin()
    print("\nThông tin người:")
    nguoi.xuatThongTin()

    # Nhập thông tin cho n nhân viên
    n = int(input("\nNhập số lượng nhân viên: "))
    nhan_viens = []
    for i in range(n):
        print(f"\nNhập thông tin nhân viên thứ {i+1}:")
        nhan_vien = NhanVien("", "", 0, 0.0)
        nhan_vien.nhapThongTin()
        nhan_viens.append(nhan_vien)

    # In thông tin của n nhân viên cùng với lương
    print("\nThông tin của n nhân viên cùng với lương:")
    for nhan_vien in nhan_viens:
        nhan_vien.xuatThongTin()

    # Sắp xếp danh sách nhân viên theo thứ tự giảm dần theo hệ số lương
    nhan_viens.sort(reverse=True)
    print("\nDanh sách nhân viên sau khi sắp xếp theo hệ số lương giảm dần:")
    for nhan_vien in nhan_viens:
        nhan_vien.xuatThongTin()
    main()