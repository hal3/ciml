from sklearn.svm import SVC
import numpy as np
import optparse
import sys

def parseFeature(s):
    [fn,fv] = s.split(':')
    return float(fv)

def loadData(filename):
    X = []
    Y = []
    with open(filename, 'r') as h:
        for l in h.readlines():
            a = l.strip().split()
            # assumes all features are defined!
            Y.append(float(a[0]))
            X.append(map(parseFeature,a[1:]))
    return np.array(X),np.array(Y)

def string2kernel(s):
    if s == '0': return 'linear'
    elif s == '1': return 'poly'
    elif s == '2': return 'rbf'
    elif s == '3': return 'tanh'
    else: return s

def main(args):
    if len(args) < 2: raise Exception()
    c = 1.0
    k = 'rbf'
    d = 3
    g = 1.0
    r = 0.0
    filename = args[-2]
    model = args[-1]
    print 'training model %s -> %s' % (filename,model)
    i = 0
    while i < len(args) - 2:
        if args[i] == '-t':
            k = string2kernel(args[i+1])
            i += 2
        elif args[i] == '-c':
            c = float(args[i+1])
            i += 2
        elif args[i] == '-r':
            r = float(args[i+1])
            i += 2
        elif args[i] == '-g':
            g = float(args[i+1])
            i += 2
        elif args[i] == '-d':
            d = float(args[i+1])
            i += 2
        else:
            raise Exception('invalid argument: ' + str(args[i]))

    X,Y = loadData(filename)
    f = SVC(C=c, kernel=k, degree=d, gamma=g, coef0=r)
    f.fit(X,Y)
    print >>sys.stderr, 'fit model:', f
    with open(model, 'w') as h:
        possv,negsv = 0,0
        if f.classes_[0] == -1:
            f.dual_coef_ *= -1
        for alpha in f.dual_coef_[0]:
            if alpha < 0: negsv += 1
            else: possv += 1
        print >>h, 'svm_type c_svc'
        print >>h, 'kernel_type', k
        print >>h, 'gamma', g
        print >>h, 'degree', d
        print >>h, 'coef0', r
        print >>h, 'nr_class', 2
        print >>h, 'total_sv', np.sum(f.n_support_)
        print >>h, 'rho', -f.intercept_[0]
        print >>h, 'label -1 1'
        print >>h, 'nr_sv', possv, negsv
        print >>h, 'SV'
        for i,alpha in enumerate(f.dual_coef_[0]):
            if alpha < 0: continue
            print >>h, str(alpha) + ' ' + ' '.join([str(fn+1)+':'+str(fv) for fn,fv in enumerate(f.support_vectors_[i])])
        for i,alpha in enumerate(f.dual_coef_[0]):
            if alpha > 0: continue
            print >>h, str(alpha) + ' ' + ' '.join([str(fn+1)+':'+str(fv) for fn,fv in enumerate(f.support_vectors_[i])])

if __name__ == '__main__' and len(sys.argv) > 0 and len(sys.argv[0]) > 0:
    main(sys.argv[1:])
    
