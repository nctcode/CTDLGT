class Ngay:
    def __init__(self,ngay,thang,nam):
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
    @staticmethod
    def soNgayCuaThang(thang,nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif(thang in [4,6,9,11]):
            return 30
        elif(thang==2):
            if(nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
                return 29
            else:
                return 28
    
    def ngayTrongNam(self):
        giaTriNgayTrongNam=0
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x,self.nam)
        giaTriNgayTrongNam += self.ngay
        return giaTriNgayTrongNam
    
    def thangTrongNam(self):
        i=0
        for i in range()
a= Ngay(15,3,2004)
print("Ngay trong nam {0} la: {1}".format(a.nam,a.ngayTrongNam()))
    