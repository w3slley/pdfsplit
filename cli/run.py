import sys
from split import split_pdf

if (len(sys.argv) == 2 and '.pdf' in sys.argv[1]):
    split_pdf(sys.argv[1])
else:
    print('Error: please add the pdf filename as an argument')
