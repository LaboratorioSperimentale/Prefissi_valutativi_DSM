import os
import collections
import tqdm

_SETPOS = "VER"
_SETFILE = "data/escludere_verbi.txt"

def read_itwac(fname):

    sentence = []

    with open(fname, encoding="iso-8859-1") as fin:

        for line in fin:
            if line.startswith("<s"):
                if not len(sentence) == 0:
                    yield sentence

                sentence = []

            elif line.startswith("<"):
                pass

            else:
                line = line.strip().split("\t")
                if len(line) == 3:
                    form = line[0]
                    lemma = line[2]
                    pos = line[1].split(":")[0]

                    token = (form, lemma, pos)
                    sentence.append(token)
                else:
                    pass
                    #TODO add log

        if not len(sentence) == 0:
            yield sentence

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

da_escludere = set()

with open(_SETFILE) as fin:
    for line in fin:
        da_escludere.add(line.strip())

lista_file_itwac = os.listdir("/home/ludovica/Documents/CORPORA/ITWAC")

# lista_file_itwac = ["ITWAC-1.xml", "ITWAC-2.xml"]


for file in tqdm.tqdm(lista_file_itwac):
    prev_lemma = ""
    prev_form = ""
    prev_pos = ""


    for sentence in tqdm.tqdm(read_itwac(f"/home/ludovica/Documents/CORPORA/ITWAC/{file}")):
        for token_n, token in enumerate(sentence):
            form, lemma, pos = token
            pos = pos.split(":")[0]

            if pos == _SETPOS and not lemma in da_escludere:
                for pref in prefissi:
                    if not lemma == pref:

                        if lemma.startswith(pref):
                            if lemma[len(pref)] == "-":
                                base = lemma[len(pref)+1:]
                                prefissi[pref]["hyphen"][base] += 1

                            else:
                                base = lemma[len(pref):]
                                prefissi[pref]["s-word"][base] += 1
                        #    print(lemma)
                        #    print(prefissi)
                        #    input()

                        if prev_lemma == pref:
                            base = lemma
                            prefissi[pref]["space"][base] += 1
                            # print(lemma)
                            # print(prefissi)
                            # input()

            prev_lemma = lemma
            prev_form = form
            prev_pos = pos



for pref in prefissi:
    bases_space = list(prefissi[pref]["space"].keys())
    bases_hyphen = list(prefissi[pref]["hyphen"].keys())
    bases_sword = list(prefissi[pref]["s-word"].keys())

    bases = set(bases_space+bases_hyphen+bases_sword)

    with open(f"output/{pref}_basi.txt", "w") as fout:
        print("\ts-word\thyphen\tspace", file=fout)
        for base in bases:
            print(f"{base}\t{prefissi[pref]['s-word'][base]}\t{prefissi[pref]['hyphen'][base]}\t{prefissi[pref]['space'][base]}", file=fout)