from pathlib import Path

"""
    We can use the Path class for optimized pattern matching.
    
    The constructor of the Path class will require a string representing the 
    directory path we want to use. 
    
    
    Calling the glob method on a Path object, we'll get a generator 
    that will yield the files that match the search criteria passed to the method. 
"""


def glob_match(folder_path: str, search_criteria: str) -> None:
    p: Path = Path(folder_path)
    print(type(p.glob(search_criteria)))
    for n in p.glob(search_criteria):  # Yields <class 'pathlib.PosixPath'> objects matching the search criteria
        print(n)
    print()


glob_match('../files', '*2*.t*')
glob_match('../files/subfolder', '*1_t*file_*c*.t*')