dominance = {
    'AA_AA':	1,
    'AA_Aa':	1,
    'AA_aa':	1,
    'Aa_Aa':	(3/4),
    'Aa_aa':	(2/4),
    'aa_aa':	0
}

pop = {
    'AA_AA':	17181,
    'AA_Aa':	17226,
    'AA_aa':	17412,
    'Aa_Aa':	19489,
    'Aa_aa':	19048,
    'aa_aa':	16553
}

offspring = 0

for d in dominance:
    offspring += dominance[d]*float(pop[d])

print(offspring*2)