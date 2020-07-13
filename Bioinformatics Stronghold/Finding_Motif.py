def find_motif(seq, pattern):
    ans = []
    for i in range(len(seq) - len(pattern) - 1):
        if pattern == seq[i:i + len(pattern)]:
            ans.append(i + 1)

    return ans


seq = 'ATCTGTGCCATCTGTGTATCTGTGTAATCTGTGCATCTGTGTGATCTGTGCAGGAATCTGTGGTATCTGTGTATCTGTGGTAATCTGTGAATCTGTGGATCTGTGATCTGTGATCTGTGTTGGTGATCTGTGAAATCTGTGGATCTGTGATCTGTGCAATCTGTGACGATCTGTGGCCATCTGTGATCTGTGAATCTGTGATTTATCTGTGTTTTGGATCTGTGGCTATCTGTGTCTGCAATCTGTGGAATCTGTGGATCTGTGTCTTTATCTGTGAAAATCTGTGATCTGTGATCTGTGCGTCGGATCTGTGATCTGTGATCTGTGATCTGTGCGCTCATCTGTGTATCTGTGATCTGTGATCTGTGATCTGTGTAGATCTGTGTCATCTGTGATCTGTGCAAATGGGCACAACATCTGTGATCTGTGCATCTGTGATCTGTGCGGACATCTGTGATCTGTGCGCGGAATCTGTGATCTGTGGGTTATCTGTGTAATGCAGAGAGATCTGTGCATTATCTGTGATCTGTGATCATCTGTGATCTGTGTCATCTGTGCGGGATCTGTGTAATCTGTGATCTGTGATCTGTGCTCATCTGTGGCGATCTGTGTGCCGGTACTATCTGTGGCCATCTGTGAAAAACTTATCTGTGATCTGTGGATCTGTGCAATCTGTGCATCTGTGTATCTGTGGCGTATCTGTGGTTATCTGTGACGAGTGCTATCTGTGATCTGTGATCTGTGGAATCTGTGTTATCTGTGCTATCTGTGGATTTATCTGTGTATCTGTGATCTGTGTACATCTGTGATCTGTGACGCATCTGTGGATCTGTGTATCTGTGATCTGTGTGTGCCATCTGTGATCTGTGTAAATCTGTGCGATCTGTGATCCTATCTGTG'
pattern = 'ATCTGTGAT'

print(*find_motif(seq, pattern))
