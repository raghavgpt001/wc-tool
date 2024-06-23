# My WC Tool

## Overview

This tool is a Python-based utility that mimics the basic functionality of the Unix `wc` command. It is designed to count the number of lines, words, and characters in a given file. Users can specify which counts to display through command-line arguments.

## Installation

To use this tool, you need to have Python installed on your system. This tool has been tested with Python 3.8 and above.

1. Clone this repository or download the source code.
2. Navigate to the directory containing `main.py`.

## Usage

Run the tool from the command line, specifying the file you want to analyze and the counts you are interested in. The basic syntax is as follows:

python main.py [filename] [options]


### Options

- `-l`, `--lines`: Count the number of lines in the file.
- `-w`, `--words`: Count the number of words in the file.
- `-c`, `--characters`: Count the number of characters in the file.

If no options are specified, the tool will display counts for lines, words, and characters by default.

### Example

To count the words in `example.txt`, you would run:

python main.py example.txt -w