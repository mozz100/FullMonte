#!/usr/bin/env python
from argumentholder import ArgumentHolder

ah = ArgumentHolder('Find low-energy conformations.')

ah.add_argument('-s', '--steps',
                metavar = 'N',
                action  = 'store',
                nargs   = 1,
                default = 10,
                type    = int,
                help    = 'number of steps.')

ah.add_argument('-l', '--levl',
                metavar = 'LEVL',
                action  = 'store',
                nargs   = 1,
                default = 'PM3',
                choices = ['AM1', 'PM3', 'PM6'],
                help    = 'model chemistry used.')

ah.add_argument('-o', '--output',
                metavar = 'PATH',
                action  = 'store',
                nargs   = 1,
                dest    = 'output_path',
                help    = 'output file path.')

ah.add_argument('input_file_path', metavar='INPUT_FILE', help='Input file.')

if __name__ == '__main__':
     
    args = ah.parse_args()

    print args
