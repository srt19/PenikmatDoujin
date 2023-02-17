def dash(a):
    a[0] = int(a[0])
    a[1] = int(a[1])
    return a

def comma(a):
    for i, n in zip(a, range(len(a))):
        a[n] = int(i)
    return a

def total_chapter(no):
    if no == None:
        return None, "all"

    else:
        if "," in no:
            a = no.split(',')
            chn = comma(a)
            return chn, "comma"

        elif "-" in no:
            a = no.split('-')
            chn = dash(a)
            return chn, "dash"

        else:
            return int(no), "single"
