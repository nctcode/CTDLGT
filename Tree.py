class Nut:
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    
    def chen(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return
    
        if khoa < self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa)
            else:
                self.trai.chen(khoa)
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                self.phai.chen(khoa) 
        else:
            print('Bi trung khoa ',khoa)

class CayNhiPhanTimKiem:
    def __init__(self, khoa = None):
        if khoa == None:
            self.goc = None
        else:
            self.goc = Nut(khoa)
    
    # Chen
    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:
            self.goc.chen(khoa)
    
    # Xoa
    def xoa(self, khoa):
        pass

    # LNR
    def duyet_trai_nut_phai(self, goc = 0):
        nut_ht = goc 
        if goc == 0:
            nut_ht = self.goc
        
        if nut_ht == None:
            return []
        else:
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            
            kq.append(nut_ht.khoa)
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq    
    
    # NLR
    def duyet_nut_trai_phai(self, goc = 0):
        nut_ht = goc 
        if goc == 0:
            nut_ht = self.goc
        
        if nut_ht == None:
            return []
        else:
            kq = []
            kq.append(nut_ht.khoa)

            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            return kq

    #LRN
    def duyet_trai_phai_nut(self, goc = 0):
        nut_ht = goc 
        if goc == 0:
            nut_ht = self.goc
        
        if nut_ht == None:
            return []
        else:
            kq = []

            kq_trai = self.duyet_trai_phai_nut(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            
            kq.append(nut_ht.khoa)

            return kq     

    # Tim
    def tim(self, khoa):
        if self.goc == None:
            return

        nut_ht = self.goc
        kq = ''
        while nut_ht != None and nut_ht.khoa != khoa:
            kq = kq + f'{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
        
        if nut_ht == None:
            return None
        else:
            kq = kq + f'{nut_ht.khoa}'
            return kq
        
def main():
    SoPhanTu = 7
    cay = CayNhiPhanTimKiem()
    print('---Chen vao cay---')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SoPhanTu:
        gt = randint(1, 100)
        tap_gia_tri.add(gt)

    tap_gia_tri = list(tap_gia_tri)
    tap_gia_tri = [27,14,35,10,19,31,42]

    print('Chen lan luot', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)

    print('---Duyet cay theo LNR---')
    kq = cay.duyet_trai_nut_phai()
    print(kq)

    print('---Duyet cay theo NLR---')
    kq = cay.duyet_nut_trai_phai()
    print(kq)

    print('---Duyet cay theo LRN---')
    kq = cay.duyet_trai_phai_nut()
    print(kq)

    while True:
        nhap = input('Nhap vao khoa can tim: ')
        if nhap == '':
            break

        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print('Khong tim thay ', gt)
        else:
            print('Tim thay {0}: {1}'.format(gt,kq))

if __name__ == '__main__':
    main()

