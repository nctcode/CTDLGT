class NútCây:
    def __init__(self, giá_trị):
        self.giá_trị = giá_trị
        self.trái = None
        self.phải = None

class CâyNhịPhânTìmKiếm:
    def __init__(self):
        self.gốc = None

    def chèn(self, giá_trị):
        if not self.gốc:
            self.gốc = NútCây(giá_trị)
        else:
            self._chèn_đệ_quy(self.gốc, giá_trị)

    def _chèn_đệ_quy(self, nút, giá_trị):
        if giá_trị < nút.giá_trị:
            if not nút.trái:
                nút.trái = NútCây(giá_trị)
            else:
                self._chèn_đệ_quy(nút.trái, giá_trị)
        elif giá_trị > nút.giá_trị:
            if not nút.phải:
                nút.phải = NútCây(giá_trị)
            else:
                self._chèn_đệ_quy(nút.phải, giá_trị)

    def _là_số_nguyên_tố(self, số):
        if số < 2:
            return False
        for i in range(2, int(số**0.5) + 1):
            if số % i == 0:
                return False
        return True

    def _là_số_chính_phương(self, số):
        return số >= 0 and int(số**0.5)**2 == số

    def _đếm_số_nguyên_tố_đệ_quy(self, nút):
        if not nút:
            return 0
        đếm = 1 if self._là_số_nguyên_tố(nút.giá_trị) else 0
        return đếm + self._đếm_số_nguyên_tố_đệ_quy(nút.trái) + self._đếm_số_nguyên_tố_đệ_quy(nút.phải)

    def đếm_số_nguyên_tố(self):
        return self._đếm_số_nguyên_tố_đệ_quy(self.gốc)

    def _đếm_số_chính_phương_đệ_quy(self, nút):
        if not nút:
            return 0
        đếm = 1 if self._là_số_chính_phương(nút.giá_trị) else 0
        return đếm + self._đếm_số_chính_phương_đệ_quy(nút.trái) + self._đếm_số_chính_phương_đệ_quy(nút.phải)

    def đếm_số_chính_phương(self):
        return self._đếm_số_chính_phương_đệ_quy(self.gốc)

    def _đếm_số_chẵn_lẻ_đệ_quy(self, nút):
        if not nút:
            return (0, 0)
        chẵn = 1 if nút.giá_trị % 2 == 0 else 0
        lẻ = 1 if nút.giá_trị % 2 != 0 else 0
        chẵn_trái, lẻ_trái = self._đếm_số_chẵn_lẻ_đệ_quy(nút.trái)
        chẵn_phải, lẻ_phải = self._đếm_số_chẵn_lẻ_đệ_quy(nút.phải)
        return (chẵn + chẵn_trái + chẵn_phải, lẻ + lẻ_trái + lẻ_phải)

    def đếm_số_chẵn_lẻ(self):
        return self._đếm_số_chẵn_lẻ_đệ_quy(self.gốc)

    def tìm_max(self):
        if not self.gốc:
            return None
        nút = self.gốc
        while nút.phải:
            nút = nút.phải
        return nút.giá_trị

    def tìm_min(self):
        if not self.gốc:
            return None
        nút = self.gốc
        while nút.trái:
            nút = nút.trái
        return nút.giá_trị

    def _tìm_nút(self, nút, giá_trị):
        if not nút:
            return None
        if nút.giá_trị == giá_trị:
            return nút
        elif giá_trị < nút.giá_trị:
            return self._tìm_nút(nút.trái, giá_trị)
        else:
            return self._tìm_nút(nút.phải, giá_trị)

    def tìm_nút(self, giá_trị):
        return self._tìm_nút(self.gốc, giá_trị)

    def _duyệt_trước(self, nút, kết_quả):
        if nút:
            kết_quả.append(nút.giá_trị)
            self._duyệt_trước(nút.trái, kết_quả)
            self._duyệt_trước(nút.phải, kết_quả)

    def duyệt_trước(self):
        kết_quả = []
        self._duyệt_trước(self.gốc, kết_quả)
        return kết_quả

    def _duyệt_theo_chiều_rộng(self, nút):
        if not nút:
            return []
        hàng_đợi = [nút]
        kết_quả = []
        while hàng_đợi:
            hiện_tại = hàng_đợi.pop(0)
            kết_quả.append(hiện_tại.giá_trị)
            if hiện_tại.trái:
                hàng_đợi.append(hiện_tại.trái)
            if hiện_tại.phải:
                hàng_đợi.append(hiện_tại.phải)
        return kết_quả

    def duyệt_theo_chiều_rộng(self):
        return self._duyệt_theo_chiều_rộng(self.gốc)

    def _duyệt_theo_chiều_sâu(self, nút):
        if not nút:
            return []
        ngăn_xếp = [nút]
        kết_quả = []
        while ngăn_xếp:
            hiện_tại = ngăn_xếp.pop()
            kết_quả.append(hiện_tại.giá_trị)
            if hiện_tại.phải:
                ngăn_xếp.append(hiện_tại.phải)
            if hiện_tại.trái:
                ngăn_xếp.append(hiện_tại.trái)
        return kết_quả

    def duyệt_theo_chiều_sâu(self):
        return self._duyệt_theo_chiều_sâu(self.gốc)

    def _xóa_nút(self, nút, giá_trị):
        if not nút:
            return nút
        if giá_trị < nút.giá_trị:
            nút.trái = self._xóa_nút(nút.trái, giá_trị)
        elif giá_trị > nút.giá_trị:
            nút.phải = self._xóa_nút(nút.phải, giá_trị)
        else:
            if not nút.trái:
                return nút.phải
            elif not nút.phải:
                return nút.trái
            temp = self._tìm_nút_min(nút.phải)
            nút.giá_trị = temp.giá_trị
            nút.phải = self._xóa_nút(nút.phải, temp.giá_trị)
        return nút

    def xóa_nút(self, giá_trị):
        self.gốc = self._xóa_nút(self.gốc, giá_trị)

    def _tìm_nút_min(self, nút):
        hiện_tại = nút
        while hiện_tại.trái:
            hiện_tại = hiện_tại.trái
        return hiện_tại

    def _tìm_nút_max(self, nút):
        hiện_tại = nút
        while hiện_tại.phải:
            hiện_tại = hiện_tại.phải
        return hiện_tại

T= CâyNhịPhânTìmKiếm()
giá_trị = [6, 5, -3, 2, 12, -5, 9, 8, 1, 20]
for giá_trị in giá_trị:
    T.chèn(giá_trị)

print(T._đếm_số_nguyên_tố_đệ_quy(4))