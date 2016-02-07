# NOTE #


---


**The pdbtools suite is now hosted on github: https://github.com/harmslab/pdbtools.  The documentation below, as well as sources, are still here for historical reasons.  -- Mike Harms, 2014-10-08**


---


#summary pdb-tools User Guide

# Usage #

Almost all programs in the pdbTools suite have the same usage:

pdb\_XXXX.py pdb\_input optional\_args > output

**pdb\_input** can be one of the following (in any arbitrary combination):
  * pdb files
  * directories of pdb files
  * four-character pdb ids
  * text files containing whitespace delimited (i.e. space, tab, carriage return) lists of any combination of the other allowed types of arguments. If the list of arguments contains pdb files or ids that do not exist locally, the parser will attempt to download the files from the RCSB database.

**optional\_args**: Although the arguments to each program are identical, the options are quite different depending on the program requirements.  The best way to learn how to use a particular program is to type pdb\_XXXX.py --help.  This will spit out a list of available options.  In most cases, the options are actually optional: the program will use a sane default if none is specified.  In some cases (notably pdb\_mutator.py), options must be specified for the program to run.

**output**: Most scripts dump out a pdb file to standard out.  This can be captured using the ">" redirect.   Some write an output file that uses the name of the input pdb file as a suffix (e.g. pdb\_close-contacts.py 1stn.pdb creates a file called 1stn.pdb.close\_contacts).

# Installation #

Download and install the [Python](http://www.python.org) interpreter (version 2.4 or greater).  Download the [pdb-tools](http://code.google.com/p/pdb-tools/downloads/list) archive and extract using the extraction utility of your choice (tar, ark, winzip, etc.).  Alternatively, you can download the bleeding-edge scripts using svn with the command: `svn checkout http://pdb-tools.googlecode.com/svn/ pdb-tools-read-only`.  Copy the pdbTools directory to a convenient location on your disk.  Unix-style OS users can put this directory in the `$PATH` environment variable and then run any command in the suite from the command line (assuming python is already in the `$PATH`, which it usually is).  As far as I know, Windows users must type `python path-to-pdb-tools/pdb-XXXX.py ARGS` every time they run a script.

Some scripts require installation of third-party programs.  These should be installed according to the instructions given by the third-party, then placed into the $PATH variable.  To use the scripts that require CHARMM, the `$CHARMM` environment variable must be set to the directory containing the `charmm` binary and the `$CHARMM_LIB` environment variable to the directory containing the charmm parameter files.