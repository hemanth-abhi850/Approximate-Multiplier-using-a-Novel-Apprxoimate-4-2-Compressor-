def DTB(pxl):

    """ Input : Decimal Value ; Output : Binary string """

    tern = np.zeros(8, dtype="int")
    value = [2**(7 - i) for i in range(8)]

    for i in range(8):

        if pxl >= value[i]:
            tern[i] = pxl // value[i]
            pxl = pxl % value[i]

    tern = tern.astype("str")
    tern = "".join(tern)

    return tern
