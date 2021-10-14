#given two DNA strings s and t
#return the hamming distance between s and t

s = 'ATCTAAAAATCCTTAAACGCTCGCGTCTCCCCTGTCTCCTATCACACCGGGAGATCAATCCTCCATGTGAGGGGGGCTATAACTGGTGTCCACCCTGCCAGTCAAGTGAAGGAGATAAAAGTCGAAGGAGTGGCACTCTAACTTACCGGACGGAGACTGTCAGTATCGAAGGCTGTACCCCGCTGGTCTCACAAGCTGAGCACGTCGCTGAACCCTCTGAGGTGGGTCTTTTATGTCCTATTTATGCTCATTGAAGACAGAGCCAGAACTCCAGAACCTGGCCTATTGGGCCCTCCGAGACGATTTCCCTACTACCAGTCCTGCATTAAGGTGAAAAAAGATGGCCGTGGACGACTGTGCGAGGGCACAGCAACCCAGCTGGTCGTTCTAAGGACATACCGGCACCCCGCTAAAATTGTATTCTGCGAGTAGCCGAAGGACAGAGATGCGCGATCTATGAAGTCCACGCGCCTTCTCCGAGGGAAAGAAATTCAAATAGGAACCTCATTAGGCGAGAGTTCCTTGACCGTATTACGCTTTTAGCGGCCCGGGTCTTCTGCTACAGCGGTCCCTTTTTGCCCATGGTGTAGACAGAGGCTTGTAAAGCCCGATTGTCGGTAAGCGGCGAATTACAAAGGCTCCCCACTCTTCGTCTCCAGCAGAAGCCCTCACCTCCGTTCTGATCCCCTCATTTGAGTAACTAGACTCCGGAATGCACTTTCTAGGTCAAAGAATATGATCGTCGCGATATCAATAGCATTAGCTCATGAGTCCCAGCTCCAGAGGGCTTCAAAGCGAGTGGTCAGAGCTCCACTCCTCTATATCTCGTATAGCTGAGACGCCATTCTGACCCGCGAGATTTCCTTCTGGTGCAGCATCTTACGAATGTTAGACTGATGACTTATGCCAGTCGGCCCTCT'
t = 'AATACGGAAGCATTGACCTTCACCCTGGTCCTTGGGACCTAGGACTTCCCGAGATTTCCCACCCATCTATGGGTGGGCAAACCCGGAGTCTGCCCTGGAACACACTCTAATCGGGAAAAATACGATGAGATTGGACTCCCCCTATGCAGAAAAGGAGTGGCGGTGACCGTCCGTCTACCAATGTGGTCGCACAAACTCAGCGCGTAGGGGAGCCCAGAGAGGCGGGTGTTTATGTTCATATGTGCGCATGGAGCGAAACGTAAAAGTTCTCCAGAGATACGCCTACATACGCCAGCGTGACGGTTCCTACATCTCCAGACCTGCATTGGGTAGATAATCGGTCTCCGGGAACTATTGTTCCTGGGCACTGTAATCCAGCAGTTGGAGCTGACTTTACCCACGTACCACATGCTAAATGTCAGCCCCGCGAGAGTTTATCAAATCCCGTGGAGACTCAGGAGGTCTTTAGTCCCCTTGCGTCCTTAAGTAATTCTAATAGTAACCACATCAACTAGAAGGAACCTTATTGGCGGCTCGCTTTCGCTGCGGCGGGGGGCTTCTTCTGCAGCCCAAATTTAACGATAGTGTAGTGACTTGCCTACAAACCTCGTAGGTCTGTAAGGGGCTTAATCCGAAGGATCGTCCCACTCCCTTCTTAGACGAAGTCCTCAGTTCCGTCTTGAATGCGTAATTCGTCTACCTGGCAACCATAGTGGTTGACCGCTGTGAAAGAATATCAGCAACTCGTGATCTACAGCAATGCCTACTGAGACTCGGCTCCTGATTGTTGGGTGGGGAGCGGATAGAATTTTACGAGGAGATACATTTAGTCTATTGGGCGTGAATGTCCCTTGTTAACCTTCACCAATCTCCTGATGTATACAAAGGCTAGACTGGTGAGCTAGAGCTGTAGCCTCTCT'

def hamming(s,t):
    result = 0
    if len(s) != len(t):
        return "Not equal"
    else:
        for x,(i,j) in enumerate(zip(s,t)):
            if i!=j:
                result+=1

    return result

print(hamming(s,t))