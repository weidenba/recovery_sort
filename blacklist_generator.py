#! /usr/bin/env python3
'''
    Recovery Sort
    Copyright (C) 2017 Peter Weidenbach

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
import logging
import sys
import os
from common_helper_files import get_dir_of_file

from main.blacklist_generator import create_blacklist


PROGRAM_NAME = 'Recovery Sort - Blacklist Generator'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'Generate blacklists to be used with Recovery Sort'

default_out_file = os.path.join(get_dir_of_file(__file__), 'blacklist/user_generated_blacklist')


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('-o', '--out_file', default=default_out_file, help='blacklist_file')
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
