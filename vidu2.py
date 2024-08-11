class DongVat:
    def __init__(self,tenLoai,Ten,chieuCao,canNang):
        self.tenLoai=tenLoai
        self.Ten=Ten
        self.chieuCao=chieuCao
        self.canNang=canNang
    
    def tiengKeu(self):
        print("Chua biet")

    def Xuat(self):
        print("Loai: {0}, Ten: {1}, Chieu cao: {2}, Can nang: {3}".format(self.tenLoai,self.Ten,self.chieuCao,self.canNang))
    
class Cho(DongVat):
    def __init__(self,Ten,chieuCao,canNang,mauSac):
        DongVat.__init__(self,"Cho",Ten,chieuCao,canNang)
        self.mauSac=mauSac
    
    def tiengKeu(self):
        print("{0}:Gau gau".format(self.Ten))
    
    def giuNha(self):
        print("{0}: Gruuuuu".format(self.Ten))

class Meo(DongVat):
    def __init__(self,Ten,chieuCao,canNang,mauSac,gioiTinh):
        DongVat.__init__(self,"Meo",Ten,chieuCao,canNang)
        self.mauSac=mauSac
        self.gioiTinh=gioiTinh

    def tiengKeu(self):
        print("{0}:Meowwww".format(self.Ten))

a=Cho("Mina","20cm","30kg","Den")
b=Meo("Meo","10cm","15kg","Vang","Duc")
a.Xuat()
a.tiengKeu()
a.giuNha()
b.Xuat()
b.tiengKeu()

       