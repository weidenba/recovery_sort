#! /usr/bin/env python3
import argparse
import logging
import sys

from main.ReOrganizer import ReOrganizer


PROGRAM_NAME = 'Recovery Sort'
PROGRAM_VERSION = '0.4'
PROGRAM_DESCRIPTION = 're-organize files by type and date'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('out_dir', help='output directory')
    parser.add_argument('-f', '--filter', default=[], help='Set filter. Can be used multiple times. Available filters: blacklist, small_video, thumbnail', action='append', type=str)
    return parser.parse_args()


def _setup_logging(args):
    log_format = logging.Formatter(fmt='[%(asctime)s][%(module)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('')
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(log_format)
    logger.addHandler(console_logger)


if __name__ == '__main__':
    args = _setup_argparser()
    _setup_logging(args)

    file_organizer = ReOrganizer(args.out_dir, args.filter)

    logging.info('Re-organize files in {}'.format(args.input_dir))
    logging.info('Result storage: {}'.format(args.out_dir))
    logging.debug('filters: {}'.format(file_organizer.filter_system.filters_to_apply))

    file_organizer.reorganize_files(args.input_dir)

    logging.info('Re-organizing complete')
    sys.exit()
