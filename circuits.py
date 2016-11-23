"""
Full Subtractor
http://www.flintgroups.com/2012/10/half-subtractor-and-full-subtractor.html
"""
def half_sub(a, b):
    borrow = ~a & b
    out   = a ^ b
    return out, borrow

def full_sub(a, b, bin):
    out, b1 = half_sub(a, b)
    out, b2 = half_sub(out, bin)
    bout = b1 | b2
    return out, bout


if __name__ == "__main__":
    print "a b c out borrow"
    for a in (0, 1):
        for b in (0, 1):
            for bin in (0, 1):
                print a, b, bin, full_sub(a, b, bin)