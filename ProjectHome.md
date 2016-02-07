# NOTE #


---


**The pdbtools suite is now hosted on github: https://github.com/harmslab/pdbtools.  The documentation below, as well as sources, are still here for historical reasons.  -- Mike Harms, 2014-10-08**


---











# Introduction #
pdbTools is a set of command line [python](http://www.python.org) scripts that manipulate [wwPDB](http://www.wwpdb.org/) protein and nucleic acid structure files.  There are many programs, both open source and proprietary, that perform similar tasks; however, most of these tools are buried within programs of larger functionality.  Thus, relatively simple calculations often involve learning a new program, compiling modules, and installing libraries. To fill a niche (and get the tasks done that I needed done), I started writing my own toolset.  This has evolved into the pdbTools suite.  The suite of programs is characterized by the following philosophy:

  1. Each program should run as a stand-alone application with a standard, GNU/POSIX style command line interface.
  1. Each program should be written in such a way to allow it to be used as a library of functions for more complex programs.
  1. Programs should require a minimum of external dependencies.

Most of the scripts will run "out of the box" using a python interpreter.  The command line parser is designed to be flexible.  It will take an arbitrarily long list of pdb files, pdb ids, text files with pdb ids, or some mixture of all three.  If the pdb file or id is not in the working directory, scripts will attempt to download the pdb file from [RCSB](http://www.rcsb.org/).  Depending on the type of operation being done, a program will either write output files in the working directory or will print to stdout.  All structure outputs are written in standard pdb format.  All data outputs are in fixed-width column format.  They were designed to be read by the statistics package [R](http://cran.r-project.org/); however, they should be easily parsed by other graphing programs.

**Note:** These scripts are only compatible with Python version 2.4-2.7.

# Current functions #

## Miscellaneous ##
  * download pdb files from the RCSB database: [pdb\_download.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_download.py)

## Structure-based calculations ##
### Geometry ###
  * calculate protein center of mass: [pdb\_centermass.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_centermass.py)
  * calculate distance distributions: [pdb\_dist-filter.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_dist-filter.py),  [pdb\_ion\_dist.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_ion-dist.py)
  * calculate backbone torsion angles: [pdb\_torsion.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_torsion.py)
  * calculate atom-by-atom solvent accessibility [pdb\_sasa.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_sasa.py)(requires [NACCESS](http://www.bioinf.manchester.ac.uk/naccess/))
  * find disulfide bonds based on distance: [pdb\_disfulfide.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_disulfide.py)
  * find residues within some distance of each other: [pdb\_contact.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_contact.py), [pdb\_water-contact.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_water-contact.py), [pdb\_close-contacts.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_close-contacts.py)
  * find number of atoms neighboring another: [pdb\_neighbors.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_neighbors.py)
  * find ligands in structure file (ignoring boring ligands like water): [pdb\_ligand.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_ligand.py)
  * figure out oligomerization state of macrmolecule: [pdb\_oligomer.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_oligomer.py)

### Energy calculation ###
  * calculate coulomb energy: [pdb\_coulomb.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_coulomb.py)
  * calculate the dipole moment of the protein: [pdb\_moment.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_moment.py)
  * calculate pKa of ionizable groups using the Solvent-Accessibility-modified Tanford-Kirkwood method [pdb\_satk.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_satk.py) (requires fortran compiler)
### Structure properties ###
  * extract structure experiment properties: [pdb\_exper.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_exper.py)
  * extract protein sequence from structure: [pdb\_seq.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_seq.py)
  * calculate theoretical pI, MW, fraction titratable residues, charge: [pdb\_param.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_param.py)

## File/structure manipulation ##
  * add polar hydrogens: [pdb\_addH.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_addH.py) (requires [CHARMM](http://www.charmm.org/))
  * add missing heavy atoms, remove alternate conformations, etc.: [pdb\_clean.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_clean.py) (requires [CHARMM](http://www.charmm.org/))
  * mutate a residue: [pdb\_mutator.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_mutator.py) (requires [CHARMM](http://www.charmm.org/))
  * renumber atoms: [pdb\_atom-renumber.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_atom_renumber.py)
  * renumber residues: [pdb\_residue-renumber.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_residue-renumber.py)
  * offset all residues by a fixed amount: [pdb\_offset.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_offset.py)
  * center protein in xyz space: [pdb\_centermass.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_centermass.py)
  * places the asymmetric unit inside the unit cell: [pdb\_centerasu.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_centerasu.py)
  * take subset of residues from file: [pdb\_subset.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_subset.py)
  * split an NMR ensemble structure into individual files: [pdb\_splitnmr.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_splitnmr.py)
  * take a set of pdb files and create an individual directory for each one: [pdb\_pdb2dir.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_pdb2dir.py)
  * load data into the b-factor column: [pdb\_bfactor.py](http://code.google.com/p/pdb-tools/source/browse/trunk/pdbTools/pdb_bfactor.py)

Some of the programs are written as interfaces to other programs: [CHARMM](http://www.charmm.org/),  [NACCESS](http://www.bioinf.manchester.ac.uk/naccess/), which must be downloaded and installed separately if their functions are desired.  To use pdb\_satk.py, a set of fortran packages must be compiled.

## Contributing ##
If you find a bug or have an idea for a program you'd like in this package, please let me know.  You can also send me your own code to incorporate, preferably via an svn branch.

# Project Owner #
  * Mike Harms (http://harmslab.uoregon.edu)

# Contributors #
  * Marcin Cieślik