import math as _math

try:

    True, False

except NameError:

    True, False = 1, 0

 def chi2Q(x2, v, exp=_math.exp, min=min):

    """Return prob(chisq >= x2, with v degrees of freedom).
    v must be even.
    """

    assert v & 1 == 0

    m = x2 / 2.0

    sum = term = exp(-m)

    for i in range(1, v//2):

        term *= m / i

        sum += term

    return min(sum, 1.0)

 def normZ(z, sqrt2pi=_math.sqrt(2.0*_math.pi), exp=_math.exp):

    "Return value of the unit Gaussian at z."

    return exp(-z*z/2.0) / sqrt2pi

 def normP(z):

    """Return area under the unit Gaussian from -inf to z.
    This is the probability that a zscore is <= z.
    """

    a = abs(float(z))

    if a >= 8.3:

        sum = 0.5

    else:

        sum2 = term = a * normZ(a)

        z2 = a*a

        sum = 0.0

        i = 1.0

        while sum != sum2:

            sum = sum2

            i += 2.0

            term *= z2 / i

            sum2 += term

    if z >= 0:

        result = 0.5 + sum

    else:

        result = 0.5 - sum

    return result

 def normIQ(p, sqrt=_math.sqrt, ln=_math.log):

    """Return z such that the area under the unit Gaussian from z to +inf is p.
    Must have 0.0 <= p <= 1.0.
    """

    assert 0.0 <= p <= 1.0

    flipped = False

    if p > 0.5:

        flipped = True

        p = 1.0 - p

    if p == 0.0:

        z = 8.3

    else:

        t = sqrt(-2.0 * ln(p))

        z = t - (2.30753 + .27061*t) / (1. + .99229*t + .04481*t**2)

    if flipped:

        z = -z

    return z

 def normIP(p):

    """Return z such that the area under the unit Gaussian from -inf to z is p.
    Must have 0.0 <= p <= 1.0.
    """

    z = normIQ(1.0 - p)

    return z + (p - normP(z)) / normZ(z)

 def main():

    from spambayes.Histogram import Hist

    import sys

    class WrappedRandom:

        def __init__(self, baserandom=random.random, tabsize=513):

            self.baserandom = baserandom

            self.n = tabsize

            self.tab = [baserandom() for i in range(tabsize)]

            self.next = baserandom()

        def random(self):

            result = self.next

            i = int(result * self.n)

            self.next = self.tab[i]

            self.tab[i] = self.baserandom()

            return result

    random = WrappedRandom().random

    def judge(ps, ln=_math.log, ln2=_math.log(2), frexp=_math.frexp):

        H = S = 1.0

        Hexp = Sexp = 0

        for p in ps:

            S *= 1.0 - p

            H *= p

            if S < 1e-200:

                S, e = frexp(S)

                Sexp += e

            if H < 1e-200:

                H, e = frexp(H)

                Hexp += e

        S = ln(S) + Sexp * ln2

        H = ln(H) + Hexp * ln2

        n = len(ps)

        S = 1.0 - chi2Q(-2.0 * S, 2*n)

        H = 1.0 - chi2Q(-2.0 * H, 2*n)

        return S, H, (S-H + 1.0) / 2.0

    warp = 0

    bias = 0.99

    if len(sys.argv) > 1:

        warp = int(sys.argv[1])

    if len(sys.argv) > 2:

        bias = float(sys.argv[2])

    h = Hist(20, lo=0.0, hi=1.0)

    s = Hist(20, lo=0.0, hi=1.0)

    score = Hist(20, lo=0.0, hi=1.0)

    for i in range(5000):

        ps = [random() for j in range(50)]

        s1, h1, score1 = judge(ps + [bias] * warp)

        s.add(s1)

        h.add(h1)

        score.add(score1)

    print "Result for random vectors of 50 probs, +", warp, "forced to", bias

    print

    print 'H',

    h.display()

    print

    print 'S',

    s.display()

    print

    print '(S-H+1)/2',

    score.display()

 def showscore(ps, ln=_math.log, ln2=_math.log(2), frexp=_math.frexp):

    H = S = 1.0

    Hexp = Sexp = 0

    for p in ps:

        S *= 1.0 - p

        H *= p

        if S < 1e-200:

            S, e = frexp(S)

            Sexp += e

        if H < 1e-200:

            H, e = frexp(H)

            Hexp += e

    S = ln(S) + Sexp * ln2

    H = ln(H) + Hexp * ln2

    n = len(ps)

    probS = chi2Q(-2*S, 2*n)

    probH = chi2Q(-2*H, 2*n)

    print "P(chisq >= %10g | v=%3d) = %10g" % (-2*S, 2*n, probS)

    print "P(chisq >= %10g | v=%3d) = %10g" % (-2*H, 2*n, probH)

    S = 1.0 - probS

    H = 1.0 - probH

    score = (S-H + 1.0) / 2.0

    print "spam prob", S

    print " ham prob", H

    print "(S-H+1)/2", score

 if __name__ == '__main__':

    import random

    main()



try:

    True, False

except NameError:

    True, False = 1, 0

 def chi2Q(x2, v, exp=_math.exp, min=min):

    """Return prob(chisq >= x2, with v degrees of freedom).
    v must be even.
    """

    assert v & 1 == 0

    m = x2 / 2.0

    sum = term = exp(-m)

    for i in range(1, v//2):

        term *= m / i

        sum += term

    return min(sum, 1.0)

 def normZ(z, sqrt2pi=_math.sqrt(2.0*_math.pi), exp=_math.exp):

    "Return value of the unit Gaussian at z."

    return exp(-z*z/2.0) / sqrt2pi

 def normP(z):

    """Return area under the unit Gaussian from -inf to z.
    This is the probability that a zscore is <= z.
    """

    a = abs(float(z))

    if a >= 8.3:

        sum = 0.5

    else:

        sum2 = term = a * normZ(a)

        z2 = a*a

        sum = 0.0

        i = 1.0

        while sum != sum2:

            sum = sum2

            i += 2.0

            term *= z2 / i

            sum2 += term

    if z >= 0:

        result = 0.5 + sum

    else:

        result = 0.5 - sum

    return result

 def normIQ(p, sqrt=_math.sqrt, ln=_math.log):

    """Return z such that the area under the unit Gaussian from z to +inf is p.
    Must have 0.0 <= p <= 1.0.
    """

    assert 0.0 <= p <= 1.0

    flipped = False

    if p > 0.5:

        flipped = True

        p = 1.0 - p

    if p == 0.0:

        z = 8.3

    else:

        t = sqrt(-2.0 * ln(p))

        z = t - (2.30753 + .27061*t) / (1. + .99229*t + .04481*t**2)

    if flipped:

        z = -z

    return z

 def normIP(p):

    """Return z such that the area under the unit Gaussian from -inf to z is p.
    Must have 0.0 <= p <= 1.0.
    """

    z = normIQ(1.0 - p)

    return z + (p - normP(z)) / normZ(z)

 def main():

    from spambayes.Histogram import Hist

    import sys

    class WrappedRandom:

        def __init__(self, baserandom=random.random, tabsize=513):

            self.baserandom = baserandom

            self.n = tabsize

            self.tab = [baserandom() for i in range(tabsize)]

            self.next = baserandom()

        def random(self):

            result = self.next

            i = int(result * self.n)

            self.next = self.tab[i]

            self.tab[i] = self.baserandom()

            return result

    random = WrappedRandom().random

    def judge(ps, ln=_math.log, ln2=_math.log(2), frexp=_math.frexp):

        H = S = 1.0

        Hexp = Sexp = 0

        for p in ps:

            S *= 1.0 - p

            H *= p

            if S < 1e-200:

                S, e = frexp(S)

                Sexp += e

            if H < 1e-200:

                H, e = frexp(H)

                Hexp += e

        S = ln(S) + Sexp * ln2

        H = ln(H) + Hexp * ln2

        n = len(ps)

        S = 1.0 - chi2Q(-2.0 * S, 2*n)

        H = 1.0 - chi2Q(-2.0 * H, 2*n)

        return S, H, (S-H + 1.0) / 2.0

    warp = 0

    bias = 0.99

    if len(sys.argv) > 1:

        warp = int(sys.argv[1])

    if len(sys.argv) > 2:

        bias = float(sys.argv[2])

    h = Hist(20, lo=0.0, hi=1.0)

    s = Hist(20, lo=0.0, hi=1.0)

    score = Hist(20, lo=0.0, hi=1.0)

    for i in range(5000):

        ps = [random() for j in range(50)]

        s1, h1, score1 = judge(ps + [bias] * warp)

        s.add(s1)

        h.add(h1)

        score.add(score1)

    print "Result for random vectors of 50 probs, +", warp, "forced to", bias

    print

    print 'H',

    h.display()

    print

    print 'S',

    s.display()

    print

    print '(S-H+1)/2',

    score.display()

 def showscore(ps, ln=_math.log, ln2=_math.log(2), frexp=_math.frexp):

    H = S = 1.0

    Hexp = Sexp = 0

    for p in ps:

        S *= 1.0 - p

        H *= p

        if S < 1e-200:

            S, e = frexp(S)

            Sexp += e

        if H < 1e-200:

            H, e = frexp(H)

            Hexp += e

    S = ln(S) + Sexp * ln2

    H = ln(H) + Hexp * ln2

    n = len(ps)

    probS = chi2Q(-2*S, 2*n)

    probH = chi2Q(-2*H, 2*n)

    print "P(chisq >= %10g | v=%3d) = %10g" % (-2*S, 2*n, probS)

    print "P(chisq >= %10g | v=%3d) = %10g" % (-2*H, 2*n, probH)

    S = 1.0 - probS

    H = 1.0 - probH

    score = (S-H + 1.0) / 2.0

    print "spam prob", S

    print " ham prob", H

    print "(S-H+1)/2", score

 if __name__ == '__main__':

    import random

    main()


