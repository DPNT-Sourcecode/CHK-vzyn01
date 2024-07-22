# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus.count('A') + skus.count('B') + skus.count('C') + skus.count('D') < len(skus):
        return -1
    if skus.isalpha():
        a_total = skus.count('A')//3 * 130 + skus.count('A') % 3 * 50
        b_total = skus.count('B')//2 * 45 + skus.count('B') % 2 * 30
        c_total = skus.count('C') * 20
        d_total = skus.count('D') * 15

        return a_total + b_total + c_total + d_total
        #Treat any other alphabets as bad barcode reads for now
    elif skus == "":
        return 0
    else:
        #Characters other than alphabets in string
        return -1


