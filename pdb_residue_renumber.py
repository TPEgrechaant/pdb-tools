#!/usr/bin/env python

# Copyright 2007, Michael J. Harms
# This program is distributed under General Public License v. 3.  See the file
# COPYING for a copy of the license.  

__description__ = \
"""
pdb_residue-renumber.py

Takes a pdb file and renumbers all chains starting from 1.  Prints renumbered
file to stdout.  If an output file is specified, the conversion from original
numbering to new numbering will be placed in this file.
"""

__author__ = "Michael J. Harms"
__date__ = "070529"
__usage__ = "pdb_residue.py pdb_file [alignment_file]"

import os, sys

def pdbResidueRenumber(pdb):
    """
    Renumber the residues in a pdb file so they are continuous.
    """

    # Initialize output lists
    fmt = "%-8s%6s%6i%10s\n"
    align_out = []
    pdb_out = []

    start = True
    for line in pdb:
        # For and ATOM record, update residue number
        if line[0:4] == "ATOM":
            # If this is the first residue in a chain, set up counter etc.
            if start:
                start = False
                current_res = line[22:26]
                if int(line[22:26]) < 1:
                    output_res = 1
                else:
                    output_res = int(line[22:26])

                align_out.append(fmt % (line[17:22],current_res,output_res,
                                        int(current_res)==output_res))

            # If this is a new residue, update the counter
            if line[22:26] != current_res:
                output_res += 1
                current_res = line[22:26]

                align_out.append(fmt % (line[17:22],current_res,output_res,
                                        int(current_res)==output_res))

            pdb_out.append("%s%4i%s" % (line[0:22],output_res,line[26:]))

        # If this is a terminii record, reset the renumbering tool
        elif line[0:3] == "TER":
            pdb_out.append("%s%4i%s" % (line[0:22],output_res,line[26:]))
            start = True

        # Print every other record without modification
        else:
            pdb_out.append(line)

    # Insert REMARK about renumber
    remark_index = [l[0:6] for l in pdb].index("REMARK")
    pdb_out.insert(remark_index,"%-80s\n" %
                   ("REMARK    *ALL GAPS IN CHAIN RENUMBERED*"))
   
    return pdb_out, align_out

def main():
    """
    Function to call if called from the command line.
    """

    from helper import cmdline

    # Parse command line
    cmdline.initializeParser(__description__,__date__)
    cmdline.addOption(short_flag="a",
                      long_flag="align-out",
                      action="store_true",
                      default=False,
                      help="write out residue alignment file.")
    
    file_list, options = cmdline.parseCommandLine()

    for pdb_file in file_list:
        
        f = open(pdb_file,'r')
        pdb = f.readlines()
        f.close()

        pdb_out, alignment = pdbResidueRenumber(pdb)

        short_pdb = os.path.split(pdb_file)[-1][:-4]
        g = open("%s_res-renum.pdb" % short_pdb,"w")
        g.writelines(pdb_out)
        g.close()

        if options.align_out:
            print "Residue alignment written out."

            alignment.insert(0,"#%s" % pdb_out[0])
            g = open("%s_res-algn.out" % short_pdb,'w')
            g.writelines(alignment)
            g.close()

if __name__ == "__main__":
    main()


