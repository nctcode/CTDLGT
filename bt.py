from LinkedList import*


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
# def

if __name__ == '__main__':
    main()
#if 
