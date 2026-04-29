"""main for hashcheck
"""
from argparse import ArgumentParser
from pathlib import Path
from hashlib import sha512
import sys

sys.dont_write_bytecode = True

#------------------------------------------------------------------------------
# check hash
#------------------------------------------------------------------------------

def hash_check(file_name, hash_value):
    """check hash

    parameters
    ----------
    file_name : str
        name of file
    hash_value : str
        value of hash
    """
    try:
        # calc hash value
        with open(file_name, 'rb') as fp:
            print(f'{Path(file_name).name} ... ', end='', flush=True)
            file_hash = sha512()
            while chunk:=fp.read(8192):
                file_hash.update(chunk)
        # compare hash value
        if hash_value == file_hash.hexdigest():
            print('OK')
        else:
            print('NG')
            print(f'  reference: {hash_value}')
            print(f'  compare  : {file_hash.hexdigest()}')
    except FileNotFoundError:
        print(f'file not found (file:<{file_name}>)')

#------------------------------------------------------------------------------
# CLI
#------------------------------------------------------------------------------

def parse_args():
    """parse command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument('file_name', type=str, help='name of file for target')
    parser.add_argument('hash_value', type=str, help='value of hash (sha512)')
    return parser.parse_args()


def main():
    """main
    """
    # parse command line arguments
    args = parse_args()

    # initialize
    file_name = args.file_name
    hash_value = args.hash_value

    # hash check
    hash_check(file_name, hash_value)


if __name__ == "__main__":
    main()
