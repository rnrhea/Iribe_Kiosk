"""
    Matt Graber

    This script's purpose is to make it possible to have multiple SVGs that each were generated by Adobe Illustrator
    pasted within the same file and not have their styles conflict.

    By default, Illustrator always names its classes "st#", with # being a number starting at 0. "#" is
    incremented with every new color that is added. Thus, in two different SVG files, they could very easily have the same
    class names being used but with different contents. Therefore, this script is intended to change the class prefix from
    "st" to something else of the specified file.

    To run:

    python script_irb_svg_classes.py "in-filename.svg" "out-filename.svg" "st" "new_prefix"

"""

import sys
import re

# Replace any instance of the specified "old_prefix" that is followed immediately by a number with the specified "new_prefix"
def replace_class_prefix(infile, outfile, old_prefix, new_prefix):
    with open(infile, "rt") as fin:
        with open(outfile, "wt") as fout:
            for line in fin:
                fout.write(re.sub(r"st(?=\d)", new_prefix, line))
    fin.close()
    fout.close()
    print("Replacement complete,", outfile, "has been generated!")

def main():
    replace_class_prefix(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()