# Recovery Sort
[![Build Status](https://travis-ci.org/weidenba/recovery_sort.svg)](https://travis-ci.org/weidenba/recovery_sort)

Re-organize files by type and date; filter duplicates and unintended files

# Requirements
Since Recovery Sort relies on file/magic it will not run on Windows at the moment.  

* Python 3
* PIP

# Basic Usage
```sh
$ sudo -EH pip3 install -r requirements.txt
$ ./recovery_sort.py INPUT_DIRECTORY OUTPUT_DIRECTOTRY
```
For more advanced features and optional filtering of unintended files have a look at the "--help" option.

# Result
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
