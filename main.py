import argparse
import pathlib
from pathlib import Path

import tqdm

import src.extract as e
import src.process as p


def _compute_frequencies(args):

	prefixes = set()
	with open(args.prefixes, encoding="utf-8") as fin:
		for line in fin:
			prefixes.add(line.strip().split())


	e.compute_derivates_frequencies(args.input_files_list,
								   	args.pos,
					   				prefixes,
					   				args.output_folder)


def _compute_rawfreqs(args):
	e.compute_rawfrequencies(args.input_files_list,
							args.pos,
							args.output_folder)


def _linearize_itwac(args):
	p.linearize(args.input_files_list, args.output_folder)

if __name__ == "__main__":

	parent_parser = argparse.ArgumentParser(add_help=False)

	root_parser = argparse.ArgumentParser(prog='pv_dsm', add_help=True)
	subparsers = root_parser.add_subparsers(title="actions", dest="actions")


	parser_frequencies = subparsers.add_parser('frequencies',
											formatter_class=argparse.ArgumentDefaultsHelpFormatter,
											parents=[parent_parser],
											description='compute frequency of derivatives and bases',
											help='compute frequency of derivatives and bases')
	parser_frequencies.add_argument("-i", "--input-files-list",
								 default="files containing ITWAC corpus", nargs="+",
								 type=pathlib.Path,
								 help="path to file containing ITWAC corpus")
	parser_frequencies.add_argument("-o", "--output-folder", default="data_sample/output_frequencies/",
								 type=pathlib.Path,
								 help="path to output folder")
	parser_frequencies.add_argument("-p", "--pos", default="ADJ", choices=["ADJ", "NOUN", "VER", "ADV"],
								 help="part of speech tag")
	parser_frequencies.add_argument("--prefixes", default="data_sample/prefixes.txt",
							type=pathlib.Path,
							help="path to file containing list of studies prefixes")
	parser_frequencies.set_defaults(func=_compute_frequencies)


	parser_rawfreqs = subparsers.add_parser('raw_frequencies',
											formatter_class=argparse.ArgumentDefaultsHelpFormatter,
											parents=[parent_parser],
											description='compute frequency of derivatives and bases',
											help='compute frequency of derivatives and bases')
	parser_rawfreqs.add_argument("-i", "--input-files-list",
								 default="files containing ITWAC corpus", nargs="+",
								 type=pathlib.Path,
								 help="path to file containing ITWAC corpus")
	parser_rawfreqs.add_argument("-o", "--output-folder", default="data_sample/output_rawfreqs/",
								 type=pathlib.Path,
								 help="path to output folder")
	parser_rawfreqs.add_argument("-p", "--pos", default="ADJ", choices=["ADJ", "NOUN", "VER", "ADV"],
								 help="part of speech tag")
	parser_rawfreqs.set_defaults(func=_compute_rawfreqs)


	parser_linear = subparsers.add_parser('linearize',
									   	formatter_class=argparse.ArgumentDefaultsHelpFormatter,
										parents=[parent_parser],
										description='linearize ITWAC',
										help='linearize ITWAC')
	parser_linear.add_argument("-i", "--input-files-list",
								 default="files containing ITWAC corpus", nargs="+",
								 type=pathlib.Path,
								 help="path to file containing ITWAC corpus")
	parser_linear.add_argument("-o", "--output-folder", default="data_sample/output_rawfreqs/",
								 type=pathlib.Path,
								 help="path to output folder")
	parser_linear.set_defaults(func=_linearize_itwac)


	args = root_parser.parse_args()

	if "func" not in args:
		root_parser.print_usage()
		exit()

	args.func(args)
