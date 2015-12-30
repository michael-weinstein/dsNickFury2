
dsNickFury2 User's Guide
========================

About dsNickFury2
-----------------
**Purpose**: dsNickFury is a Python3 program to help select guide RNA sequences for use with any CRISPR/Cas system.  This program can work with any system having activity sites defined by a guide RNA of some maximum length and some PAM sequence of fixed length with or without a degenerate sequence.

**How it works**: This program works by identifying all potential activity sites for any given guide length/PAM sequence combination during its *index* operation.  During *search* operations, a given guide sequence will be searched against the indexed sites to determine if any are similar enough to be of concern in designing a CRISPR targeting strategy.  During a *selection* operation, all potential targets for a system are collected from a sequence (or a list of already-selected targets can be supplied) and analyzed.  The potential targets will then be sorted by their predicted specificity and efficiency (in that order).

#### Version history:
 
*Version 1 (All Shiny and Chrome)*: The original version of this program worked by creating several small files, each containing several thousand potential CRISPR targets from the chosen genome.  Sites were stored sequentially, relative to their genomic locus and every site was matched against the site of interest following a highly-parallelized map/reduce type of scheme.  This version was forked into a server/stand-alone and cluster version, with one being optimized for use on a single system with multiple cores and the other being optimized for use on a cluster system running an SGE job scheduler.  These versions were later rejoined, with cluster or stand-alone mode being specified as an argument.

*Version 2 (CRISPR Divided)*: This version's major change was the introduction of a tree structure to better organize the potential targets.  The indexer now separates targets into multiple bins depending upon their sequence immediately prior to the PAM site.  This requires significantly more computational effort than the previous method of saving them in the order they are found, and will often result in *index* jobs requiring double or triple the amount of time required in the previous version.  This organization of sites, however, makes site *searches* significantly more efficient than the previous version.  Additionally, this version will not list all potential off-targets during a *selection* run for potential target sites with with over 100 potential mismatch sites per allowed mismatch (i.e. with the default setting of 3 mismatches, any site with over 300 potential mismatch sites will show how many potential mismatches it has, but will not list them specifically unless clobber mode is set).  The changes introduced in this version have resulted in significantly faster searches and selections (with some operations seeing a 30-fold improvement in time) and cleaner outputs. 

Setting up the script
---------------------
In order to run, you *MUST* enter either the absolute path (preferred) or the shortcut you use (carries potential risks of errors) to access your python3 interpreter.  Absolute paths *should* always work so long as they are the correct path for a python3 interpreter; passing a shortcut *sometimes* works.  You can do this by looking for where the global variable pythonInterpreterAbsolutePath is set (this should be just after the license information, or just grep for the second time it appears).  Remember to enter the path between the quotes and remove any spaces at the beginning or end.
You can also set some limits on job size while you're editing this portion of the program.  You can set a limit for how many potential targets can be allowed during a single selection mode job and how many parallel jobs can be going at one time for one of these jobs (this can be very important if you are running on a single server with limited resources or a cluster that limits how many items you can have in the job queue).

Requirements:
-------------
This program requires Python3 and the basic Python library (urllib was likely included with your installation).  To run with the **--cluster--** option set, you will (obviously) need to be on a cluster system with a scheduler that can take *qsub* commands.  If you have a cluster that requres different commands to schedule jobs, please contact me and we can look into making this compatible.

Selecting different modes:
--------------------------
There are 3 modes most users will want to run:

*selection* will look through either a list of sequences, or a sequence passed on the command line, or a FASTA sequence file to find potential targets and rank them.

*index* will search a genome and save any potential targets based on the user-defined guide length and PAM sequence.

*search* will look through an indexed genome for anything matching the user-defined target site within the user-defined mismatch tolerance.

The mode will always be passed under the **-m** command line argument and is *always* required for a run.

How to run a job:
-----------------
#### Information to have ready prior to beginning
*Defining your Cas9/Crispr-type system*: Every mode requires the user to define what their system looks like.  This will be done by passing either a specific sequence (for searches) or a generic sequence (for indexing and site selection).  A generic sequence with a 20bp guide RNA and a PAM sequence of NGCG can be formatted as:

NNNNNNNNNNNNNNNNNNN_NGCG

or can be written as 

20_NGCG 

any guide length and PAM sequence combination can be indexed and then searched, although you will have to run the program in clobber mode (argument **-9**) to use one with a combined length below 16 bases (such a system would likely be of limited use, and you would need to take care to avoid creating memory errors due to too many matches during a search).  PAM sequences can, and often will, have at least one degenerate nucleotide in them.  The guide and PAM must be separated with an underscore.  For indexing a system that can take multiple lengths of gRNA, index the longest possible version (and even a little extra), as that same indexed genome can be used for shorter versions as well.  A
specific sequence will be required for search jobs.  That is defined the same way, except that the N's in the gRNA portion will be replaced by your actual sequence.  The sequence will be passed under the **-s** command line argument.

*Selecting your genome*: Every job will require passing a genome argument.  This argument will be passed as **-g** [GENOME].  For indexing, this will define the name of the genome (such as HG38).  Genome names can be arbitrary, but should be informative and easy to remember, as that name will be used to select it for searching in the future.

*Selecting a species*: You will need to choose a species for your genome when indexing it.  In order to get back information regarding genes associated with a target or mismatch site, please be sure that the species name given is the same as is used by the Ensembl servers.  The indexer will warn you if you are selecting a species not listed in the ensembl databases and you will have to run with command line option **-9**.  You will also need to use this option if you wish to index a genome with the same genome name but a different species identifier as a previously-indexed genome (you probably don't want to have this situation).

#### Run Modes
*Site selection*: This requires the user to define a target sequence, which can either be in a file (passed as **--targetFasta** [filename] or directly as **--targetSequence** [sequence]).  Alternatively, the user can pass a list of already-determined target sites in a file as **--targetList** [filename] with one potential target site per line.  This also requires the user to define their system as described above.  The genome name is also required and can be passed under the **-g** argument.  Optional arguments include mismatch tolerance (**-t**, default value of 3) and parallel jobs per search (**-p**, default of 10).
Azimuth analysis can be skipped entirely by passing **--skipAzimuth**.

SAMPLE COMMANDLINE:

    dsNickFuryX.X.py -m selection -s 20_NGG -g hg38 --targetFasta file.fa

*Mismatch search*: This requires the user to define their system, as described above (passed as the **-s** argument and using a specific sequence instead of generic).  This also requires the user to define which genome they wish to search (passed as the **-g** argument).  The program will search the folder of indexed genomes for a suitable one (having a compatible PAM sequence, and a guide RNA of equal or greater length).  Optional arguments include the number of parallel jobs for the search (passed as **-p** with a default of 20) and mismatch tolerance (passed as **-t** with a default of 3).

SAMPLE COMMAND LINE:

    dsNickFuryX.X.py -m search -s GATTACAGATTACAGAATTC_TGG -g hg38

*Genome index*: This will be done for every genome/system combination unless a suitable indexed genome already exists (one with the same PAM and longer gRNA size). The indexing will gather information about target frequency between contains and will also generate files listing these target sequences.  This speeds up the search process tremendously.  The user will have to define a generic target sequence for their system (as described above, passed under the **-s** argument as always).  They will also need to state which species the genome is from (passed as **--species**).  The stated species should use the same name as is listed in ensembl's website.  A FASTA formatted sequence is required for indexing.  This is passed under the **-f** argument.  The FASTA file needs to have been indexed (a companion .fai file generated) by SAMtools or another equivalent FASTA indexer.  If there are specific chromosomes/contigs in the genome you want to skip, simply delete their lines from the .fai file and they will be ignored by the indexer.  Optional arguments include **--ordered**, which will generate only a single parallel job per contig.  Users can set the chunk size for parallel chromosome indexing.  With more nodes available for computing or a smaller genome, a smaller chunksize can decrease the time required before indexing is complete.  This can be passed as **--chunkSize** INT, with INT representing an integer value.  If a value less than 100 is passed, it will be assumed to mean megabases.  To avoid causing conflicts with your cluster, the program may automatically increase your chunk size to avoid creating too many parallel jobs at once, depending on the parallel job limit you set in the program's global variables.  In order to ignore/overwrite an existing suitable genome or use a species name not listed on ensembl, run the indexing with command option **-9** or **--clobber**.

SAMPLE COMMAND LINE:

    dsNickFuryX.X.py -m index -f hg38.fa -g hg38 --species Human -s NNNNNNNNNNNNNNNNNNNN_NGG
    
*Tree-structure options*: With version 2 of this program, a tree-structure was put in place to organize the target sites found during the index operation.  This results in the indexing taking significantly longer than the previous version (but much faster searching later on).  The indexing operation now consists of three distinct steps:

1. Indexing (finding all potential targets for the system)
2. Tree compilation (taking the tree level 1 data and expanding it into level 2)
3. Saving a copy of the tree structure for rapid access during searches

Both tree levels are set by default to 5.  This means that threre will be up to 1024 level 1 bins created and up to 1024 level 2 bins created for each level 1 bin.  These values can be altered with the **--treeLevel1** and **--treeLevel2** options (you must pass an integer value).  Setting these values either too high or too low can cause the program to potentially crash or perform very slowly during the index operation.  If your index operation is disrupted after one of the three steps is completed, you may restart it with the same command line used previously, adding in **--directToCompiler** in order to restart the tree compilation job (any incompletely compiled bins will begin again from the start, while any completed bin will be left alone) or **--recreateTree** to restart the process of saving the tree structure for quick access.  This can also be used to recreate a corrupted or lost tree file without having to reindex the whole genome.
    
**Azimuth analysis:**

In order to run an analysis using Azimuth, you will need an API key stored in the same directory as this program in file azimuth.apikey.  If you require a key, please contact the people responsible for maintaining the Azimuth server.  If you are not using the standard NGG Cas9/Crispr system with a 20 base guide, this program will try to force your sites to fit into their model.  Because of this, the predictions may not be accurate.

Thank you for allowing me to assist in your efforts,

Michael Weinstein
