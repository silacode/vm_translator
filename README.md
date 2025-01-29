# VM Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

A VM translator implemented in Python for the Nand2Tetris course.

## Description

This program translates VM code (similar to Java bytecode) into Hack assembly language. It's part of the Nand2Tetris project, which builds a modern computer from first principles.

## Features

- Translates VM arithmetic/logical commands
- Handles memory access commands
- Processes program flow commands
- Supports function calling commands

## Usage

```bash
python vm_translator.py <input_file.vm>
```

## Installation

1. Clone this repository
2. Ensure Python 3.9 or higher is installed
3. No additional dependencies required

## Project Structure

- `vm_translator.py`: Main program file
- `parser.py`: Parses VM commands
- `code_writer.py`: Generates assembly code
- `test/`: Test files and examples

## Author

Siladitya Samaddar

## License

MIT License