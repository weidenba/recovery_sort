# Recovery Sort
[![Build Status](https://travis-ci.org/weidenba/recovery_sort.svg)](https://travis-ci.org/weidenba/recovery_sort)
[![codecov](https://codecov.io/gh/weidenba/recovery_sort/branch/master/graph/badge.svg)](https://codecov.io/gh/weidenba/recovery_sort)

Re-organize files by type and date; filter duplicates and unintended files.

## Requirements
Since Recovery Sort relies on file/magic it will not run on Windows at the moment.  

* Python >= 3.4
* PIP

## Basic Usage
```sh
$ sudo -EH pip3 install -r requirements.txt
$ ./recovery_sort.py INPUT_DIRECTORY OUTPUT_DIRECTOTRY
```
For more advanced features and optional filtering of unintended files have a look at the "--help" option.

## Result
Recovery sort creates new folders and copy the files into them.  
New file paths are generated with this template: *MIME/TYPE/ModificationDate_OriginalFileName*

The resulting folder/file structure will look like this:

```sh
.
├── image
│   ├── jpeg
│   │   └── 2015-01-01_photo.jpg
│   └── png
│       └── 2016-05-25_icon.png
└── text
    └── plain
        └── 2017-09-06_text.txt

```
Duplicates are not copied.

## Ignore Filter

There is a filter system to ignore unintended files.
Ignore filters can be applied with the -i argument.
You can apply several filters at once by using -i several times.  

```sh
$ ./recovery_sort.py -i FILTER_1 [-i FILTER 2 ...] INPUT_DIRECTORY OUTPUT_DIRECTOTRY
```
If you'd like to add all available ignore filters, you can use the '-I' argument.

### blacklist
Ignore files that are on a blacklist.
Blacklists are stored in the */blacklist* folder.
We provide blacklists for Windows and widely spread software.
You can add your own blacklist by using the blacklist_generator. 

```sh
$ ./blacklist_generator.py INPUT_DIRECTORY
```

INPUT_DIRECTORY shall contain all files you would like to blacklist.
The generated list is stored to */blacklist/user_generated_blacklist*.  
For more advanced features have a look at the "--help" option.

### small_video
Ignore video files < 10KiB. These files are most likely broken.

### thumbnail
Ignore thumbnail files recovered by [PhotoRec](http://www.cgsecurity.org/wiki/PhotoRec).

## Rename Filter
There is filter system to rename files.
Rename filters can be applied with the -r argument
You can apply several filters at once by using -r several times.  

```sh
$ ./recovery_sort.py -r FILTER_1 [-r FILTER 2 ...] INPUT_DIRECTORY OUTPUT_DIRECTOTRY
```
If you'd like to add all available ignore filters, you can use the '-I' argument

### mp3
Sort mp3 files according to their meta data.
The resulting folder/file structure will look like this:

```sh
.
└── audio
    └── mpeg
        ├── John Doe
        │   └── Best Album Ever
        │       └── The best Song Ever.mp3
        └── Jane Doe
            └── Just Another Album
                └── Fantastic Song.mp3
```
