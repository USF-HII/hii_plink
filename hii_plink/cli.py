import argparse
import sys

import hii_plink.app
import hii_plink.release

def main():
    parser = argparse.ArgumentParser(prog='hii_plink', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v', '--version', action='version', version=hii_plink.release.__version__)

    subparsers = parser.add_subparsers(help='sub-command help')

    #-----------------------------------------------------------------------------------------------------
    # remove duplicates
    #-----------------------------------------------------------------------------------------------------

    parser_remove_duplicates = subparsers.add_parser('remove_duplicates', help='Remove duplicate snps in plink binary files')

    parser_remove_duplicates.set_defaults(func=hii_plink.app.remove_duplicates)

    parser_remove_duplicates.add_argument('--plink_prefix')

    parser_remove_duplicates.add_argument('-o', '--output_prefix')

    #-----------------------------------------------------------------------------------------------------
    # plink update snpid from coordniate
    #-----------------------------------------------------------------------------------------------------

    parser_snpid_from_coord_update = subparsers.add_parser('snpid_from_coord_update',
                                                    help='Plink update using output from snptk snpid_from_coord')

    parser_snpid_from_coord_update.set_defaults(func=hii_plink.app.snpid_from_coord_update)

    parser_snpid_from_coord_update.add_argument('--plink_prefix')

    parser_snpid_from_coord_update.add_argument('--update_file')

    parser_snpid_from_coord_update.add_argument('--delete_file')

    parser_snpid_from_coord_update.add_argument('-o', '--output_prefix')

    #-----------------------------------------------------------------------------------------------------
    # plink update snpid and position
    #-----------------------------------------------------------------------------------------------------

    parser_snpid_and_position_update = subparsers.add_parser('snpid_and_position_update',
                                                    help='Plink update using output from snptk snpid_and_position')

    parser_snpid_and_position_update.set_defaults(func=hii_plink.app.snpid_and_position_update)

    parser_snpid_and_position_update.add_argument('--plink_prefix')

    parser_snpid_and_position_update.add_argument('--delete_file')

    parser_snpid_and_position_update.add_argument('--update_file')

    parser_snpid_and_position_update.add_argument('--coord_file')

    parser_snpid_and_position_update.add_argument('--chr_file')

    parser_snpid_and_position_update.add_argument('-o', '--output_prefix')

    #-----------------------------------------------------------------------------------------------------
    # parse
    #-----------------------------------------------------------------------------------------------------

    if len(sys.argv) > 1:
        args = parser.parse_args(sys.argv[1:])
        args.func(vars(args))
    else:
        parser.print_help()
        sys.exit(1)
