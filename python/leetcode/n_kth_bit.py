def n_k_bit(n,k):
    length = 2**n-1
    midpoint = length//2+1
    print(f'{n,k,midpoint}')
    if k==midpoint:
        return '0' if n==1 else '1'
    elif k<midpoint:
        return n_k_bit(n-1,k)
    else:
        return '0' if n_k_bit(n-1,length+1-k) == '1' else '1'

correct = dict()
correct[(1,1)] = '0'
correct[(2,1)],correct[(2,2)],correct[(2,3)] = '0','1','1'
correct[(3,1)],correct[(3,2)],correct[(3,3)],correct[(3,4)],correct[(3,5)],correct[(3,6)],correct[(3,7)] = '0','1','1','1','0','0','1'

if __name__ == '__main__':
    cases = [(1,1), (2,1),(2,2),(2,3),(3,1),(3,2),(3,4),(3,6),(3,7)]
    for n,k in cases:
        print(n_k_bit(n,k)==correct[(n,k)])

