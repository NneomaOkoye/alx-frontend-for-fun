#!/usr/bin/python3
"""
This script converts a Markdown file to an HTML file.

Usage: ./markdown2html.py <inputfile> <outputfile>
"""

import markdown
import sys
import os.path

if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get the input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    # Read the content of the input file
    with open(input_file, 'r') as f:
        md = f.read()

    # Convert Markdown to HTML
    html = markdown.markdown(md)

    # Write the HTML content to the output file
    with open(output_file, 'w') as f:
        f.write(html)

    sys.exit(0)
