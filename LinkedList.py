class Nut:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep=None
    # def
#class

class DSLienKet:
    def __init__(self):
        self.dau=None
        self.duoi=None
    # def
    def in_ds(self):
        stt = 0
        hien_tai = self.dau
        kq = 'DS['
        while hien_tai != None:
            stt += 1
            if stt == 1: # dau tien
                kq += ' ' + str(hien_tai.gia_tri)
            else: # 2 ve sau
                kq += ' -> ' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep    
        kq += ' ]'
        print(kq)
    
    # them
    def them(self,gia_tri):
        #them dau tien
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        #them cuoi 
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut

    
    def chen(self,chi_muc,gia_tri):
        nut = Nut(gia_tri)
        truoc = None
        hien_tai = self.dau
        i = 0
        while i < chi_muc and hien_tai != None:
            i += 1
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        # chen vao dau ds
        if truoc == None:
            nut.nut_ke_tiep = self.dau
            self.dau = nut
            if self.duoi == None:
                self.duoi = nut
        else:
             # chen vao cuoi ds
            if hien_tai == None: 
                self.duoi.nut_ke_tiep = nut
                self.duoi = nut
             # Them vao giua ds
            else:
                truoc.nut_ke_tiep = nut
                nut.nut_ke_tiep = hien_tai

    #tim
    def tim(self,gia_tri):
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            hien_tai = hien_tai.nut_ke_tiep
            vi_tri += 1
        
        if hien_tai == None:
            return None
        else:
            return vi_tri
    #xoa
    def xoa(self,gia_tri):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
        # Tim thay  
             # Xoa phan tu duy nhat
            if hien_tai == self.dau and hien_tai == self.duoi:   
                self.dau = self.duoi = None  
            # Xoa phan tu dau tien (khong duy nhat)
            elif hien_tai == self.dau: 
                self.dau = self.dau.nut_ke_tiep
            # Xoa phan tu duoi (khong duy nhat)
            elif hien_tai == self.duoi:
                truoc.nut_ke_tiep = None
                self.duoi = truoc
            # Xoa o giua
            else:   
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep

            del hien_tai  
    # Cap nhat
    def cap_nhat(self, vi_tri, gia_tri):
        hien_tai = self.dau
        i= 0
        while i < vi_tri and hien_tai != None:
            i += 1
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            hien_tai.gia_tri = gia_tri

    # Xoa het
    def xoa_het(self):
        hien_tai = self.dau
        self.dau = self.duoi = None
        while hien_tai != None:
            tam = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
            del tam
# class
def main():
    ds = DSLienKet()
    ds.in_ds()

    # them
    print('a: them---------------')
    ds.them(12)
    ds.in_ds()

    ds.them(10)
    ds.in_ds()

    # chen
    print('b: chen---------------')
    ds.chen(0,8)
    ds.in_ds()

    ds.chen(1,15)
    ds.in_ds()

    ds.chen(1,17)
    ds.in_ds()
    # tim
    print('c: tim-----------------')
    print(ds.tim(17))
    print(ds.tim(78))
    # xoa
    print('d: xoa-----------------')
    ds.xoa(8)
    ds.in_ds()

    ds.xoa(90)
    ds.in_ds()
    # cap nhat
    print('e: cap nhat------------')
    ds.cap_nhat(1,3)
    ds.in_ds()
    
    ds.cap_nhat(6,6)
    ds.in_ds()
    # xoa het
    print('f: xoa het-------------')
    ds.xoa_het()
    ds.in_ds()

if __name__ == '__main__':
    main()