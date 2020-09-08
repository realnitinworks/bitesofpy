import os
from pathlib import Path


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    return (
        sum(p.is_dir() for p in Path(directory).glob("**/*")),
        sum(p.is_file() for p in Path(directory).glob("**/*"))
    )
