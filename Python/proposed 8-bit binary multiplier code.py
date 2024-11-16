def Binary_Multiply8(a, b):


      p77 = andg(int(a[7]),int(b[7]))
      p67 = andg(int(a[6]),int(b[7]))
      p57 = andg(int(a[5]),int(b[7]))
      p47 = andg(int(a[4]),int(b[7]))
      p37 = andg(int(a[3]),int(b[7]))
      p27 = andg(int(a[2]),int(b[7]))
      p17 = andg(int(a[1]),int(b[7]))
      p07 = andg(int(a[0]),int(b[7]))

      p76 = andg(int(a[7]),int(b[6]))
      p66 = andg(int(a[6]),int(b[6]))
      p56 = andg(int(a[5]),int(b[6]))
      p46 = andg(int(a[4]),int(b[6]))
      p36 = andg(int(a[3]),int(b[6]))
      p26 = andg(int(a[2]),int(b[6]))
      p16 = andg(int(a[1]),int(b[6]))
      p06 = andg(int(a[0]),int(b[6]))

      p75 = andg(int(a[7]),int(b[5]))
      p65 = andg(int(a[6]),int(b[5]))
      p55 = andg(int(a[5]),int(b[5]))
      p45 = andg(int(a[4]),int(b[5]))
      p35 = andg(int(a[3]),int(b[5]))
      p25 = andg(int(a[2]),int(b[5]))
      p15 = andg(int(a[1]),int(b[5]))
      p05 = andg(int(a[0]),int(b[5]))


      p74 = andg(int(a[7]),int(b[4]))
      p64 = andg(int(a[6]),int(b[4]))
      p54 = andg(int(a[5]),int(b[4]))
      p44 = andg(int(a[4]),int(b[4]))
      p34 = andg(int(a[3]),int(b[4]))
      p24 = andg(int(a[2]),int(b[4]))
      p14 = andg(int(a[1]),int(b[4]))
      p04 = andg(int(a[0]),int(b[4]))

      p73 = andg(int(a[7]),int(b[3]))
      p63 = andg(int(a[6]),int(b[3]))
      p53 = andg(int(a[5]),int(b[3]))
      p43 = andg(int(a[4]),int(b[3]))
      p33 = andg(int(a[3]),int(b[3]))
      p23 = andg(int(a[2]),int(b[3]))
      p13 = andg(int(a[1]),int(b[3]))
      p03 = andg(int(a[0]),int(b[3]))


      p72 = andg(int(a[7]),int(b[2]))
      p62 = andg(int(a[6]),int(b[2]))
      p52 = andg(int(a[5]),int(b[2]))
      p42 = andg(int(a[4]),int(b[2]))
      p32 = andg(int(a[3]),int(b[2]))
      p22 = andg(int(a[2]),int(b[2]))
      p12 = andg(int(a[1]),int(b[2]))
      p02 = andg(int(a[0]),int(b[2]))

      p71 = andg(int(a[7]),int(b[1]))
      p61 = andg(int(a[6]),int(b[1]))
      p51 = andg(int(a[5]),int(b[1]))
      p41 = andg(int(a[4]),int(b[1]))
      p31 = andg(int(a[3]),int(b[1]))
      p21 = andg(int(a[2]),int(b[1]))
      p11 = andg(int(a[1]),int(b[1]))
      p01 = andg(int(a[0]),int(b[1]))


      p70 = andg(int(a[7]),int(b[0]))
      p60 = andg(int(a[6]),int(b[0]))
      p50 = andg(int(a[5]),int(b[0]))
      p40 = andg(int(a[4]),int(b[0]))
      p30 = andg(int(a[3]),int(b[0]))
      p20 = andg(int(a[2]),int(b[0]))
      p10 = andg(int(a[1]),int(b[0]))
      p00 = andg(int(a[0]),int(b[0]))

            # FIRST STAGE

      cd1,cc1,cs1 = cmp(p27,p36,p45,p54,p63)
      cd2,cc2,cs2 = cmp(p17,p26,p35,p44,p53)
      cd3,cc3,cs3 = cmp(p07,p16,p25,p34,p43)
      cd4,cc4,cs4 = cmp(p06,p15,p24,p33,p42)
      cd5,cc5,cs5 = cmp(p05,p14,p23,p32,p41)

      fc1,fs1 = FA(p52,p61,p70)
      fc2,fs2 = FA(p04,p13,p22)

      hc1,hs1 = HA(p37,p46)
      hc2,hs2 = HA(p51,p60)

          # second stage

      cd6,cc6,cs6 = cmp(cc1,cd1,cs2,p62,p71)
      cd7,cc7,cs7 = cmp(cc2,cd2,cs3,fs1,cd6)
      cd8,cc8,cs8 = cmp(cd3,cc3,fc1,cs4,hs2)
      cd9,cc9,cs9 = cmp(cd4,cc4,hc2,cs5,p50)
      cd10,cc10,cs10= cmp(cd5,cc5,fs2,p31,p40)
      cd11,cc11,cs11 = cmp(fc2,p03,p12,p21,p30)

      hc3,hs3 = HA(p47,p56)

      fc3,fs3 = FA(hs1,p55,p64)
      fc4,fs4 = FA(hc1,p72,cs1)
      fc5,fs5 = FA(p02,p11,p20)

             # third stage

      hc4,hs4 = HA(p57,p66)

      fc6,fs6 = FA(hs3,p65,p74)
      fc7,fs7 = FA(fs3,hc3,p73)

      hc5,hs5 = HA(fc3,fs4)
      hc6,hs6 = HA(fc4,cs6)
      hc7,hs7 = HA(cc6,cs7)

      fc8,fs8 = FA(cd7,cc7,cs8)
      fc9,fs9 = FA(cd8,cc8,cs9)
      fc10,fs10 = FA(cd9,cc9,cs10)
      fc11,fs11 = FA(cd10,cc10,cs11)
      fc12,fs12 = FA(cd11,cc11,fs5)
      fc13,fs13 = FA(fc5,p01,p10)

            # third stage

      hc8,hs8 = HA(p67,p76)

      fc14,fs14 = FA(hs4,p75,hc8)
      fc15,fs15 = FA(hc4,fs6,fc14)
      fc16,fs16 = FA(fc6,fs7,fc15)
      fc17,fs17 = FA(fc7,hs5,fc16)

      fc18,fs18 = FA(hc5,hs6,fc17)
      fc19,fs19 = FA(hc6,hs7,fc18)
      fc20,fs20 = FA(hc7,fs8,fc19)
      fc21,fs21 = FA(fc8,fs9,fc20)

      fc22,fs22 = FA(fc9,fs10,fc21)
      fc23,fs23 = FA(fc10,fs11,fc22)
      fc24,fs24 = FA(fc11,fs12,fc23)
      fc25,fs25 = FA(fc12,fs13,fc24)
      fc26,fs26 = FA(p00,fc13,fc25)


      y = fc26,fs26,fs25,fs24,fs23,fs22,fs21,fs20,fs19,fs18,fs17,fs16,fs15,fs14,hs8,p77
      return y
