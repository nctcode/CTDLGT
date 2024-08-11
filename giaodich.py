class GiaoDich:
    def __init__(self,maGiaoDich,ngayGiaoDich,donGia,soLuong):
        self.maGiaoDich=maGiaoDich
        self.ngayGiaoDich=ngayGiaoDich
        self.donGia=donGia
        self.soLuong=soLuong
    
    def tinhThanhTien(self):
        pass

class GiaoDichVang(GiaoDich):
    def __init__(self, maGiaoDich, ngayGiaoDich, donGia, soLuong,loaiVang):
        super().__init__(maGiaoDich, ngayGiaoDich, donGia, soLuong)
        self.loaiVang=loaiVang
    def tinhThanhTien(self):
        return self.soLuong*self.donGia
    
class GiaoDichTienTe(GiaoDich):
    def __init__(self, maGiaoDich, ngayGiaoDich, donGia, soLuong, loaiTienTe, loaiGiaoDich):
        super().__init__(maGiaoDich, ngayGiaoDich, donGia, soLuong)
        self.loaiTienTe=loaiTienTe
        self.loaiGiaoDich=loaiGiaoDich
    
    def tinhThanhTien(self):
        if self.loaiGiaoDich =="mua":
            return self.soLuong*self.donGia
        elif self.loaiGiaoDich=="ban":
            return (self.soLuong*self.donGia)*1.05
        
def NhapGiaoDich():
    DanhSachGD=[]
    soLuongGD=input("Nhap so luong GD: ")
    for i in range(soLuongGD):
        loaiGiaoDich=input("Nhap loai giao dich vang/tiente: ")
        maGiaoDich=input("Nhap ma giao dich: ")
        ngayGiaoDich=input("Nhap ngay giao dich ngay/thang/nam: ")
        donGia=float(input("Nhap don gia: "))
        soLuong=int(input("Nhap so luong: "))
        if loaiGiaoDich=="vang":
            loaiVang =input("Nhap loai vang 18k/24k/999: ")
            giaoDich=GiaoDichVang(maGiaoDich,ngayGiaoDich,donGia,soLuong,loaiVang)
        elif loaiGiaoDich=="tiente":
            loaiTienTe=input("Nhap loai tien te USD/EURO/AUD: ")
            giaoDich=GiaoDichTienTe(maGiaoDich,ngayGiaoDich,donGia,soLuong,loaiTienTe,loaiGiaoDichTienTe)
        DanhSachGD.addpend(giaoDich)
    return DanhSachGD


    


    