from fractions import gcd

frac1 = (20, 50)
frac2 = (30, 100)


def fraction_add(frac1, frac2):
    res = (frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1])
    GCD = gcd(*res)
    res = map(lambda x: x // GCD, res)
    return tuple(res)


def fraction_sub(frac1, frac2):
    res = (frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1])
    GCD = gcd(*res)
    res = map(lambda x: x // GCD, res)
    return tuple(res)


def fraction_mul(frac1, frac2):
    res = (frac1[0] * frac2[0], frac1[1] * frac2[1])
    GCD = gcd(*res)
    res = map(lambda x: x // GCD, res)
    return tuple(res)


def fraction_div(frac1, frac2):
    res = (frac1[0] * frac2[1], frac1[1] * frac2[0])
    GCD = gcd(*res)
    res = map(lambda x: x // GCD, res)
    return tuple(res)


def fraction_smpl(frac):
    if frac[0]/frac[1] >= 1:
        return frac[0]//frac[1], (frac[0]%frac[1], frac[1])
    else:
        return 0, (frac[0], frac[1])



res = fraction_smpl(fraction_add(fraction_add(frac1, frac1), frac2))
print(res)
