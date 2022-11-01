for i in range(int(input())):
    s = input()
    for j in range(len(s)):
        if s[j] == 'a':
            if 'n' in s[j:]:
                ind_n = s.index('n', j)
                if 't' in s[ind_n:]:
                    ind_t = s.index('t', ind_n)
                    if 'o' in s[ind_t:]:
                        ind_o = s.index('o', ind_t)
                        if 'n' in s[ind_o:]:
                            print(i + 1, end = ' ')
                            break
