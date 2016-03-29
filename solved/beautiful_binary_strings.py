def beautiful_binary_strings(BinaryString):
    s = BinaryString
    while s:
        s0,s = s,s.replace('AA','').replace('BB','')
        if s == s0:
            return False
    return True