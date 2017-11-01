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

from main.ReOrganizer import ReOrganizer


PROGRAM_NAME = 'Recovery Sort'
PROGRAM_VERSION = '1.0'
PROGRAM_DESCRIPTION = 're-organize files by type and date'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('input_dir', help='input directory')
    parser.add_argument('out_dir', help='output directory')
    parser.add_argument('-i', '--ignore_filter', default=[], help='Set ignore filter. Can be used multiple times. Available filters: blacklist, small_video, thumbnail', action='append', type=str)
    parser.add_argument('-I', '--apply_all_ignore_filters', action='store_true', default=False, help='apply all available ignore filters')
    parser.add_argument('-r', '--rename_filter', default=[], help='Set rename filter. Can be used multiple times. Available filters: mp3', action='append', type=str)
    parser.add_argument('-R', '--apply_all_rename_filters', action='store_true', default=False, help='apply all available rename filters')
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

    ignore_filters = args.ignore_filter if not args.apply_all_ignore_filters else 'all'
    rename_filters = args.rename_filter if not args.apply_all_rename_filters else 'all'

    file_organizer = ReOrganizer(
        out_dir=args.out_dir,
        ignore_filters_to_apply=ignore_filters,
        rename_filters_to_apply=rename_filters
    )

    logging.info('Re-organize files in {}'.format(args.input_dir))
    logging.info('Result storage: {}'.format(args.out_dir))
    logging.debug('ignore filters: {}'.format(file_organizer.ignore_filter_system.filters_to_apply))
    logging.debug('rename filters: {}'.format(file_organizer.rename_filter_system.filters_to_apply))

    file_organizer.reorganize_files(args.input_dir)

    logging.info('Re-organizing complete')
    sys.exit()
