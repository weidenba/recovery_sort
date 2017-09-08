#! /usr/bin/env python3
import argparse
import logging
import sys

from main.blacklist_generator import create_blacklist


PROGRAM_NAME = 'Recovery Sort - Blacklist Generator'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'Generate blacklists to be used with Recovery Sort'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('out_file', help='blacklist_file')
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

    logging.info('Generate blacklist from files in {}'.format(args.input_dir))
    logging.info('Store blacklist to: {}'.format(args.out_file))

    create_blacklist(args.input_dir, args.out_file)

    logging.info('Blacklist complete')
    sys.exit()
