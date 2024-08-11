class GiaoDich:
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong):
        self.ma_giao_dich = ma_giao_dich
        self.ngay_giao_dich = ngay_giao_dich
        self.don_gia = don_gia
        self.so_luong = so_luong

    def tinh_thanh_tien(self):
        pass


class GiaoDichVang(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_vang):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai_vang = loai_vang

    def tinh_thanh_tien(self):
        return self.so_luong * self.don_gia


class GiaoDichTienTe(GiaoDich):
    def __init__(self, ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_tien_te, loai_giao_dich):
        super().__init__(ma_giao_dich, ngay_giao_dich, don_gia, so_luong)
        self.loai_tien_te = loai_tien_te
        self.loai_giao_dich = loai_giao_dich

    def tinh_thanh_tien(self):
        if self.loai_giao_dich == "mua":
            return self.so_luong * self.don_gia
        elif self.loai_giao_dich == "bán":
            return (self.so_luong * self.don_gia) * 1.05


def nhap_danh_sach_giao_dich():
    danh_sach_giao_dich = []
    so_luong_giao_dich = int(input("Nhập số lượng giao dịch: "))
    for i in range(so_luong_giao_dich):
        loai_giao_dich = input("Nhập loại giao dịch (vang/tiente): ")
        ma_giao_dich = input("Nhập mã giao dịch: ")
        ngay_giao_dich = input("Nhập ngày giao dịch (ngày/tháng/năm): ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        if loai_giao_dich == "vang":
            loai_vang = input("Nhập loại vàng (18k/24k/9999): ")
            giao_dich = GiaoDichVang(ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_vang)
        elif loai_giao_dich == "tiente":
            loai_tien_te = input("Nhập loại tiền tệ (USD/EUR/AUD): ")
            loai_giao_dich_tiente = input("Nhập loại giao dịch (mua/bán): ")
            giao_dich = GiaoDichTienTe(ma_giao_dich, ngay_giao_dich, don_gia, so_luong, loai_tien_te, loai_giao_dich_tiente)
        danh_sach_giao_dich.append(giao_dich)
    return danh_sach_giao_dich


def xuat_danh_sach_giao_dich(danh_sach_giao_dich):
    for giao_dich in danh_sach_giao_dich:
        if isinstance(giao_dich, GiaoDichVang):
            print("Giao dịch vàng - Mã:", giao_dich.ma_giao_dich)
        elif isinstance(giao_dich, GiaoDichTienTe):
            print("Giao dịch tiền tệ - Mã:", giao_dich.ma_giao_dich)
        print("Ngày giao dịch:", giao_dich.ngay_giao_dich)
        print("Thành tiền:", giao_dich.tinh_thanh_tien())


def tinh_tong_so_luong_va_thanh_tien(danh_sach_giao_dich):
    tong_so_luong_vang = 0
    tong_thanh_tien_vang = 0
    tong_so_luong_tiente = 0
    tong_thanh_tien_tiente = 0

    for giao_dich in danh_sach_giao_dich:
        if isinstance(giao_dich, GiaoDichVang):
            tong_so_luong_vang += giao_dich.so_luong
            tong_thanh_tien_vang += giao_dich.tinh_thanh_tien()
        elif isinstance(giao_dich, GiaoDichTienTe):
            tong_so_luong_tiente += giao_dich.so_luong
            tong_thanh_tien_tiente += giao_dich.tinh_thanh_tien()

    print("Tổng số lượng vàng:", tong_so_luong_vang)
    print("Tổng thành tiền vàng:", tong_thanh_tien_vang)
    print("Tổng số lượng tiền tệ:", tong_so_luong_tiente)
    print("Tổng thành tiền tiền tệ:", tong_thanh_tien_tiente)


# Chạy chương trình
danh_sach_giao_dich = nhap_danh_sach_giao_dich()
xuat_danh_sach_giao_dich(danh_sach_giao_dich)
tinh_tong_so_luong_va_thanh_tien(danh_sach_giao_dich)
