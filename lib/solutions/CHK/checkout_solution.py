# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0
    if skus.isalpha():
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')
        e_count = skus.count('E')
        f_count = skus.count('F')

        if a_count + b_count + c_count + d_count + e_count + f_count < len(skus):
            return -1
        
        a_total = a_count//5 * 200 + (a_count%5)//3 * 130 + (a_count%5) % 3 * 50
        c_total = c_count * 20
        d_total = d_count * 15
        e_total = e_count * 40
        f_total = f_count//3 * 20 + f_count % 3 * 10

        b_count = b_count - e_count // 2
        if b_count < 0:
            b_count = 0
        b_total = b_count//2 * 45 + b_count % 2 * 30

        return a_total + b_total + c_total + d_total + e_total + f_total
    
    #Characters other than alphabets in string
    return -1


