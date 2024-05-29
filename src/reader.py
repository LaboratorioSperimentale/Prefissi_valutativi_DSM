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