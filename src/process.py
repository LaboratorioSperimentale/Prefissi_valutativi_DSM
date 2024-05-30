import tqdm
import src.reader as r

def linearize_itwac(input_files, output_folder):

	for file in tqdm.tqdm(input_files):
		basename = file.stem

		with open(output_folder.joinpath(f"{basename}.linear"), "w", encoding="utf-8") as fout:
			for sentence in tqdm.tqdm(r.read_itwac(file)):
				sent = [f"{lemma}/{pos}" for form, lemma, pos in sentence]
				print(" ".join(sent), file=fout)