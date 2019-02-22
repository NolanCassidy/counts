"""
Count the number of occurrences of each major code in a file.
Authors: jsventek (Joe Sventek)

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    reads the major codes, 1 per line, from the file provided in the argument
    outputs each different major code, 1 per line with the number of times
        that the major appears in the file.  The output is sorted by major code.

    inputs:
        majors_file: a text file containing major codes, one per line

    outputs:
        sorted list of different major codes in the file, with each major
        code followed by the number of times that the major code appears in
        the file is printed.
    """
    majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    if len(majors) == 0:
        print(majors_file, 'is empty')
        return

    majors.append('This is not a legal major')	# our sentinel element
    current_major = majors[0]			# the check for an empty list
                                                # must occur before this line
    count = 0
    for major in majors:
        if major == current_major:
            count += 1
        else:
            print(current_major, count)
            current_major = major
            count = 1

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
