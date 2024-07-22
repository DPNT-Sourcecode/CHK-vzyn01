# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0
    if skus.isalpha() and skus.isupper():
        a_count = skus.count('A')
        b_count = skus.count('B')
        c_count = skus.count('C')
        d_count = skus.count('D')
        e_count = skus.count('E')
        f_count = skus.count('F')

        #Count Dict probably could have been created a lot more easily through some 
        #one liner related to alphabet and count of alphabet as key value pairs for all uppercase alphabets
        count_dict = {'A': skus.count('A'), 'B': skus.count('B'), 'C': skus.count('C'), 'D': skus.count('D'), 
                      'E': skus.count('E'), 'F': skus.count('F'), 'G': skus.count('G'), 'H': skus.count('H'), 
                      'I': skus.count('I'), 'J': skus.count('J'), 'K': skus.count('K'), 'L': skus.count('L'), 
                      'M': skus.count('M'), 'N': skus.count('N'), 'O': skus.count('O'), 'P': skus.count('P'), 
                      'Q': skus.count('Q'), 'R': skus.count('R'), 'S': skus.count('S'), 'T': skus.count('T'), 
                      'U': skus.count('U'), 'V': skus.count('V'), 'W': skus.count('W'), 'X': skus.count('X'), 
                      'Y': skus.count('Y'), 'Z': skus.count('Z')}

        price_dict = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 
                      'K': 80, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 
                      'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50}
        
        a_total = count_dict['A']//5 * 200 + (count_dict['A']%5)//3 * 130 + (count_dict['A']%5) % 3 * price_dict['A']
        c_total = count_dict['C'] * price_dict['C']
        d_total = count_dict['D'] * price_dict['D']
        e_total = count_dict['E'] * price_dict['E']
        f_total = count_dict['F']//3 * 2 * price_dict['F'] + count_dict['F'] % 3 * price_dict['F']

        count_dict['B'] = count_dict['B'] - count_dict['E'] // 2
        if count_dict['B'] < 0:
            count_dict['B'] = 0
        b_total = count_dict['B']//2 * 45 + count_dict['B'] % 2 * 30

        return a_total + b_total + c_total + d_total + e_total + f_total
    
    #Characters other than alphabets in string
    return -1
