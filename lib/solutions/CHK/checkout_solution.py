# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus.isalpha():
        a_total = skus.count('A')//3 * 130 + skus.count('A') % 3 * 50
        b_total = skus.count('B')//2 * 45 + skus.count('A') % 2 * 30
        c_total = skus.count('C') * 20
        d_total = skus.count('D') * 15

        return a_total + b_total + c_total + d_total
        #Treat any other alphabets as bad barcode reads for now
    else:
        #Characters other than alphabets in string
        return -1
    
    return -1
