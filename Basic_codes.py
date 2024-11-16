def HA(X, Y):

    bit_sum = np.array([[0,1], [1,0]])
    bit_carry = np.array([[0,0], [0,1]])

    return bit_carry[X][Y], bit_sum[X][Y]

def FA(x,y,z):
    c1,s1 = HA(x,y)
    c2,s2 = HA(s1,z)
    carry = c1 + c2
    return carry,s2

def cmp(p,q,r,s,t):  # exact 4:2 compressor
    cout,s1 = FA(p,q,r)
    carry,sum = FA(s1,s,t)
    return cout,carry,sum
