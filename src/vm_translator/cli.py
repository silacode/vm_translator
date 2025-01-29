"""Command-line interface module for the VM Translator.

This module provides command-line argument parsing functionality for the VM Translator,
allowing users to specify input files or directories for translation.
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command line arguments for the VM Translator.

    Returns:
        argparse.Namespace: Parsed command line arguments containing the input path.
    """
    parser = argparse.ArgumentParser(description="VM Translator for Nand2Tetris")
    parser.add_argument("path", type=Path, help="Path to .vm file or directory")
    return parser.parse_args()
