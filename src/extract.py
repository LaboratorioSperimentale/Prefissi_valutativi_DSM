import collections

import tqdm

import src.reader as r


def compute_derivates_frequencies(input_files,
								part_of_speech, prefixes,
								output_folder):

	prefissi = {x: {"space": collections.defaultdict(int),
					"hyphen": collections.defaultdict(int),
					"s-word": collections.defaultdict(int)}
					for x in prefixes}

	basi = collections.defaultdict(int)

	found_bases = set()

	for file in tqdm.tqdm(input_files):
		for sentence in tqdm.tqdm(r.read_itwac(file)):
			prev_lemma = ""
			prev_form = ""
			prev_pos = ""

			for token_n, token in enumerate(sentence):
				form, lemma, pos = token
				pos = pos.split(":")[0]

				if pos == part_of_speech:

					found = False

					for pref in prefissi:
						if not lemma == pref:
							if lemma.startswith(pref):
								if lemma[len(pref)] == "-":
									found = True
									base = lemma[len(pref)+1:]
									prefissi[pref]["hyphen"][base] += 1
									found_bases.add(base)

								else:
									found = True
									base = lemma[len(pref):]
									prefissi[pref]["s-word"][base] += 1
									found_bases.add(base)

							elif prev_lemma == pref:
								found = True
								base = lemma
								prefissi[pref]["space"][base] += 1
								found_bases.add(base)

					if not found:
						basi[lemma] += 1

				prev_lemma = lemma
				prev_form = form
				prev_pos = pos


	with open(output_folder.joinpath("TOT.tsv"), "w", encoding="utf-8") as fout:

		header = "BASE\t"

		for pref in prefissi:
			header += f"{pref}.s-word\t{pref}.hyphen\t{pref}.space\t{pref}.TOT\t"

		header += "not-prefixed"

		print(header, file=fout)

		for base in found_bases:

			s = f"{base}\t"

			for pref in prefissi:
				hyphen = prefissi[pref]['s-word'][base]
				sword = prefissi[pref]['hyphen'][base]
				space = prefissi[pref]['space'][base]
				tot_pref = hyphen + sword + space
				s+=f"{hyphen}\t{sword}\t{space}\t{tot_pref}\t"
			s+=f"{basi[base]}"

			print(s, file=fout)


def compute_rawfrequencies(input_files,
							part_of_speech,
							output_folder):

	freqs = collections.defaultdict(int)

	for file in tqdm.tqdm(input_files):
		for sentence in tqdm.tqdm(r.read_itwac(file)):
			for token_n, token in enumerate(sentence):
				form, lemma, pos = token
				pos = pos.split(":")[0]

				if pos == part_of_speech:
					freqs[f"{lemma}/{part_of_speech}"]+=1


	with open(output_folder.joinpath(f"{part_of_speech}.counts"), "w", encoding="utf-8") as fout:
		for lemma, freq in freqs.items():
			print(f"{lemma}\t{freq}", file=fout)
