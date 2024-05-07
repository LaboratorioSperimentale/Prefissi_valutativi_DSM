import os
import collections
import tqdm

tot_basi = set()

prefissi = {"stra": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)},

            "iper": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)},

            "ultra": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)},

            "extra": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)},

            "arci": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)},

            "super": {"space": collections.defaultdict(int),
                     "hyphen": collections.defaultdict(int),
                     "s-word": collections.defaultdict(int)}
            }


lista_file = [(x, f"output/{x}_basi.txt") for x in prefissi]


for pref, file in tqdm.tqdm(lista_file):
    with open(file) as fin:
        fin.readline()
        for line in fin:
            line = line.strip().split("\t")

            base, sword,hyphen,space = line
            sword = int(sword)
            hyphen = int(hyphen)
            space = int(space)

            tot_basi.add(base)

            prefissi[pref]["s-word"][base] = sword
            prefissi[pref]["hyphen"][base] = hyphen
            prefissi[pref]["space"][base] = space


with open(f"output/TOT_basi.txt", "w") as fout:
    s = "\t"
    for pref in prefissi:
        s+=f"{pref}\t\t"
    print(s, file=fout)

    for base in tot_basi:
        s = base+"\t"
        for pref in prefissi:
            s+=f"{prefissi[pref]['s-word'][base]}\t{prefissi[pref]['hyphen'][base]}\t{prefissi[pref]['space'][base]}\t"
        print(s, file=fout)