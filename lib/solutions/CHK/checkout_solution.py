# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "":
        return 0
    if skus.isalpha() and skus.isupper():
        total = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 
                 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
                 'Y': 0, 'Z': 0}

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
                      'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 
                      'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}

        #No Offers
        total['C'] = count_dict['C'] * price_dict['C']
        total['D'] = count_dict['D'] * price_dict['D']
        total['E'] = count_dict['E'] * price_dict['E']
        total['G'] = count_dict['G'] * price_dict['G']
        total['I'] = count_dict['I'] * price_dict['I']
        total['J'] = count_dict['J'] * price_dict['J']
        total['L'] = count_dict['L'] * price_dict['L']
        total['N'] = count_dict['N'] * price_dict['N']
        total['O'] = count_dict['O'] * price_dict['O']
        total['R'] = count_dict['R'] * price_dict['R']
        total['W'] = count_dict['W'] * price_dict['W']

        #Various multi offer on same skus (x_num for p1 y_num for p2 etc )
        total['A'] = count_dict['A']//5 * 200 + (count_dict['A']%5)//3 * 130 + (count_dict['A']%5) % 3 * price_dict['A']
        total['H'] = count_dict['H']//10 * 80 + (count_dict['H']%10)//5 * 45 + (count_dict['H']%10) % 5 * price_dict['H']
        total['V'] = count_dict['V']//3 * 130 + (count_dict['V']%3)//2 * 90 + (count_dict['V']%3) % 2 * price_dict['V']

        total['K'] = count_dict['K']//2 * 120 + count_dict['K'] % 2 * price_dict['K']
        total['P'] = count_dict['P']//5 * 200 + count_dict['P'] % 5 * price_dict['P']

        #Multi Offer Type 2 (Buy x Get y free)
        total['F'] = count_dict['F']//3 * 2 * price_dict['F'] + count_dict['F'] % 3 * price_dict['F']
        total['U'] = count_dict['U']//4 * 3 * price_dict['U'] + count_dict['U'] % 4 * price_dict['U']

        #Multi offer between 2 skus
        count_dict['B'] = count_dict['B'] - count_dict['E'] // 2
        if count_dict['B'] < 0:
            count_dict['B'] = 0
        total['B'] = count_dict['B']//2 * 45 + count_dict['B'] % 2 * 30

        count_dict['M'] = count_dict['M'] - count_dict['N'] // 3
        if count_dict['M'] < 0:
            count_dict['M'] = 0
        total['M'] = count_dict['M'] * price_dict['M']

        count_dict['Q'] = count_dict['Q'] - count_dict['R'] // 3
        if count_dict['Q'] < 0:
            count_dict['Q'] = 0
        total['Q'] = count_dict['Q']//3 * 80 + count_dict['Q'] % 3 * price_dict['Q']

        #Item Group Offer
        #total['S'] = count_dict['S'] * price_dict['S']
        #total['T'] = count_dict['T'] * price_dict['T']
        #total['X'] = count_dict['X'] * price_dict['X']
        #total['Y'] = count_dict['Y'] * price_dict['Y']
        #total['Z'] = count_dict['Z'] * price_dict['Z']
        #offer_array = [count_dict['S'], count_dict['T'], count_dict['X'], count_dict['Y'], count_dict['Z']]
        total_group1_offer = (count_dict['S'] + count_dict['T'] + count_dict['X'] + count_dict['Y'] + count_dict['Z'])//3 * 45
        remaining_amount = (count_dict['S'] + count_dict['T'] + count_dict['X'] + count_dict['Y'] + count_dict['Z']) % 3
        
        remaining_items_sorted = []
        x = count_dict['X']
        s = count_dict['S']
        t = count_dict['T']
        y = count_dict['Y']
        z = count_dict['Z']
        for i in range(x):
            remaining_items_sorted.append('X')
        for i in range(s):
            remaining_items_sorted.append('S')
        for i in range(t):
            remaining_items_sorted.append('T')
        for i in range(y):
            remaining_items_sorted.append('Y')
        for i in range(z):
            remaining_items_sorted.append('Z')

        if remaining_amount == 0:
            return sum(total.values()) + total_group1_offer
        elif remaining_amount == 1:
            return sum(total.values()) + total_group1_offer + price_dict[remaining_items_sorted[0]]
        else:
            return sum(total.values()) + total_group1_offer + price_dict[remaining_items_sorted[0]] + price_dict[remaining_items_sorted[1]]
        
    
    #Characters other than alphabets in string
    return -1



