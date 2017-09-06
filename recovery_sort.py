#! /usr/bin/env python3
import argparse
import logging
import sys

from main import reorganize_files


PROGRAM_NAME = "Recovery Sort"
PROGRAM_VERSION = "0.1"
PROGRAM_DESCRIPTION = "re-organize files by type and date"

filter_list = []


def _setup_argparser():
    parser = argparse.ArgumentParser(description="{} - {}".format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version="{} {}".format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="print debug messages")
    parser.add_argument("-t", "--ignore_thumbnails", action="store_true", default=False, help="ignore recoverd thumbnail files")
    parser.add_argument("-s", "--ignore_small_media", action="store_true", default=False, help="ignore small media files")
    parser.add_argument("input_dir", help="input directory")
    parser.add_argument("out_dir", help="output directory")
    return parser.parse_args()


def _setup_logging(args):
    log_format = logging.Formatter(fmt="[%(asctime)s][%(module)s][%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger('')
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(log_format)
    logger.addHandler(console_logger)


def _set_filters(args):
    global filter_list
    if args.ignore_thumbnails:
        filter_list.append("thumbnail")
    if args.ignore_small_media:
        filter_list.append("small_media")


if __name__ == '__main__':
    args = _setup_argparser()
    _setup_logging(args)

    logging.info("Re-organize files in {}".format(args.input_dir))
    logging.info("Result storage: {}".format(args.out_dir))

    _set_filters(args)
    reorganize_files(args.input_dir, args.out_dir, filter_list)

    logging.info("Re-organizing complete")
    sys.exit()
