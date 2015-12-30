#!/usr/bin/env python3
'''
Software License
Commercial reservation
This License governs use of the accompanying Software, and your use of the Software constitutes acceptance of this license.

You may use this Software for any non-commercial purpose, subject to the restrictions in this license. Some purposes which can be non-commercial are teaching, academic research, and personal experimentation. 

You may not use or distribute this Software or any derivative works in any form for any commercial purpose. Examples of commercial purposes would be running business operations, licensing, leasing, or selling the Software, or distributing the Software for use with commercial products. 

You may modify this Software and distribute the modified Software for non-commercial purposes; however, you may not grant rights to the Software or derivative works that are broader than those provided by this License. For example, you may not distribute modifications of the Software under terms that would permit commercial use, or under terms that purport to require the Software or derivative works to be sublicensed to others.

You agree: 
1.	Not remove any copyright or other notices from the Software.
2.	That if you distribute the Software in source or object form, you will include a verbatim copy of this license.
3.	That if you distribute derivative works of the Software in source code form you do so only under a license that includes all of the provisions of this License, and if you distribute derivative works of the Software solely in object form you do so only under a license that complies with this License.
4.	That if you have modified the Software or created derivative works, and distribute such modifications or derivative works, you will cause the modified files to carry prominent notices so that recipients know that they are not receiving the original Software. Such notices must state: (i) that you have changed the Software; and (ii) the date of any changes.
5.	THAT THIS PRODUCT IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS PRODUCT, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  YOU MUST PASS THIS LIMITATION OF LIABILITY ON WHENEVER YOU DISTRIBUTE THE SOFTWARE OR DERIVATIVE WORKS.

6.	That if you sue anyone over patents that you think may apply to the Software or anyone's use of the Software, your license to the Software ends automatically.
7.	That your rights under the License end automatically if you breach it in any way.
8.	UCLA and the Regents of the University of California reserves all rights not expressly granted to you in this license.

9.	Nothing in this Agreement grants by implication, estoppel, or otherwise any rights to any intellectual property owned by the Regents of the University of California, except as explicitly set forth in this license.
10.	You will hold the Regents of the harmless for all claims, suits, losses, liabilities, damages, costs, fees, and expenses resulting from their respective activities arising from this license.  
11.	You will not use any name, trade name, trademark, name of any campus, or other designation of the Regents of the University of California in advertising, publicity, or other promotional activity, except as permitted herein.
'''

#This is the path for the python interpreter.  You must set it before this will run.  If you are unsure what this is, try the command "which python3" or "which pypy3" and try pasting the path returned between the quotes on the next line.
global pythonInterpreterAbsolutePath
pythonInterpreterAbsolutePath = ""  #Set the absolute path for your python interpreter here between the quotes.  Depending on your system configuration, you may also be able to use a shortcut, such as python3, but that has a greater chance of errors
    
#USEFUL DEFAULT SETTINGS HERE
global selectionModeTargetLimitPerJob
selectionModeTargetLimitPerJob = 0 #This prevents a user from submitting a job with too many target sites that might overload or degrade performance on the system.  Clobber mode can override this.  Change this value according to your system's capabilities.  Set to 0 or negative value for no limit.

global clusterDefaultSelectionModeParallelJobLimit; global standAloneDefaultSelectionModeParallelJobLimit
clusterDefaultSelectionModeParallelJobLimit = 230  #Limit on how many simultaneous parallel jobs can be going at once on a cluster (set this based on the limit for how many queued items you can have)
standAloneDefaultSelectionModeParallelJobLimit = 64  #Limit on how many simultaneous parallel jobs can be going if run on a single system.  Change according to your machine.

global currentVersion
currentVersion = "2.0.1"

global versionName
versionName = "GuideSeq Divided... I never asked for this"

global yearWritten
yearWritten = "2015"

def yesAnswer(question):  #asks the question passed in and returns True if the answer is yes, False if the answer is no, and keeps the user in a loop until one of those is given.  Also useful for walking students through basic logical python functions
    answer = False  #initializes the answer variable to false.  Not absolutely necessary, since it should be undefined at this point and test to false, but explicit is always better than implicit
    while not answer:  #enters the loop and stays in it until answer is equal to True
        print (question + ' (Y/N)')  #Asks the question contained in the argument passed into this subroutine
        answer = input('>>') #sets answer equal to some value input by the user
        if str(answer) == 'y' or str(answer) == 'Y':  #checks if the answer is a valid yes answer
            return True  #sends back a value of True because of the yes answer
        elif str(answer) == 'n' or str(answer) == 'N': #checks to see if the answer is a valid form of no
            return False  #sends back a value of False because it was not a yes answer
        else: #if the answer is not a value indicating a yes or no
            print ('Invalid response.')
            answer = False #set ansewr to false so the loop will continue until a satisfactory answer is given

def reportUsage(details):  #this will report usage back to us.  This is required by the people who maintain the Azimuth server.  This will not send back any details of your job except if azimuth was used.
    import urllib.request
    url = "http://pathways.mcdb.ucla.edu/cgi-bin/MW_counter/counter.cgi?counter=" + details
    try:
        req = urllib.request.urlopen(url)
    except:
        pass        

def printStartUp():
    print("Double-stranded Nick Fury -- Watch your Crispr targets with both eyes.")
    print("Version " + currentVersion + " (" + versionName + ")")
    print("By Michael M. Weinstein, Copyright " + yearWritten)
    print("Dan Cohn Laboratory and Collaboratory, University of California, Los Angeles")
        
def printManual():
    import urllib.request
    try:
        import textwrap
        wrap = True
    except:
        wrap = False
    try:
        import random
        egg = random.randint(1,100)
        if egg == 42:
            print(urllib.request.urlopen("https://raw.githubusercontent.com/michael-weinstein/dsNickFury2/master/ajd/AJD.txt").read().decode('utf-8'))  #this works better if your terminal has a dark background
    except:
        pass
    manualURL = 'https://raw.githubusercontent.com/michael-weinstein/dsNickFury2/master/readme.md'
    try:
        rawManual = urllib.request.urlopen(manualURL)
        text = rawManual.read().decode('utf-8')
        print("Manual from " + manualURL)
        if not wrap:
            print(text)
        else:
            text = text.split("\n")
            for paragraph in text:
                print("\n".join(textwrap.wrap(paragraph, width = 120, break_long_words = False)))
    except:
        print("Unable to download and display manual.  Please view it in your browser at:\n\n" + manualURL + "\n")
    try:
        import random
        egg = random.randint(1,100)
        if egg == 42:
            print(urllib.request.urlopen("https://raw.githubusercontent.com/michael-weinstein/dsNickFury2/master/ajd/AJD.txt").read().decode('utf-8'))  #this works better if your terminal has a dark background
    except:
        pass
    quit()
    
def checkPythonInterpreterAbsolutePath(absPath):
    import os
    import subprocess
    if not absPath:
        printManual()
        raise RuntimeError("ABORTED: You must set the absolute path for your python interpreter at the beginning of this script.")
    if not os.path.isfile(absPath):  #if the absolute path is not actually a file, check if we have an alias we can expand upon
        import subprocess
        try:
            absPath = subprocess.check_output(['which',absPath]).decode('utf-8').strip()
        except subprocess.CalledProcessError:
            raise RuntimeError("ABORTED: Python interpreter not found at " + absPath + " and it does not appear to be a valid alias.  Please correct the location.")
    return absPath
pythonInterpreterAbsolutePath = checkPythonInterpreterAbsolutePath(pythonInterpreterAbsolutePath)

#===================================Command line Argument Checking===========================================

class Args(object):
    
    def __init__(self):
        import os
        import argparse #loads the required library for reading the commandline
        parser = argparse.ArgumentParser()
        parser.add_argument ("--manual", help = "Print out the user manual and sample command lines.", action = 'store_true')
        parser.add_argument ("-m", "--mode", help = "Specify how the program is to run (what the desired task is)")
        parser.add_argument ("-g", "--genome", help = "Specify the genome for searching or indexing.")
        parser.add_argument ("-d", "--inputDirectory", help = "Specify genome index directory for a worker job.")
        parser.add_argument ("-f", "--inputfile", help = "Specify a single input file for splitting")
        parser.add_argument ("--tempDir", help = "Temporary directory name for parallel jobs")
        parser.add_argument ("-p", "--parallelJobs", help = "Max number of parallel jobs at once. (Or per search if running in selection mode)")
        parser.add_argument ("-9", "--clobber", help = "Do not ask before overwriting files.", action = 'store_true')
        parser.add_argument ("-w", "--workerID", help = "Worker process ID.  Users should not be setting this value.")
        parser.add_argument ("-s", "--sequence", help = "Sequence of interest.  Format: NNNNNNGUIDERNANNNNNN_PAM")
        parser.add_argument ("-t", "--mismatchTolerance", help = "Maximim number of mismatches permitted for a positive result.")
        parser.add_argument ("--verbose", help = "Run in verbose mode", action = 'store_true')
        parser.add_argument ("--mock" , help = "Print exec commands instead of running them.", action = 'store_true')
        parser.add_argument ("--ordered", help = "Do not break up chromosomes for parallel analysis.", action = 'store_true')
        parser.add_argument ("-c", "--chunkSize", help = "Specify the chunk size for parallel genome annotation.")
        parser.add_argument ("--chromosome", help = "Used to specify the chromosome/contig ID.  This should be passed by the machine and not the user.")
        parser.add_argument ("--start", help = "Used to specify the starting byte of the FASTA for indexing.  This should be passed by the machine and not the user.")
        parser.add_argument ("--length", help = "Used to specify the bytelength of the chunk to be indexed by the program.  This should be passed by the machine and not the user.")
        parser.add_argument ("--forceJobIndex", help = "Force the indexing supervisor instance to take a specific job index.  Mostly useful for debugging functions.")
        parser.add_argument ("--outputDirectory", help = "Directory for outputting search results to a hypervisor.  This should generally be passed by the machine and not the user.")
        parser.add_argument ("--noCleanup", help = "Leave behind any temporary files for future inspection.", action = 'store_true')
        parser.add_argument ("--forceGenome", help = "Force the search supervisor to use this genome directory.  Generally this should be passed by the machine and not the user.")
        parser.add_argument ("--species", help = "Tell the indexer which species the genome is from.")
        parser.add_argument ("--targetSequence", help = "Enter a long sequence here to search for and analyze potential targets.")
        parser.add_argument ("--targetFasta", help = "Enter a file name for a FASTA file to search for and analyze potential target sites.")
        parser.add_argument ("--targetList", help = "Enter a list of potential sites to analyze for off-target risk.")
        parser.add_argument ("--noForcedBases", help = "Prevent forcing bases 1 and/or 3 in the guide RNA to match those submitted for Azimuth analysis")
        parser.add_argument ("--skipAzimuth", help = "Do not attempt Azimuth analysis.", action = 'store_true')
        parser.add_argument ("--parallelJobLimit", help = "Set a limit on the number of parallel jobs allowed at once in the queue for highly parallelized tasks (this MUST be set below your scheduler's limit for queued jobs for a single user, and should be set 5-10 percent below it).")
        parser.add_argument ("--genomeDirectory", help = "Specify an alternate directory to search for suitable indexed genomes.")
        parser.add_argument ("--annotationExpansion", help = "Specify how far from the target site to search for an annotated gene/genomic feature (default is 1KB).")
        parser.add_argument ("--azimuthSequence", help = "Specify a sequence for Azimuth analysis.")
        parser.add_argument ("--outputToFile", help = "In selection mode, dump the output to the filename passed as an argument here.")
        parser.add_argument ("--scratchFolder", help = "Specify a directory to use for writing temporary (job) folders.")
        parser.add_argument ("--cluster", help = "Specify that this is running on a cluster system.", action = "store_true")
        parser.add_argument ("--standAlone", "--standalone", help = "Specify that this is running on a single system or server.", action = "store_true")
        parser.add_argument ("--directToCompiler", help = "If you already have run the index, but compiling did not complete successfully, try this to recompile.", action = "store_true")
        parser.add_argument ("--recreateTree", help = "Recreate the tree pickle for an existing genome index.", action = "store_true")
        parser.add_argument ("--bins", help = "Pass a comma-separated list of bins for this compiler instance to work on.")
        parser.add_argument ("--treeLevel1", help = "Pass an integer value for the first level of the tree")
        parser.add_argument ("--treeLevel2", help = "Pass an integer value for the second level of the tree")
        args = parser.parse_args()  #puts the arguments into the args object
        
        if args.standAlone and args.cluster: #You really can't be both.
            raise RuntimeError("Aborted: You must specify either --cluster or --standAlone.  You can't be both.")
        if not (args.standAlone or args.cluster or args.manual) and args.mode in ['search', 'index', 'selection']:
            raise RuntimeError("ABORTED: You must specify if this will be running on a stand-alone system or a cluster. (--standAlone or --cluster)")
        else:
            if args.standAlone:
                self.standAlone = True
                self.cluster = False
            if args.cluster:
                self.cluster = True
                self.standAlone = False
        if not args.mode and not args.manual:  #series of case statements for mode to determine which set of inputs to validate.  If no mode was set, it will see if the user is asking for the manual.  
            raise RuntimeError("ABORTED: No run mode was set on the commandline.")
        self.mode = args.mode
        if not args.genomeDirectory:
            self.genomeListDirectory = "genomes/"
        else:
            self.genomeListDirectory = args.genomeDirectory
            if not self.genomeListDirectory[-1] == "/":
                self.genomeListDirectory += "/"
            if not os.path.isdir(self.genomeListDirectory) and not self.mode == 'index':
                raise RuntimeError("ABORTED: User-specified genome: " + self.genomeListDirectory + " not found.")
        if args.mode == 'worker':
            self.setWorkerArgs(args)
        elif args.mode == 'search':
            self.setSearchArgs(args)
        elif args.mode == 'index':
            self.setIndexArgs(args)
        elif args.mode == 'FASTAWorker':
            self.setFASTAWorkerArgs(args)
        elif args.mode == 'selection':
            self.setSelectionArgs(args)
        elif args.mode == 'compiler':
            self.setCompilerArgs(args)
        elif args.manual:
            printManual()
            quit()
        else:
            raise RuntimeError('ABORTED: Invalid/no mode set on commandline.  Please select a mode or run with --manual set for assistance.')
            
    def setSelectionArgs(self, args):  #validating and setting arguments for selection of targets from a user-provided sequence
        import os
        self.sequence = args.sequence
        if not self.sequence:
            raise RuntimeError("ABORTED: You must specify a generic sequence to describe your system (see manual, argument --manual) for more information.")
        if "_" in args.sequence:
            guide, pam = args.sequence.split("_")
            try:
                guide = int(guide)
            except ValueError:
                pass
            else:
                args.sequence = "N"*guide + "_" + pam
            self.sequence = args.sequence.upper()
        else:
            raise RuntimeError("ABORTED: Invalid sequence passed. Please include an underscore between the guide and PAM sequences.")
        if not len(self.sequence) > 15 and not args.clobber:
            raise RuntimeError("ABORTED: This guide+pam combination appears too short, and will likely cause memory and other errors.  Rerun in clobber mode (argument -9) to proceed anyway.")
        self.targetSequence = args.targetSequence
        self.targetFasta = args.targetFasta
        if self.targetFasta and not os.path.isfile(self.targetFasta):
            raise RuntimeError("ABORTED: " + self.targetFasta + " is not a valid file.")
        self.targetList = args.targetList
        if self.targetList and not os.path.isfile(self.targetList):
            raise RuntimeError("ABORTED: " + self.targetList + " is not a valid file.")
        if not args.genome:
            raise RuntimeError("ABORTED: You must set a genome.  See manual (run with --manual) for details.")
        self.genome = args.genome.upper()
        self.verbose = args.verbose
        self.mock = args.mock
        if args.parallelJobs:
            try:
                self.parallelJobs = int(args.parallelJobs)
            except ValueError:
                raise RuntimeError("ABORTED: Parallel jobs argument must be an integer")
        else:
            self.parallelJobs = 5
        if not args.mismatchTolerance:
            self.mismatchTolerance = 3
        else:
            try:
                self.mismatchTolerance = int(args.mismatchTolerance)
            except ValueError:
                raise RuntimeError("ABORTED: Mismatch tolerance must be an integer.  Please check your command line options and try again.")
        if args.noForcedBases:
            if args.noForcedBases == "1":
                self.noForcedBases = False
                self.noForced1 = True
                self.noForced3 = False
            if args.noForcedBases == "3":
                self.noForcedBases = False
                self.noForced1 = False
                self.noForced3 = True
            else: #if they put in any other argument here, we block forcing either base (this could include 1,3 or all or anything else)
                self.noForcedBases = True
                self.noForced1 = True
                self.noForced3 = True
        else:  #if the argument was left blank or not passed at all, we allow base forcing
            self.noForcedBases = False
            self.noForced1 = False
            self.noForced3 = False
            self.skipAzimuth = args.skipAzimuth
        self.noCleanup = args.noCleanup
        if not args.parallelJobLimit:
            if self.cluster:
                self.maxParallelJobs = clusterDefaultSelectionModeParallelJobLimit  #set this value at the top of the script for your configuration of choice
            if self.standAlone:
                self.maxParallelJobs = standAloneDefaultSelectionModeParallelJobLimit
        else:
            try:
                self.maxParallelJobs = int(args.parallelJobLimit)
            except ValueError:
                raise RuntimeError("ABORTED: Parallel job limit must be an integer.")
        if self.maxParallelJobs < self.parallelJobs:
            self.maxParallelJobs = self.parallelJobs
        self.outputToFile = args.outputToFile
        if self.outputToFile and os.path.isfile(self.outputToFile) and not args.clobber:
            raise RuntimeError("ABORTED: Output file " + self.outputToFile + " already exists.  Run in clobber mode to overwrite.")
        self.clobber = args.clobber
        self.scratchFolder = args.scratchFolder
        if not self.scratchFolder:
            self.scratchFolder = "" #making sure this is cast to a string and not a NoneType (although that will probably add to a string with no trouble)
        else:
            if not self.scratchFolder[-1] == "/":
                self.scratchFolder = self.scratchFolder + "/"  #make sure that the directory name is passed ending with a slash so we can prepend it directly to our tempDir name
            if not os.path.isdir(self.scratchFolder):
                try:
                    os.mkdir(self.scratchFolder)
                except OSError:
                    if not os.path.isdir(self.scratchFolder):  #This could happen because of a data race type condition, if one process creates the directory after this one checks for it, but before it creates it.  This will catch that problem.
                        raise RuntimeError("ABORTED: Unable to create scratch folder.  Check if directory containing this folder already exists.")
            
    def setWorkerArgs(self, args):  #Validating arguments for a search worker.  This should not require too much validation, as users should not be launching worker processes themselves
        self.mode = "worker"
        self.workerID = args.workerID
        self.tempDir = args.tempDir
        self.sequence = args.sequence
        self.mismatchTolerance = int(args.mismatchTolerance)
        self.inputDirectory = args.inputDirectory
        self.verbose = args.verbose
        self.skipAzimuth = True
           
    def setSearchArgs(self, args):  #Validating arguments for launching a search supervisor.  This will require good validations, as users are likely to be launching this on their own.
        import os
        self.mode = "search"
        self.sequence = args.sequence
        if not self.sequence:
            raise RuntimeError("ABORTED: You must specify a sequence to search for.  Remember to place an underscore between the guide and PAM sequences.")
        if not "_" in self.sequence:
            raise RuntimeError("ABORTED: You must include an underscore '_' in your sequence between the guide RNA portion and the PAM sequence.")
        if not len(self.sequence) > 15 and not args.clobber:
            raise RuntimeError("ABORTED: This guide+pam combination appears too short, and will likely cause memory and other errors.  Rerun in clobber mode (argument -9) to proceed anyway.")
        self.sequence = self.sequence.upper()
        if not args.mismatchTolerance:
            self.mismatchTolerance = 3
        else:
            try:
                self.mismatchTolerance = int(args.mismatchTolerance)
            except ValueError:
                raise RuntimeError("ABORTED: Mismatch tolerance must be an integer.  Please check your command line options and try again.")
        self.tempDir = args.tempDir
        self.workerID = args.workerID
        self.inputDirectory = args.inputDirectory
        self.verbose = args.verbose
        self.mock = args.mock
        if not args.forceGenome:
            self.genome = args.genome.upper()  #if a genome is forced by a hypervisor function, this will prevent an error from trying to uppercase a NoneType variable.
        if args.parallelJobs:
            try:
                self.parallelJobs = int(args.parallelJobs)
            except ValueError:
                raise RuntimeError("ABORTED: Parallel jobs argument must be an integer")
        else:
            self.parallelJobs = 5
        self.outputDirectory = args.outputDirectory
        self.noCleanup = args.noCleanup
        self.forceGenome = args.forceGenome
        self.skipAzimuth = True
        self.annotationExpansion = args.annotationExpansion
        if not self.annotationExpansion:
            self.annotationExpansion = 1000
        else:
            try:
                self.annotationExpansion = int(self.annotationExpansion)
            except ValueError:
                raise RuntimeError("ABORTED: Annotation expansion range must be an integer value.")
        self.azimuthSequence = args.azimuthSequence
        if not self.azimuthSequence or self.azimuthSequence == "False":
            self.azimuthSequence = False
        self.scratchFolder = args.scratchFolder
        if not self.scratchFolder:
            self.scratchFolder = "" #making sure this is cast to a string and not a NoneType (although that will probably add to a string with no trouble)
        else:
            if not self.scratchFolder[-1] == "/":
                self.scratchFolder = self.scratchFolder + "/"  #make sure that the directory name is passed ending with a slash so we can prepend it directly to our tempDir name
            if not os.path.isdir(self.scratchFolder):
                try:
                    os.mkdir(self.scratchFolder)
                except OSError:
                    raise RuntimeError("ABORTED: Unable to create scratch folder.  Check if directory containing this folder already exists.")
        self.clobber = False
        if args.clobber:
            self.clobber = True

    def setIndexArgs(self, args):  #Validating arguments for launching an indexing supervisor.  This will also require good validations as users are likely to be launching this on their own.
        import os
        self.mode = "index"
        if not args.sequence:
            raise RuntimeError("ABORTED: No search sequence specified.")
        if "_" in args.sequence:
            guide, pam = args.sequence.split("_")
            try:
                guide = int(guide)
            except ValueError:
                pass
            else:
                args.sequence = "N"*guide + "_" + pam
            self.sequence = args.sequence.upper()
        else:
            raise RuntimeError("ABORTED: Invalid sequence passed. Please include an underscore between the guide and PAM sequences.")
        if not len(self.sequence) > 15 and not args.clobber:
            raise RuntimeError("ABORTED: This guide+pam combination appears too short, and will likely cause memory and other errors.  Rerun in clobber mode (argument -9) to proceed anyway.")
        if not args.inputfile:
            raise RuntimeError("ABORTED: No FASTA specified for searching.")
        if os.path.isfile(args.inputfile):
            self.inputfile = args.inputfile
        else:
            raise RuntimeError("ABORTED: FASTA file: " + args.inputfile + " not found.")
        if not args.genome:
            raise RuntimeError("ABORTED: You must specify the name you want to identify this genome by.")
        self.genome = args.genome.upper()
        self.clobber = args.clobber
        self.mock = args.mock
        self.tempDir = args.tempDir
        self.ordered = args.ordered
        self.workerID = args.workerID
        self.species = args.species.upper()
        if args.chunkSize:
            try:
                args.chunkSize = int(args.chunkSize)
            except ValueError:
                raise RuntimeError("ABORTED: Invalid chunk size passed as argument (must be an integer)")
            self.chunkSize = args.chunkSize
        else:
            self.chunkSize = 20000000
        if self.chunkSize < 100:
            self.chunkSize = 1000000 * self.chunkSize
        if args.forceJobIndex:
            try:
                tester = int(args.forceJobIndex)  #Leave this argument as a string until it is used so that a zero value can be passed for the index and will still evaluate to true.
            except ValueError:
                raise RuntimeError("ABORTED: Forced job index argument must be an integer so that it can be used as an index.  If you don't understand why this is, you probably should not be messing with this argument.")
            self.forceJobIndex = args.forceJobIndex
        else:
            self.forceJobIndex = False
        self.noCleanup = args.noCleanup
        self.skipAzimuth = True
        self.verbose = args.verbose
        if not args.parallelJobLimit:
            if self.cluster:
                self.maxParallelJobs = clusterDefaultSelectionModeParallelJobLimit
            if self.standAlone:
                self.maxParallelJobs = standAloneDefaultSelectionModeParallelJobLimit
        else:
            try:
                self.maxParallelJobs = int(args.parallelJobLimit)
            except ValueError:
                raise RuntimeError("ABORTED: Parallel job limit must be an integer.")
            else:
                if self.maxParallelJobs < 1:
                    raise RuntimeError("ABORTED: Parallel job limit must be greater than 0")
        self.scratchFolder = args.scratchFolder
        if not self.scratchFolder:
            self.scratchFolder = "" #making sure this is cast to a string and not a NoneType (although that will probably add to a string with no trouble)
        else:
            if not self.scratchFolder[-1] == "/":
                self.scratchFolder = self.scratchFolder + "/"  #make sure that the directory name is passed ending with a slash so we can prepend it directly to our tempDir name
            if not os.path.isdir(self.scratchFolder):
                try:
                    os.mkdir(self.scratchFolder)
                except OSError:
                    raise RuntimeError("ABORTED: Unable to create scratch folder.  Check if directory containing this folder already exists.")
        self.directToCompiler = False
        self.recreateTree = False
        if args.recreateTree:
            if args.directToCompiler:
                raise RuntimeError("You cannot set both the --directToCompiler and --recreateTree arguments.  If you need both, --directToCompiler will run both for you.")
            else:
                self.recreateTree = True
                self.directToCompiler = True
        else:
            if args.directToCompiler:
                self.directToCompiler = True
        if args.treeLevel1:
            try:
                args.treeLevel1 = int(args.treeLevel1)
            except ValueError:
                raise RuntimeError("ABORTED: Invalid tree level 1 size passed as argument (must be an integer).  We got " + str(args.treeLevel1))
            self.treeLevel1 = args.treeLevel1
        else:
            self.treeLevel1 = 5
        if args.treeLevel2:
            try:
                args.treeLevel2 = int(args.treeLevel2)
            except ValueError:
                raise RuntimeError("ABORTED: Invalid tree level 2 size passed as argument (must be an integer).  We got " + str(args.treeLevel2))
            self.treeLevel2 = args.treeLevel2
        else:
            self.treeLevel2 = 5
    
    def setFASTAWorkerArgs(self, args):  #Validate arguments for launching a FASTA indexing worker.  Users are unlikely to be launching this on their own.
        import os
        self.mode = "FASTAWorker"
        self.chromosome = args.chromosome
        self.start = args.start
        self.length = args.length
        if "_" in args.sequence:
            self.sequence = args.sequence
        else:
            raise RuntimeError("ABORTED: Invalid sequence passed to worker. Please include an underscore between the guide and PAM sequences.")
        if os.path.isfile(args.inputfile):
            self.inputfile = args.inputfile
        else:
            raise RuntimeError("ABORTED: FASTA file: " + args.inputfile + " not found.")
        self.genome = args.genome.upper()
        self.tempDir = args.tempDir
        self.workerID = args.workerID
        self.chunkSize = args.chunkSize
        #if os.path.isdir(args.tempDir):
        #    self.tempDir = args.tempDir
        #else:
        #    raise RuntimeError("ABORTED: Unable to detect temporary directory: " + args.tempDir)
        self.skipAzimuth = True
        self.species = args.species
        self.verbose = args.verbose
        try:
            args.treeLevel1 = int(args.treeLevel1)
        except ValueError:
            raise RuntimeError("ABORTED: Invalid tree level 1 size passed as argument (must be an integer).  We got " + str(args.treeLevel1))
        self.treeLevel1 = args.treeLevel1
        try:
            args.treeLevel2 = int(args.treeLevel2)
        except ValueError:
            raise RuntimeError("ABORTED: Invalid tree level 2 size passed as argument (must be an integer).  We got " + str(args.treeLevel2))
        self.treeLevel2 = args.treeLevel2
        
    def setCompilerArgs(self, args):
        import os
        self.mode = "compiler"
        if "_" in args.sequence:
            self.sequence = args.sequence
        else:
            raise RuntimeError("ABORTED: Invalid sequence passed to worker. Please include an underscore between the guide and PAM sequences.")
        self.genome = args.genome.upper()
        self.tempDir = args.tempDir
        self.workerID = args.workerID
        self.skipAzimuth = True
        self.species = args.species
        self.verbose = args.verbose
        if not args.bins:
            raise RuntimeError("Tried to run a bin compiler without specifying bins to compile.  It got bored.")
        self.bins = args.bins
        self.noCleanup = False
        if args.noCleanup:
            self.noCleanup = True

#=================================================Sequence target analysis/hypervisor objects=================================================================================================================================

class TargetSite(object):  #This object holds attributes that describe a potential target site found in the user-defined target sequence.  This can be extended as we get better ways to describe potential target sites.  Only needs a cut site sequence to be initialized, all else can be set later.
    
    def __init__(self, cutSeq, longSeq = False):
        self.longSeq = longSeq
        self.cutSeq = cutSeq  #this value should come in with the underscore already added between guide and pam
        self.matches = {}   #This is designed to hold the dictionary of match/mismatch sites that gets passed from the search function
        for i in range(0, args.mismatchTolerance + 1):
            self.matches[i] = []
        self.azimuthScore = -1  #Default value for this is -1 to indicate no score.
        self.score = False
        self.acceptable = True  #This flag gets set to false if the target has more than one perfect match in the genome
        self.mismatchRisk = False  #This is a function of how well-matched the sites are and if they are in or near an annotated gene
        self.tooManyMatches = False  #This flags any sites with more than 100 * mismatch tolerance potential off-targets.  They're not especially useful for genome editing, generate obscenely huge outputs, and severely degrade performance when annotated.
        
    def calculateSortValue(self):
        self.sortValue = (self.mismatchRisk, -self.azimuthScore)

class TargetFinder(object):  #This object is analogous to a FASTA indexer, except designed to deal with smaller sequences and can be extended to collect larger windows for analysis in azimuth
    
    def __init__(self, target):
        self.target = target  #This is the target sequence passed in.  Should be supplied by the user either on the command line or in a FASTA file
        self.longSeq = False  #If we can generate a 30bp site to pass to azimuth, this is where it gets stored.  Note that we may have to force it a bit if we try to apply their model to other systems
        self.lastGroup = 0
        self.done = False
        self.cutWindow = len(args.sequence) - 1  #subtract out the underscore
        self.start = 0  #start is inclusive
        self.end = self.cutWindow
        self.guide, self.pam = args.sequence.split("_")
        self.pamList = NondegenerateBases(self.pam).permutations()
        self.pamLength = len(self.pam)
        self.matches = []  #initialize an empty list to hold our match sites (which will be TargetSite class instances)
        self.done = False
        self.forceAzimuthPam = False  #This indicates that we have forced the azimuth model for this system by trimming the fixed bases on the end of the pam
        self.forceGuide1 = False  #This indicates that we have forced the azimuth model by making the 5' base we submit into the 5' base on the guide
        self.forceGuide3 = False  #This indicates we have done the same thing with the second base from the 5' end (base 3 if the guide is indexed to 1)
        
    def findMatches(self):  #main running function for this object, actually runs the search, gets azimuth scores if needed, and returns the list of matches
        while not self.done:
            windowSeq = self.target[self.start:self.end]
            revComp = str(ReverseComplement(windowSeq))
            if windowSeq[-self.pamLength:] in self.pamList:
                guide = windowSeq[:-self.pamLength]
                pam = windowSeq[-self.pamLength:]
                if not args.skipAzimuth:
                    longSeq = self.getLongSeq(guide, pam,'+')  #tries to get an extended sequence for azimuth analysis
                self.matches.append(TargetSite(guide + "_" + pam, longSeq))
            if revComp[-self.pamLength:] in self.pamList:
                guide = revComp[:-self.pamLength]
                pam = revComp[-self.pamLength:]
                if not args.skipAzimuth:
                    longSeq = self.getLongSeq(guide, pam,'-')
                self.matches.append(TargetSite(guide + "_" + pam, longSeq))
            self.advance()
        # if not args.skipAzimuth:
        #     self.useAzimuth = True
        # else:
        #     self.useAzimuth = False
        # if self.useAzimuth:
        #     self.azimuthAPIkey = self.getAzimuthAPIkey()
        #     if self.azimuthAPIkey:
        #         self.assignAzimuthScores()
        return self.matches
    
    def advance(self):  #moves the window ahead one character, then checks to see if it has reached the end
        self.start += 1
        self.end += 1
        self.done = self.end > len(self.target)
        
    def getLongSeq(self, guide, pam, strand):  #this method gets an extended sequence for azimuth or other analysis if possible
        pamExtensionLength = 3
        guideExtensionLength = 24 - len(self.guide)
        try:  #we need a try/except block for this because it is possible that the extended sequence will run us off the end of the sequence
            if strand == '+':
                pamEnd = self.end + pamExtensionLength
                guideStart = self.start - guideExtensionLength
                if pamEnd > len(self.target) or guideStart < 0:
                    return False
                pamExtension = self.target[self.end : pamEnd]
                guideExtension = self.target[self.start - guideExtensionLength : self.start]
            if strand == '-':
                pamStart = self.start - pamExtensionLength
                guideEnd = self.end + guideExtensionLength
                if pamStart < 0 or guideEnd > len(self.target):
                    return False
                pamExtension = self.target[self.start - pamExtensionLength : self.start]
                guideExtension = self.target[self.end : self.end + guideExtensionLength]
                pamExtension = str(ReverseComplement(pamExtension))
                guideExtension = str(ReverseComplement(guideExtension))
        except IndexError:  #If we get something near the end of the given sequence where we try to read off the end, we just return False for this value.  Later, this will tell us not try submitting it for analysis.
            return False
        if not len(pam) == 3:  #if we have to force the pam, we will warn the user
            if not self.forceAzimuthPam:
                print("WARNING: Attempting to force conformity of PAM site to the Azimuth model.  Predictions based on forced projections may not be as accurate.")
            self.forceAzimuthPam = True
            pam = pam[:2]
        extendedSeq = guideExtension + guide + pam + pamExtension
        # if not len(guide) == 20 and not args.noForcedBases:
        #     extendedSeq = list(extendedSeq)  #making it a list so that I can change individual characters by their index
        #     if not extendedSeq[4] == guide[0] and not args.noForced1:
        #         extendedSeq[4] = guide[0]
        #         if not self.forceGuide1:
        #             print("Forcing guide base 1 into position 1 for azimuth analysis.  Predictions based on forced projections may not be as accurate.")
        #             self.forceGuide1 = True
        #     if not extendedSeq[6] == guide[2] and not args.noForced3:
        #         extendedSeq[6] = guide[2]
        #         if not self.forceGuide3:
        #             print("Forcing guide base 3 into position 3 for azimuth analysis.  Predictions based on forced projections may not be as accurate.")
        #             self.forceGuide3 = True
        #     extendedSeq = str(extendedSeq)  #return the value back to a string for later submission
        return extendedSeq
    
    def getAzimuth(self, sequence, failedPrevious = False):  #this handles communication with the azure server to get a score.  This can later be replaced if we decide to run a local instance with the source code.
        import urllib.request
        import json
        import time
        import sys #for error catching
        data = {
            "Inputs":{
                "input1":{
                    "ColumnNames":["sequence", "cutsite", "percentpeptide"],
                    "Values":[[sequence, "-1", "-1"]]
                }
            },
                "GlobalParameters": {}
        }
        body = str.encode(json.dumps(data))
        #url = 'https://ussouthcentral.services.azureml.net/workspaces/ee5485c1d9814b8d8c647a89db12d4df/services/c24d128abfaf4832abf1e7ef45db4b54/execute?api-version=2.0&details=true'
        url = 'https://ussouthcentral.services.azureml.net/workspaces/ee5485c1d9814b8d8c647a89db12d4df/services/5c6cbabaef4947b4b7425e934b6f7d6b/execute?api-version=2.0&details=true'  #slower, but only one working for now.  Use for testing
        api_key = self.azimuthAPIkey
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        req = urllib.request.Request(url, body, headers)
        try:
            response = urllib.request.urlopen(req)
            result = response.read().decode('utf-8')
            result = json.loads(result)
            return float(result['Results']['output2']['value']['Values'][0][0])
        except urllib.error.HTTPError as error:
            if error.code == 401:
                print("Unable to use Azimuth due to a possible invalid API key.  Please check on the status of key: " + self.azimuthAPIkey)
            else:
                print("The Azimuth request failed with status code: " + str(error.code))
                print(error.info())
                print(json.loads(error.read().decode('utf-8')))
            self.useAzimuth = False
            return -1  #Remember that -1 is our placeholder value for a failed attempt or no attempt.
        except urllib.error.URLError:
            if not failedPrevious:
                time.sleep(5) #wait 5 seconds before retry
                return self.getAzimuth(sequence, True)
            else:
                print("Unable to reach/find Azimuth server.  Please confirm you are connected to the internet.")
                self.useAzimuth = False
                return -1
        except:  #Allowing this for now while dealing with many possible exceptions due to experimental server and software
            if not failedPrevious:
                time.sleep(5)
                return self.getAzimuth(sequence, True)  #give it another go, because why not...
            else:
                error = sys.exc_info()
                print("Unexpected error in Azimuth scoring:")
                for item in error:
                    print(item)
                return -1
        
    def getAzimuthAPIkey(self):  #this gets the API key from a file
        import os
        if os.path.isfile("azimuth.apikey"):
            file = open("azimuth.apikey", 'r')
            key = file.read()
            file.close()
            key = key.strip()
            return key
        else:
            print("Unable to run azimuth.  Cannot locate API key.  Please save the key the same directory as this program under filename azimuth.apikey.")
            return False
        
    def assignAzimuthScores(self):  #iterate over all our matches and get an azimuth score if there is a saved extended sequence, otherwise it is left as the default -1 value
        for i in range(0,len(self.matches)):
            if self.matches[i].longSeq and self.useAzimuth:
                self.matches[i].azimuthScore = self.getAzimuth(self.matches[i].longSeq)        
                
class TargetSelection(object):  #This is the main running object for the target selection job
    
    def __init__(self):
        printStartUp()
        reportUsage("SELECTION")
        self.targetList = []
        self.indexedGenome = self.selectIndexedGenome() #we will pass this to the search supervisor.  This will save each supervisor a few seconds (probably not significant) and will cover for the potential loss of degeneracy when we pass the sequence to searcher agents 
        print("Checking for target sites")
        self.getTargetSequence()
        if not self.targetList:
            self.targetList = TargetFinder(self.target).findMatches()
        if not self.targetList:
            raise RuntimeError('ABORTED: No suitable target sequences found.')
        if selectionModeTargetLimitPerJob > 0 and len(self.targetList) > selectionModeTargetLimitPerJob and not args.clobber:
            raise RuntimeError("ABORTED: Too many targets in sequence.  Try running a shorter target sequence, a more specific Crispr system, or using clobber mode (argument -9) to override this.")
        print("Found " + str(len(self.targetList)) + " potential target sites.")
        self.createTempDir()
        self.createJobList()
        self.runJobList()
        self.gatherResults()
        self.sortResults()
        if not args.outputToFile:
            self.reportResults()
        else:
            self.reportToFile()
        if not args.noCleanup:
            self.cleanup()
        
    def getTargetSequence(self):
        if args.targetSequence:  #if the user just passed the sequence as an argument...
            target = args.targetSequence.strip()
            target = target.upper()
            for letter in target:
                if letter not in ['A','T','G','C']:  #reject any degenerate sequences passed (probably reasonable to expect the user to have a good sequence for their target)
                    raise RuntimeError("ABORTED: Invalid letters in targeted DNA sequence")
            self.target = target
        elif args.targetFasta:  #if the user referred us to a file for the sequence...
            try:
                targetFasta = open(args.targetFasta, 'r')
            except FileNotFoundError:
                raise RuntimeError("ABORTED: Unable to open the specified FASTA file")
            else:
                target = ""
                line = targetFasta.readline()
                while line:
                    if ">" in line:  #fasta standards state that a line starting with > is identifying a contig and will not contain sequence
                        line = targetFasta.readline()  #readline is probably less efficient than slurping the whole file.  If the user wants to run this on a sequence big enough that this becomes a concern, they are going to have bigger problems in their future.
                        continue
                    else:
                        line = line.replace("\n","")
                        line = line.upper()
                        for letter in line:
                            if letter not in ["A","T","G","C"]:
                                targetFasta.close()
                                raise RuntimeError("ABORTED: Invalid letters in the sequence file")
                        target += line
                        line = targetFasta.readline()
            self.target = target
            targetFasta.close()
        elif args.targetList:  #if the user passed a list of targets...
            try:
                targetListFile = open(args.targetList, 'r')
            except FileNotFoundError:
                raise RuntimeError("ABORTED: Unable to open the specified list of target sites")
            targetList = []
            line = targetListFile.readline()
            while line:
                line = line.strip()
                line = line.replace("\n","")
                line = line.upper()
                for letter in line:
                    if letter not in ['A','T','G','C','_']:
                        raise RuntimeError("ABORTED: Invalid character specified in target list item.")
                if not "_" in line:
                    line = line[:-len(self.pam)] + "_" + line[-len(self.pam):]
                targetList.append(TargetSite(line))  #we can't get an extended sequence from here, so longSeq will remain the default False value and the azimuth score will remain -1
                line = targetListFile.readline()
            self.targetList = targetList
            targetListFile.close()
            print("Using targets from target list file.")
        else:
            raise RuntimeError("ABORTED: No target sequence or list of target sites given/nothing for me to do.")
    
    def selectIndexedGenome(self):  #uses the user-passed guide_pam scheme to pick an indexed genome (or say if we don't have one) that is suitable for this run.  Remember that the sequence is stored in reverse
        import os
        if not os.path.isdir(args.genomeListDirectory):
            raise RuntimeError("ABORTED: No indexed genome directory found.  Please run the indexer to create indexed genomes for searching.")
        seqPam, seqGuide = args.sequence[::-1].split("_")
        self.pam = seqPam[::-1]
        self.guide = seqGuide[::-1]
        directoryContents = os.listdir(args.genomeListDirectory)
        for item in directoryContents:
            if not item[0] == "." and "." in item and "_" in item and "NNN" in item:
                itemSeq, itemGenome, species = item.split(".")
                if itemGenome == args.genome:
                    itemPam, itemGuide = itemSeq.split("_")
                    itemPamList = NondegenerateBases(itemPam).permutations()
                    if (seqPam == itemPam or seqPam in itemPam) and len(seqGuide) <= len(itemGuide):
                        return item
        raise RuntimeError("ABORTED: Please create an indexed genome for this search.  No suitable indexed genome was found.")
        
    def createTempDir(self):  #makes a temporary directory for this run.  Completions will clock out here and results will be reported back to it.
        if args.verbose:
            print ("Creating temporary directory")
        import re
        import os
        import datetime
        successful = False
        while not successful:
            currenttime = datetime.datetime.now()
            currenttime = str(currenttime)
            currenttime = re.sub(r'\W','',currenttime)
            self.tempDir = args.scratchFolder + '.shieldHQ' + currenttime
            if os.path.isdir(self.tempDir):
                continue
            try:
                os.mkdir(self.tempDir)
            except OSError:
                continue
            successful = True
        os.mkdir(self.tempDir + "/completed")
        os.mkdir(self.tempDir + "/progress")
        os.mkdir(self.tempDir + "/result")
        if args.verbose:
            print ("Temporary directory created.")
        return True
        
    def createJobList(self):
        self.jobList = {'queued':[], 'running':[], 'complete':[]}
        for targetSite in self.targetList:
            self.jobList['queued'].append(targetSite)
            
    def runJobList(self):
        import os
        import time
        self.submittedJob = 1
        maxSimultaneousJobs = args.maxParallelJobs // args.parallelJobs
        while self.jobList['queued'] or self.jobList['running']:
            try:
                while self.jobList['queued'] and len(self.jobList['running']) < maxSimultaneousJobs:
                    self.createJobBash(self.jobList['queued'][0])
                    self.submitJob(self.jobList['queued'][0])
                    self.jobList['running'].append(self.jobList['queued'][0])
                    del self.jobList['queued'][0]
                while len(self.jobList['running']) >= maxSimultaneousJobs or len(self.jobList['queued']) == 0:
                    newlyCompleted = []
                    for i in range(0, len(self.jobList['running'])):
                        if os.path.isfile(self.tempDir + "/completed/" + self.jobList['running'][i].cutSeq):
                            newlyCompleted.append(i)
                    newlyCompleted.sort(reverse = True)  #we need to reverse this list so that we remove items in reverse index order.  If we did not do this, and we had two items on the list (say 1 and 3), we could potentially remove item 1 first, and then item 3 becomes item 2, with what started off as item 4 now targeted for deletion and a very high probability that at some point we will run off the end of the list (IndexError)
                    if newlyCompleted:
                        for completedIndex in newlyCompleted:
                            self.jobList['complete'].append(self.jobList['running'][completedIndex])
                            del self.jobList['running'][completedIndex]
                    if not self.jobList['running'] and not self.jobList['queued']:
                        break
                    time.sleep(10)
            except KeyboardInterrupt:
                for key in list(self.jobList.keys()):
                    print(key)
                    for item in self.jobList[key]:
                        print("\t" + item.cutSeq)
                    if yesAnswer("Continue with run?"):
                        continue
                    else:
                        raise RuntimeError("ABORTED: By your command.")
                    
    def createJobBash(self, job):  #Creates a bash file to submit for running the job
        self.bash = self.tempDir + "/" + str(job.cutSeq) + ".sh"
        bashFile = open(self.bash, 'w')
        bashFile.write("#! /bin/bash\n")
        scratchFolder = ""
        clobber = ""
        if args.clobber:
            clobber = " --clobber"
        if args.scratchFolder:
            scratchFolder = " --scratchFolder " + args.scratchFolder
        if args.cluster:
            systemInfo = " --cluster "
        if args.standAlone:
            systemInfo = " --standAlone "
        #bashFile.write("module load python/3.4\n")
        bashFile.write(pythonInterpreterAbsolutePath + " dsNickFury" + currentVersion + ".py --mode search --mismatchTolerance " + str(args.mismatchTolerance) + clobber + " --sequence " + job.cutSeq + " --forceGenome " + self.indexedGenome + " --outputDirectory " + self.tempDir + " --parallelJobs " + str(args.parallelJobs) + " --mismatchTolerance " + str(args.mismatchTolerance) + " --genomeDirectory " + args.genomeListDirectory.replace(" ",'\ ') + " --azimuthSequence " + str(job.longSeq) + scratchFolder + systemInfo + "\n")
        bashFile.close()
    
    def submitJob(self, job):  #submits the bash file to the queue scheduler
        shortName = "ShieldHQ" + str(self.submittedJob)
        self.submittedJob += 1
        if args.cluster:
            import os
            command = "qsub -cwd -V -N " + shortName + " -l h_data=2G,time=23:59:00 -e " + os.getcwd() +  "/schedulerOutput/ -o " + os.getcwd() + "/schedulerOutput/ " + self.bash
            if not args.mock:
                import os
                import time
                submitted = False
                while not submitted:
                    submission = os.system(command)
                    if not submission == 0:
                        print("Job submission unsuccessful, waiting 5 seconds and resubmitting.")
                        time.sleep(5)
                        continue
                    else:
                        submitted = True
            else:
                print ("MOCK SUBMIT: " + command)
        if args.standAlone:
            command = "bash " + self.bash
            if not args.mock:
               import subprocess
               subprocess.Popen(command, shell = True)
            else:
                print ("MOCK SUBMIT: " + command)
            
            
    def gatherResults(self):  #gathers the results from the worker processes (passed via pickle), checks for unacceptable sites (ones that have perfect matches in multiple genomic locations), and calculates mismatch risk numbers
        import pickle
        for i in range(0,len(self.targetList)):
            totalMismatchRisk = 0
            genesCounted = [] #prevent us from counting multiple hits in the same gene twice
            inputFile = open(self.tempDir + "/result/" + self.targetList[i].cutSeq, 'rb')
            result = pickle.load(inputFile)
            inputFile.close()
            self.targetList[i].matches = result['matches']
            self.targetList[i].azimuthScore = result['azimuthScore']
            if len(self.targetList[i].matches[0]) > 1:
                first = self.targetList[i].matches[0][0].gene
                for site in self.targetList[i].matches[0]:
                    if site.gene != first:
                        self.targetList[i].acceptable = False
                        break
            if self.targetList[i].matches[0][0].tooManyOtherSites:
                self.targetList[i].tooManyMatches = self.targetList[i].matches[0][0].tooManyOtherSites
            for j in range(0, args.mismatchTolerance + 1):
                for k in range(0, len(self.targetList[i].matches[j])):
                    risk = self.targetList[i].matches[j][k].calculateMismatchRisk()
                    if not (j == 0 and k == 0) or self.targetList[i].matches[j][k].gene in genesCounted:
                        totalMismatchRisk += risk
                    if self.targetList[i].matches[j][k].gene and self.targetList[i].matches[j][k].gene not in genesCounted:
                        genesCounted.append(self.targetList[i].matches[j][k].gene)
            self.targetList[i].mismatchRisk = totalMismatchRisk
                        
    def sortResults(self):  #Sorts in ascending order by mismatch risk first, then by azimuth score (done by sorting on the negative value of the azimuth score).  If no azimuth was given, the result will be shown last
        import operator
        for i in range(0, len(self.targetList)):
            self.targetList[i].calculateSortValue()        
        self.targetList.sort(key = operator.attrgetter('sortValue'))
        
    def reportResults(self):  #Reports results to STDOUT.  At some point, I should probably offer alternatives to output to a file or even some data object format like JSON
        import sys
        print("Command: " + " ".join(sys.argv))
        unacceptableHeaderPrinted = False
        tooManyMatchHeaderPrinted = False
        for target in self.targetList:
            if target.acceptable and not (target.tooManyMatches and not args.clobber):
                print(target.cutSeq + "\tMismatch Risk: " + str(target.mismatchRisk))
                if int(target.azimuthScore) != -1:
                    print(" "*len(target.cutSeq) + "\tAzimuth Score: " + str(target.azimuthScore))
                else:
                    print(" "*len(target.cutSeq) + "\tAzimuth Score: Cannot determine")
                for count in range(0, args.mismatchTolerance + 1):
                    print("\tMismatches: " + str(count))
                    for site in target.matches[count]:
                        print("\t\t" + str(site))
        for target in self.targetList:
            if not target.acceptable:
                if not unacceptableHeaderPrinted:
                    print("******SITES WITH PERFECT MATCHES ELSEWHERE IN THE GENOME******")
                    unacceptableHeaderPrinted = True
                print(target.cutSeq + "\tMismatch Risk: " + str(target.mismatchRisk))
                for count in range(0, args.mismatchTolerance + 1):
                    print("\tMismatches: " + str(count))
                    for site in target.matches[count]:
                        print("\t\t" + str(site))
        for target in self.targetList:
            if target.tooManyMatches and not args.clobber:
                if not tooManyMatchHeaderPrinted:
                    print("******SITES WITH TOO MANY POTENTIAL MISMATCHES TO DISPLAY******")
                    tooManyMatchHeaderPrinted = True
                print(target.cutSeq + "\tTotal off-target sites: " + str(target.tooManyMatches))
                        
    def reportToFile(self): #Reports results to a file passed as the appropriate argument
        output = open(args.outputToFile,'w')  #We validated that this is not an existing file (or we are willing to clobber it) in the arg checking above
        import sys
        output.write("Command: " + " ".join(sys.argv) + "\n")
        unacceptableHeaderPrinted = False
        tooManyMatchHeaderPrinted = False
        for target in self.targetList:
            if target.acceptable and not (target.tooManyMatches and not args.clobber):
                output.write(target.cutSeq + "\tMismatch Risk: " + str(target.mismatchRisk) + "\n")
                if int(target.azimuthScore) != -1:
                    output.write(" "*len(target.cutSeq) + "\tAzimuth Score: " + str(target.azimuthScore) + "\n")
                else:
                    output.write(" "*len(target.cutSeq) + "\tAzimuth Score: Cannot determine" + "\n")
                for count in range(0, args.mismatchTolerance + 1):
                    output.write("\tMismatches: " + str(count) + "\n")
                    for site in target.matches[count]:
                        output.write("\t\t" + str(site) + "\n")
        for target in self.targetList:
            if not target.acceptable:
                if not unacceptableHeaderPrinted:
                    output.write("******SITES WITH PERFECT MATCHES ELSEWHERE IN THE GENOME******" + "\n")
                    unacceptableHeaderPrinted = True
                output.write(target.cutSeq + "\tMismatch Risk: " + str(target.mismatchRisk) + "\n")
                for count in range(0, args.mismatchTolerance + 1):
                    output.write("\tMismatches: " + str(count) + "\n")
                    for site in target.matches[count]:
                        output.write("\t\t" + str(site) + "\n")
        for target in self.targetList:
            if target.tooManyMatches and not args.clobber:
                if not tooManyMatchHeaderPrinted:
                    output.write("******SITES WITH TOO MANY POTENTIAL MISMATCHES TO DISPLAY******\n")
                    tooManyMatchHeaderPrinted = True
                output.write(target.cutSeq + "\tTotal off-target sites: " + str(target.tooManyMatches) + "\n")
                        
    def cleanup(self):
        import shutil
        shutil.rmtree(self.tempDir)
                        

#=================================================Azimuth analysis object==================================================================================================================

class AzimuthAnalysis(object):

    def __init__(self, sequence, failedPrevious = False):  #this handles communication with the azure server to get a score.  This can later be replaced if we decide to run a local instance with the source code.
        import urllib.request
        import json
        import time
        import sys #for error catching
        self.azimuthAPIkey = self.getAzimuthAPIkey()
        if not self.azimuthAPIkey:
            self.score = -1
        else:
            data = {
                "Inputs":{
                    "input1":{
                        "ColumnNames":["sequence", "cutsite", "percentpeptide"],
                        "Values":[[sequence, "-1", "-1"]]
                    }
                },
                    "GlobalParameters": {}
            }
            body = str.encode(json.dumps(data))
            #url = 'https://ussouthcentral.services.azureml.net/workspaces/ee5485c1d9814b8d8c647a89db12d4df/services/c24d128abfaf4832abf1e7ef45db4b54/execute?api-version=2.0&details=true'
            url = 'https://ussouthcentral.services.azureml.net/workspaces/ee5485c1d9814b8d8c647a89db12d4df/services/5c6cbabaef4947b4b7425e934b6f7d6b/execute?api-version=2.0&details=true'  #slower, but only one working for now.  Use for testing
            api_key = self.azimuthAPIkey
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
            req = urllib.request.Request(url, body, headers)
            try:
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                result = json.loads(result)
                self.score = float(result['Results']['output2']['value']['Values'][0][0])
            except urllib.error.HTTPError as error:
                if error.code == 401:
                    print("Unable to use Azimuth due to a possible invalid API key.  Please check on the status of key: " + self.azimuthAPIkey)
                else:
                    print("The Azimuth request failed with status code: " + str(error.code))
                    print(error.info())
                    print(json.loads(error.read().decode('utf-8')))
                self.useAzimuth = False
                self.score = -1  #Remember that -1 is our placeholder value for a failed attempt or no attempt.
            except urllib.error.URLError:
                if not failedPrevious:
                    time.sleep(5) #wait 5 seconds before retry
                    self.score = AzimuthAnalysis(sequence, True).score
                else:
                    print("Unable to reach/find Azimuth server.  Please confirm you are connected to the internet.")
                    self.useAzimuth = False
                    self.score = -1
            except:  #Allowing this for now while dealing with many possible exceptions due to experimental server and software
                if not failedPrevious:
                    time.sleep(5)
                    self.score = AzimuthAnalysis(sequence, True)  #give it another go, because why not...
                else:
                    error = sys.exc_info()
                    print("Unexpected error in Azimuth scoring:")
                    for item in error:
                        print(item)
                    self.score = -1
        
    def getAzimuthAPIkey(self):  #this gets the API key from a file
        import os
        if os.path.isfile("azimuth.apikey"):
            file = open("azimuth.apikey", 'r')
            key = file.read()
            file.close()
            key = key.strip()
            return key
        else:
            print("Unable to run azimuth.  Cannot locate API key.  Please save the key the same directory as this program under filename azimuth.apikey.")
            return False
        
class OffTargetAzimuth:

    def __init__(self, extendedSeq, mismatchSites):
        self.extendedSeq = extendedSeq
        self.mismatchSites = mismatchSites
        self.score = self.calculateScore()
        
    def calculateScore(self):
        return -1
    
#=================================================Reverse Complement and other sequence manipulation.  Possibly move to its own module later?===========================================Complete==============================

class ReverseComplement(object):  #declares an object class.  We capitalize the first letter (unlike variables that should start with lowercase) to avoid potential collisions with variable names
    
    def __init__(self, sequence, reverse = True, case = 'original'):
        case = case.lower()
        if not case in ['upper','lower','original']:
            raise ValueError('Case option must be set to upper, lower, or original.')
        self.case = case
        if reverse:  #we defined an optional argument "reverse" to be true.  We did this because we assume people will often want the reverse complement.  They have to specify reverse = False if they don't.
            self.inputSeq = sequence[::-1]  #Neat trick in Python to reverse the order of an iterable (string, list, etc).  Indexing goes [inclusive start:non-inclusive end:step].  A step of -1 tells it to start from the end and step backwards 1 element at a time.  This seems to run slightly more efficiently than iterating in reverse.
        else: #if the user wants a non-reverse complement
            self.inputSeq = sequence  #we store the value without reversing.  The self.[name] means that this value will be variable that can be called from anywhere within this instance of the object AND from outside the object by calling [instance].[name].  A variable that is tied to a function like this one is called an attribute. 
        if self.case == 'upper':  #now that case is being handled by the dictionary itself, we just need to change the original sequence if necessary
            self.inputSeq = self.inputSeq.upper()  
        elif self.case == 'lower':
            self.inputSeq == self.inputSeq.lower()
        self.complementTable = self.createComplementTable()  #this is defining an attribute of the object (complementTable) by calling the createComplementTable method.  Of interest, since the table is just returned by the function, a program could call the table for its own use by calling [instance].createComplementTable()
        self.complementLists = self.createComplementLists()  #same as above, but this one gets back all non-degenerate possibilities
        self.checkInput() #always good to validate inputs.  This will handle any invalid letters entered.  It will still raise an exception, but will be more specific in the error reporting.
        self.outputSeqString = self.createOutputString()  #Creates the outputString (the reverse complement).  Because this is called in the __init__ initializer method, we automatically calculate the reverse complement (why this is convenient will be covered in the __str__ overload method)
        self.outputList = False  #this initializes an attribute to False.  Why we want to do this will be covered as part of a later method.
        
        
    def __str__(self):  #this is overloading the existing str(object) method.  Normally, if I tried to print(thisObject), I would either get an exception or a bunch of rubbish back.
        return self.outputSeqString  #Instead, this says that if I try to print the entire object or turn it to a string, what I REALLY want to get back is the outputSeqString I created in the initialization function
        
    def createComplementTable(self):  #Will this work faster is we just define the values by case in our dictionary?
        complementTable =  {"A":"T",
                            "T":"A",
                            "G":"C",
                            "C":"G",
                            "Y":"R",
                            "R":"Y",
                            "S":"S",
                            "W":"W",
                            "K":"M",
                            "M":"K",
                            "B":"V",
                            "D":"H",
                            "H":"D",
                            "V":"B",
                            "N":"N",
                            "a":"t",
                            "t":"a",
                            "g":"c",
                            "c":"g",
                            "y":"r",
                            "r":"y",
                            "s":"s",
                            "w":"w",
                            "k":"m",
                            "m":"k",
                            "b":"v",
                            "d":"h",
                            "h":"d",
                            "v":"b",
                            "n":"n"}
        return complementTable
    
    def createComplementLists(self):  
        complementLists =  {"A":["T"],
                            "T":["A"],
                            "G":["C"],
                            "C":["G"],
                            "Y":["G","A"],
                            "R":["T","C"],
                            "S":["C","G"],
                            "W":["T","A"],
                            "K":["A","C"],
                            "M":["T","G"],
                            "B":["G","C","A"],
                            "D":["T","C","A"],
                            "H":["T","G","A"],
                            "V":["T","G","C"],
                            "N":["T","G","C","A"],
                            "a":["t"],
                            "t":["a"],
                            "g":["c"],
                            "c":["g"],
                            "y":["g","a"],
                            "r":["t","c"],
                            "s":["c","g"],
                            "w":["t","a"],
                            "k":["a","c"],
                            "m":["t","g"],
                            "b":["g","c","a"],
                            "d":["t","c","a"],
                            "h":["t","g","a"],
                            "v":["t","g","c"],
                            "n":["t","g","c","a"]}
        return complementLists
    
    def checkInput(self):  #Input validation
        for letter in self.inputSeq:   #iterate over the input letters
            if letter not in list(self.complementLists.keys()):  #get a list of keys from the complement table, and if a letter is in the input sequence that is not a key in the table
                raise ValueError(letter + " in " + self.inputSeq + " is not a valid DNA base.")  #Raise an exception that explicitly lists what the problem was and where.  Help the user help themselves.
            
    def createOutputString(self):  #This simple function creates our most basic output: a reverse complement string containing any degeneracy that may have been in the original
        output = ""  #intialize an empty string
        for letter in self.inputSeq:  #iterate over our input string (which, if appropriate was reversed in the initializer)
            output += self.complementTable[letter]  #add on the proper complementary base to the growing output string
        return output  #return the output
    
    def permutations(self):  #turn a sequence containing degenerate bases into a list of all possible non-degenerate sequences
        import itertools  #this library contains the code we need to create all possible permutations and probably does so more efficiently than our own code would
        if self.outputList:  #if we already have the value we are trying to create here (and we can tell because it is no longer the False value we initialized it to)
            return self.outputList  #we avoid repeating previous work and just output what we already have stored.  As will be shown in the test code below, the work required for this function can grow exponentially.  We only want to run it if it is requested AND we only ever want to run it the one time.
        letterList = []  #initialize an empty list to store a list of lists, where the outer list will correspond to the letters of the sequence and each inner list will represent all possibilities for that letter
        for letter in self.inputSeq:  #iterate over the input sequence
            letterList.append(self.complementLists[letter])  #add a list of possible bases to a growing list of possible bases at each position
        self.outputList = [''.join(letter) for letter in itertools.product(*letterList)]  #use the itertools module's product function to create the permutations (if this line seems strange to you, try looking up list comprehension in python and positional arguments, commonly called *args)
        return self.outputList #return the (potentially quite large) list
    
class RNAReverseComplement(ReverseComplement):  #declare another class called RNAReverseComplement as an extension of the ReverseComplement base class
    
    def createComplementTable(self):  #Will this work faster is we just define the values by case in our dictionary?
        complementTable =  {"A":"U",
                            "T":"A",
                            "U":"A",
                            "G":"C",
                            "C":"G",
                            "Y":"R",
                            "R":"Y",
                            "S":"S",
                            "W":"W",
                            "K":"M",
                            "M":"K",
                            "B":"V",
                            "D":"H",
                            "H":"D",
                            "V":"B",
                            "N":"N",
                            "a":"u",
                            "t":"a",
                            "u":"a",
                            "g":"c",
                            "c":"g",
                            "y":"r",
                            "r":"y",
                            "s":"s",
                            "w":"w",
                            "k":"m",
                            "m":"k",
                            "b":"v",
                            "d":"h",
                            "h":"d",
                            "v":"b",
                            "n":"n"}
        return complementTable
    
    def createComplementLists(self):  
        complementLists =  {"A":["U"],
                            "T":["A"],
                            "U":["A"],
                            "G":["C"],
                            "C":["G"],
                            "Y":["G","A"],
                            "R":["U","C"],
                            "S":["C","G"],
                            "W":["U","A"],
                            "K":["A","C"],
                            "M":["U","G"],
                            "B":["G","C","A"],
                            "D":["U","C","A"],
                            "H":["U","G","A"],
                            "V":["U","G","C"],
                            "N":["U","G","C","A"],
                            "a":["u"],
                            "t":["a"],
                            "u":["a"],
                            "g":["c"],
                            "c":["g"],
                            "y":["g","a"],
                            "r":["u","c"],
                            "s":["c","g"],
                            "w":["u","a"],
                            "k":["a","c"],
                            "m":["u","g"],
                            "b":["g","c","a"],
                            "d":["u","c","a"],
                            "h":["u","g","a"],
                            "v":["u","g","c"],
                            "n":["u","g","c","a"]}
        return complementLists

class InosineReverseComplement(ReverseComplement):
    
    def createComplementTable(self):  #Will this work faster is we just define the values by case in our dictionary?
        complementTable =  {"A":"T",
                            "T":"A",
                            "G":"C",
                            "C":"G",
                            "Y":"R",
                            "R":"Y",
                            "S":"S",
                            "W":"W",
                            "K":"M",
                            "M":"K",
                            "B":"V",
                            "D":"H",
                            "H":"D",
                            "V":"B",
                            "N":"N",
                            "I":"N",
                            "a":"t",
                            "t":"a",
                            "g":"c",
                            "c":"g",
                            "y":"r",
                            "r":"y",
                            "s":"s",
                            "w":"w",
                            "k":"m",
                            "m":"k",
                            "b":"v",
                            "d":"h",
                            "h":"d",
                            "v":"b",
                            "n":"n",
                            "i":"n"}
        return complementTable
    
    def createComplementLists(self):  
        complementLists =  {"A":["T","I"],
                            "T":["A","I"],
                            "G":["C","I"],
                            "C":["G","I"],
                            "Y":["G","A","I"],
                            "R":["T","C","I"],
                            "S":["C","G","I"],
                            "W":["T","A","I"],
                            "K":["A","C","I"],
                            "M":["T","G","I"],
                            "B":["G","C","A","I"],
                            "D":["T","C","A","I"],
                            "H":["T","G","A","I"],
                            "V":["T","G","C","I"],
                            "N":["T","G","C","A","I"],
                            "I":["A","T","G","C","I"],
                            "a":["t","i"],
                            "t":["a","i"],
                            "g":["c","i"],
                            "c":["g","i"],
                            "y":["g","a","i"],
                            "r":["t","c","i"],
                            "s":["c","g","i"],
                            "w":["t","a","i"],
                            "k":["a","c","i"],
                            "m":["t","g","i"],
                            "b":["g","c","a","i"],
                            "d":["t","c","a","i"],
                            "h":["t","g","a","i"],
                            "v":["t","g","c","i"],
                            "n":["t","g","c","a","i"],
                            "i":["a","t","g","c","i"]}
        return complementLists
       
class NondegenerateBases(ReverseComplement):
    
    def __init__(self, sequence, case = 'original'):
        case = case.lower()
        if not case in ['upper','lower','original']:
            raise ValueError('Case option must be set to upper, lower, or original.')
        self.case = case
        self.inputSeq = sequence  #we store the value without reversing.  The self.[name] means that this value will be variable that can be called from anywhere within this instance of the object AND from outside the object by calling [instance].[name].  A variable that is tied to a function like this one is called an attribute. 
        if self.case == 'upper':  #now that case is being handled by the dictionary itself, we just need to change the original sequence if necessary
            self.inputSeq = self.inputSeq.upper()  
        elif self.case == 'lower':
            self.inputSeq == self.inputSeq.lower()
        self.complementLists = self.createComplementLists()  #same as above, but this one gets back all non-degenerate possibilities
        self.checkInput() #always good to validate inputs.  This will handle any invalid letters entered.  It will still raise an exception, but will be more specific in the error reporting.
        self.outputList = self.permutations()  #this initializes an attribute to False.  Why we want to do this will be covered as part of a later method.
        
    def __str__(self, separator = "\n"):
        return separator.join(self.outputList)
    
    def __iter__(self):
        for i in range(0,len(self.outputList)):
            yield self.outputList[i]
            
    def __getitem__(self, index):
        return self.outputList[index]
    
    def __len__(self):
        return len(self.outputList)
        
    def createComplementLists(self):  
        complementLists =  {"A":["A"],
                            "T":["T"],
                            "G":["G"],
                            "C":["C"],
                            "Y":["C","T"],
                            "R":["A","G"],
                            "S":["G","C"],
                            "W":["A","T"],
                            "K":["T","G"],
                            "M":["A","C"],
                            "B":["C","G","T"],
                            "D":["A","G","T"],
                            "H":["A","C","T"],
                            "V":["A","C","G"],
                            "N":["A","C","G","T"],
                            "a":["a"],
                            "t":["t"],
                            "g":["g"],
                            "c":["c"],
                            "y":["c","t"],
                            "r":["a","g"],
                            "s":["g","c"],
                            "w":["a","t"],
                            "k":["t","g"],
                            "m":["a","c"],
                            "b":["c","g","t"],
                            "d":["a","g","t"],
                            "h":["a","c","t"],
                            "v":["a","c","g"],
                            "n":["a","c","g","t"]}
        return complementLists   

    def permutations(self):  #turn a sequence containing degenerate bases into a list of all possible non-degenerate sequences
        import itertools  #this library contains the code we need to create all possible permutations and probably does so more efficiently than our own code would
        try: #This try/except block is another way of determining if we have already calculated this list out.  I do not know which method is more efficient, but the difference is probably negligible in this context
            if self.outputList:  #if we already have the value we are trying to create here (and we can tell because it is no longer the False value we initialized it to)
                return self.outputList  #we avoid repeating previous work and just output what we already have stored.  As will be shown in the test code below, the work required for this function can grow exponentially.  We only want to run it if it is requested AND we only ever want to run it the one time.
        except (AttributeError, NameError):
            letterList = []  #initialize an empty list to store a list of lists, where the outer list will correspond to the letters of the sequence and each inner list will represent all possibilities for that letter
            for letter in self.inputSeq:  #iterate over the input sequence
                letterList.append(self.complementLists[letter])  #add a list of possible bases to a growing list of possible bases at each position
            self.outputList = [''.join(letter) for letter in itertools.product(*letterList)]  #use the itertools module's product function to create the permutations (if this line seems strange to you, try looking up list comprehension in python and positional arguments, commonly called *args)
            return self.outputList #return the (potentially quite large) list

#================================================Search Objects to find potential targets in an indexed genome based on guide RNA sequence=======================================================
    
class MatchSite(object):  #Note that this is also used when we unpickle this object from the hypervisor (target selection) function
    def __init__(self, chrom, begin, end, matchSeq, score, strand, colorScheme, mismatches, extendedMatchSeq, mismatchSites):
        self.chrom = chrom
        self.begin = begin
        self.end = end
        self.matchSeq = matchSeq
        self.score = score
        self.strand = strand
        self.colorScheme = colorScheme
        self.extendedMatchSeq = extendedMatchSeq
        self.mismatchSites = mismatchSites
        self.thickStart = ""
        self.thickEnd = ""
        self.azimuth = False
        self.delimiter = "\t"
        try:  #this deals with sorting chromosomes that can be identified by numbers or X, Y, and M and being able to sort by number and then by letter
            sortChr = int(self.chrom)
            sortChr = str(sortChr).zfill(2)
        except ValueError:
            sortChr = self.chrom
        self.sortValue = (sortChr,int(begin))  #This value helps sort by chromosome/location
        self.mismatchRisk = False
        self.mismatches = mismatches
        self.gene = False
        self.tooManyOtherSites = False
        if "X" in extendedMatchSeq.upper():
            self.mismatchAzimuth = -1
        else:
            self.mismatchAzimuth = self.calculateOffTargetAzimuth()
        
    def calculateMismatchRisk(self):  #
        if self.mismatchRisk:
            return self.mismatchRisk
        else:
            self.mismatchRisk = args.mismatchTolerance + 2 - self.mismatches
            if self.gene:
                self.mismatchRisk = self.mismatchRisk ** 2
            return self.mismatchRisk
        
    def __str__(self):  #quick way to output the info on the match site
        if not self.gene:
            printGene = "NoGene"
        else:
            printGene = self.gene.split("[")[0].strip() #info on source of gene annotation follows the open bracket.  This just takes the part before it.
        if self.mismatchAzimuth == -1:
            printOffTargetAzimuth = "Not Determined"
        else:
            printOffTargetAzimuth = str(self.mismatchAzimuth)
        printOffTargetAzimuth
        printName = "/".join([printGene, self.matchSeq, printOffTargetAzimuth])
        returnThings = [self.chrom, self.begin, self.end, printName, self.score, self.strand, self.thickStart, self.thickEnd, self.colorScheme]
        return self.delimiter.join(returnThings)
    
    def calculateOffTargetAzimuth(self):
        return OffTargetAzimuth(self.extendedMatchSeq, self.mismatchSites).score

class SearchSupervisor(object):
    
    def __init__(self):
        if not args.forceGenome:
            printStartUp()
            reportUsage("SEARCH") 
            genomeDirectory = self.selectIndexedGenome()
        else:
            genomeDirectory = args.forceGenome
            pam, sequence, self.species = genomeDirectory.split(".")
        self.genomeDirectory = args.genomeListDirectory + genomeDirectory
        self.createTempDir()
        print("Creating job list")
        self.createJobList()
        print("Assigning jobs")
        self.assignJobs()
        print("Calculating Azimuth Score")
        self.azimuthScore = -1
        if args.azimuthSequence:  #Do this after finishing local job, but before monitoring, since we will still be waiting on them
            self.azimuthScore = AzimuthAnalysis(args.azimuthSequence).score
        print("Monitoring")
        self.monitorJobs()
        print("Gathering")
        self.gatherJobs()
        print("Sorting")
        self.sortResults()
        print("Annotating")
        self.annotateResults()
        print("Reporting")
        if not args.outputDirectory:
            self.reportResults()
        else:
            self.reportToDirectory()
        if not args.noCleanup:
            self.cleanup()
  
    def selectIndexedGenome(self):
        import os
        if not os.path.isdir(args.genomeListDirectory):
            raise RuntimeError("ABORTED: No indexed genome directory found.  Please run the indexer to create indexed genomes for searching.")
        seqPam, seqGuide = args.sequence[::-1].split("_")
        directoryContents = os.listdir(args.genomeListDirectory)
        for item in directoryContents:
            if not item[0] == "." and "." in item and "_" in item and "NNN" in item:
                itemSeq, itemGenome, itemSpecies = item.split(".")
                if itemGenome == args.genome:
                    itemPam, itemGuide = itemSeq.split("_")
                    itemPamList = NondegenerateBases(itemPam).permutations()
                    if (seqPam.upper() == itemPam.upper() or seqPam.upper() in itemPamList) and len(seqGuide) <= len(itemGuide):
                        self.species = itemSpecies.strip().lower()
                        return item
        raise RuntimeError("ABORTED: Please create an indexed genome for this search.  No suitable indexed genome was found.")
                
    def createTempDir(self):
        if args.verbose:
            print ("Creating temporary directory")
        import re
        import os
        import datetime
        successful = False
        while not successful:
            currenttime = datetime.datetime.now()
            currenttime = str(currenttime)
            currenttime = re.sub(r'\W','',currenttime)
            self.tempDir = args.scratchFolder + '.dsNickFuryMission' + currenttime
            if os.path.isdir(self.tempDir):
                continue
            try:
                os.mkdir(self.tempDir)
            except OSError:
                continue
            successful = True
        os.mkdir(self.tempDir + "/completed")
        os.mkdir(self.tempDir + "/progress")
        os.mkdir(self.tempDir + "/result")
        if args.verbose:
            print ("Temporary directory created.")
        return True
    
    def getRefFiles(self):  #this is the old way before a tree structure.  Replace with findTargetsInTree
        import os
        dirContents = os.listdir(self.genomeDirectory)
        targets = []
        for item in dirContents:
            if os.path.isfile(self.genomeDirectory + "/" + item) and "c" in item:
                targets.append(item)
        return targets
    
    def findTargetsInTree(self):
        import pickle
        import os
        targetFiles = []  #initiate an empty list to store our good targetfiles
        try:
            treeFile = open(self.genomeDirectory + os.sep + "tree.pkl", "rb")
        except FileNotFoundError:
            raise RuntimeError("The tree structure file for this genome was not found.  Please run the indexer with the recreate tree option to correct this problem.")
        print("Loading tree structure.")
        tree = pickle.load(treeFile)
        treeFile.close()
        level1 = list(tree.keys())
        seed1Length = len(level1[0])
        seed2Length = len(tree[level1[0]][0][0])  #uses the first key value (we don't care which, since they should be uniform length) to get the the first value of its level2, and we take the first element from that tupple, since the second would be the size of the file
        pam, guide = args.sequence[::-1].split("_")  #this will reverse it and get our guide seq
        seed1 = guide[:seed1Length]
        seed2 = guide[seed1Length:seed1Length + seed2Length]
        qualifiedBins = 0
        testedBins = 0
        print(str(qualifiedBins) + " of " + str(testedBins) + " target groups qualified.", end = "\r")
        for bigBin in level1:
            seed1Mismatches = self.countMismatches(bigBin, seed1)
            if seed1Mismatches > int(args.mismatchTolerance):
                testedBins += len(tree[bigBin])
                print(str(qualifiedBins) + " of " + str(testedBins) + " target groups qualified.", end = "\r")
                continue  #this entire bigBin is disqualified
            else:
                for smallBin in tree[bigBin]:
                    testedBins += 1
                    seed2Mismatches = self.countMismatches(smallBin[0], seed2)
                    if seed1Mismatches + seed2Mismatches > int(args.mismatchTolerance):
                        print(str(qualifiedBins) + " of " + str(testedBins) + " target groups qualified.", end = "\r")
                        continue #this smallbin is disqualified
                    else:
                        qualifiedBins += 1
                        targetFiles.append((bigBin + ".targetbin" + os.sep + smallBin[0] + ".targets:" + str(seed1Mismatches + seed2Mismatches) + ":" + str(seed1Length + seed2Length), smallBin[1])) #adds on a tupple where the first element is the path to the file containing the valid targets and the second element is the size of the file.  The size will be important later for load balancing purposes.  The file path will also have two integers attached to it separated by colons; these values will be the number of mismatches already seen and the index of where the matching should start again (so combined seeds of length 10 has already covered 0:9 and should start at index 10)
                        print(str(qualifiedBins) + " of " + str(testedBins) + " target groups qualified.", end = "\r")
        print("\nAll target groups tested!")
        return targetFiles
        
    def countMismatches(self, seq1, seq2, caseSensitive = False):
        seqLength = len(seq1)
        if not caseSensitive:
            seq1 = seq1.upper()
            seq2 = seq2.upper()  #just to be sure
        if len(seq2) != seqLength:
            raise RuntimeError("Two different sequence lengths passed: " + seq1 + " and " + seq2)
        mismatches = 0
        for i in range(0,seqLength):
            if seq1[i] != seq2[i]:
                mismatches += 1
        return mismatches        
        
    def createJobList(self):
        if args.verbose:
            print ("Creating a list of jobs.")
        unorderedJobList = []
        jobLoad = []  #This will monitor the load on each individual job and allow better load balancing
        qualifiedBins = self.findTargetsInTree()
        if not args.parallelJobs or args.parallelJobs > len(qualifiedBins):
            parallelSearches = len(qualifiedBins)
        for i in range(0,args.parallelJobs):
            unorderedJobList.append([])
            jobLoad.append(0)  #this will be increased each time we add a file to the job by the size of the file (should be proportional to the lines in the file).  It will match with the job list by index
        for qualifiedBin in qualifiedBins:
            currentSmallestJobIndex = jobLoad.index(min(jobLoad))
            unorderedJobList[currentSmallestJobIndex].append(qualifiedBin[0]) #append the bin to the least-loaded job (this will just pick one if there is a tie, like at the very beginning)
            jobLoad[currentSmallestJobIndex] += qualifiedBin[1]
        self.jobList = []
        for i in range(0, len(unorderedJobList)):  #the point of this next step is to sort the job list from largest to smallest job.  This guarantees that the largest job will be run off the manager process (so we already have that node) and the rest of the jobs will be submitted largest first in order to start them first.
            largest = jobLoad.index(max(jobLoad))
            self.jobList.append(unorderedJobList[largest])
            jobLoad[largest] = 0  #zero out the size of the job we just added.  Now the next largest will be the largest on the subsequent iteration
        if not len(self.jobList) == len(unorderedJobList):
            raise RuntimeError("Ordered and unordered joblists are different lengths.  This should not happen.")       
        return True
    
    def assignJobs(self):
        import pickle  #pickle has security issues, know about them before using it
        for i in range(1,len(self.jobList)):  #we index to 1 here because job 0 (which will have an equal or greater number of searches) will be reserved for the supervisor instance
            outputFile = open(self.tempDir + "/mission" + str(i), "wb")
            pickle.dump(self.jobList[i], outputFile)  #this could also be dumped to a network socket
            outputFile.close()
            self.createJobBash(i)
            self.submitJob(i)
        print("Submitted all jobs.  Beginning worker job on this node.")
        args.workerID = "0"
        args.inputDirectory = self.genomeDirectory
        myJob = WorkerJob(self.jobList[0])
        self.matches = myJob.reportResult()  #this will both make this instance work AND function as a bit of a timer
        print("Worker job on this node complete.")
        
    def createJobBash(self,jobID):
        self.bash = self.tempDir + "/" + str(jobID) + ".sh"
        bashFile = open(self.bash, 'w')
        bashFile.write("#! /bin/bash\n")
        #bashFile.write("module load python/3.4\n")
        bashFile.write(pythonInterpreterAbsolutePath + " dsNickFury" + currentVersion + ".py --mode worker --workerID " + str(jobID) + " --mismatchTolerance " + str(args.mismatchTolerance) + " --sequence " + args.sequence + " --inputDirectory " + self.genomeDirectory + " --tempDir " + self.tempDir + " --genomeDirectory " + args.genomeListDirectory.replace(" ",'\ ') + "\n")
        bashFile.close()
    
    def submitJob(self, jobID):
        shortName = "NickFury" + str(jobID)
        if args.cluster:
            import os
            command = "qsub -cwd -V -N " + shortName + " -l h_data=2G,time=0:59:00 -e " + os.getcwd() +  "/schedulerOutput/ -o " + os.getcwd() + "/schedulerOutput/ " + self.bash
            if not args.mock:
                import os
                import time
                submitted = False
                while not submitted:
                    submission = os.system(command)
                    if not submission == 0:
                        print("Attempted submission failed, retrying in 5 seconds")
                        time.sleep(5)
                    else:
                        submitted = True
            else:
                print ("MOCK SUBMIT: " + command)
        if args.standAlone:
            command = "bash " + self.bash
            if not args.mock:
                import subprocess
                subprocess.Popen(command, shell = True)
            else:
                print ("MOCK SUBMIT: " + command)
            
    def monitorJobs(self):
        import time
        import os
        allDone = False
        if args.parallelJobs == 1:
            return True
        while not allDone:
            for i in range(1,len(self.jobList)):
                if args.verbose:
                    print("Checking for " + str(i))
                if not os.path.isfile(self.tempDir + "/completed/" + str(i) + ".done"):
                    if args.verbose:
                        print("it was not found")
                    allDone = False
                    time.sleep(10)
                    break
                else:
                    if args.verbose:
                        print("it was found")
                    allDone = True
        return True
    
    def gatherJobs(self):
        import pickle
        for i in range(1,len(self.jobList)):
            inputFile = open(self.tempDir + "/result/" + str(i), "rb")
            gatheredPart = pickle.load(inputFile)
            inputFile.close()
            for j in range(0,args.mismatchTolerance + 1):
                self.matches[j] += gatheredPart[j]
                
    def sortResults(self):
        import operator
        if args.verbose:
            print("Starting to sort.")
        for i in range(0,args.mismatchTolerance + 1):
            if args.verbose:
                print("Sorting group " + str(i))
            self.matches[i].sort(key = operator.attrgetter('sortValue'))
    
    def getAnnotation(self, site, expand = 0, failedPrevious = False):
        import urllib.request
        import time
        import json
        begin = int(site.begin) - expand
        end = int(site.end) + expand
        urlBase = 'http://rest.ensembl.org/overlap/region/' + self.species + '/'
        urlLocus = str(site.chrom) + ":" + str(begin) + "-" + str(end)
        urlArguments = "?feature=gene;content-type=application/json"
        fullURL = urlBase + urlLocus + urlArguments
        try:
            ensembl = urllib.request.urlopen(fullURL)
            ensembl = ensembl.read().decode('utf-8')
            ensembl = json.loads(ensembl)
        except urllib.error.HTTPError as error:
            if not failedPrevious:
                time.sleep(5)
                return self.getAnnotation(site, expand, True)
            else:
                print("The ensembl annotation request failed with status code: " + str(error.code))
                print(error.info())
                print(error.read().decode('utf-8'))
                return "Unable to get annotation.  Error code: " + str(error.code) + " FullURL = " + fullURL
        except urllib.error.URLError:
            if not failedPrevious:
                time.sleep(5)
                return self.getAnnotation(site, expand, True)
            else:
                print("Unable to reach/find ensembl server.  Please confirm you are connected to the internet.")
                return "Unable to contact ensembl. (URL/network error)"
        except http.client.HTTPException as error:
            if not failedPrevious:
                time.sleep(5)
                return self.getAnnotation(site, expand, True)
            else:
                print("Got bad status line trying to pull up " + fullURL)
                print("Response: " + error.read().decode('utf-8'))
                return "Unable to get annotation due to BadStatusCode error.  Matching " + args.sequence
        gene = False
        for item in ensembl:
            if item['description']:  #check if a gene is listed for the site, if not, check the next one.  If we get to the end and find no gene, then we return no gene.  Sometimes ensembl returns a result with no gene listed, followed by a second annotation listing the gene.
                gene = item['description']
        return gene

    def annotateResults(self):
        totalMatches = 0  #First we check to determine if we have a reasonable number of sites.  If it is too high, we won't bother annotating gene info, as that will seriously degrade performance for a site nobody would want to use.
        for key in list(self.matches.keys()):  #Seriously, I learned this one the hard way, having unintentionally found a CRISPR target with about 7000 potential off-targets
            totalMatches += len(self.matches[key])  #It took over an hour just to make all the Ensembl server calls.  It was brutal and kept timing out the job for a site nobody would ever use.
        if totalMatches > args.mismatchTolerance * 100 and not args.clobber:
            for key in list(self.matches.keys()):
                for i in range(0,len(self.matches[key])):
                    self.matches[key][i].tooManyOtherSites = totalMatches
            return True #Get us out of here before we bother annotating this terrible, terrible site.  Otherwise we'll be at it forever.
        for key in list(self.matches.keys()):
            for i in range(0,len(self.matches[key])):
                self.matches[key][i].gene = self.getAnnotation(self.matches[key][i])
        for key in list(self.matches.keys()):
            for i in range(0,len(self.matches[key])):
                if not self.matches[key][i].gene:
                    self.matches[key][i].gene = self.getAnnotation(self.matches[key][i], args.annotationExpansion // 10)
        for key in list(self.matches.keys()):
            for i in range(0,len(self.matches[key])):
                if not self.matches[key][i].gene:
                    self.matches[key][i].gene = self.getAnnotation(self.matches[key][i], args.annotationExpansion)
            
    def reportResults(self):
        for i in range(0,args.mismatchTolerance + 1):
            print("Mismatches: " + str(i))
            for line in self.matches[i]:
                print("\t" + str(line))

    def reportToDirectory(self):
        import pickle
        print("Starting reporter function.")
        print("Reporting to directory.")
        outputData = {}
        outputData['sequence'] = args.sequence
        outputData['matches'] = self.matches
        outputData['azimuthScore'] = self.azimuthScore
        print(self.matches)
        print(args.sequence)
        print("Starting pickle")
        outputFile = open(args.outputDirectory + "/result/" + args.sequence, 'wb')
        pickle.dump(outputData, outputFile)
        outputFile.close()
        print("Pickle done.")
        clockOut = open(args.outputDirectory + "/completed/" + args.sequence, 'w')
        clockOut.close()
        print("Clocked out.")
                
    def cleanup(self):
        import shutil
        shutil.rmtree(self.tempDir)
                
class WorkerJob(object):
    
    def __init__(self, fileList = False):
        if not fileList:
            self.fileList = self.getJobList()
        else:
            self.fileList = fileList
        self.matchTable = self.createMatchTable()
        self.pam, self.guide = args.sequence[::-1].split("_")
        self.colorScheme = self.createColorScheme()
        print("Matching")
        self.checkAllSequences()
        print("Worker job reporting results")
        self.reportResult()

    def createMatchTable(self):
        matchTable = {}
        for i in range(0,args.mismatchTolerance+1):
            matchTable[i] = []
        return matchTable
        
    def getJobList(self):
        import pickle
        inputFile = open(args.tempDir + "/mission" + args.workerID, "rb")
        jobList = pickle.load(inputFile)
        inputFile.close()
        return jobList
        
    def createColorScheme(self):
        colorScheme = []
        if args.mismatchTolerance > 7:
            increments = 8
        elif args.mismatchTolerance == 0:
            return ["0,0,0"]
        else:
            increments = args.mismatchTolerance
            step = 255//increments
        for i in range(0,increments + 1):
            if i < 8:
                red = 255 - (step*i)
                green = 0
                blue = 0 + step*i
                colorScheme.append(str(red) + "," + str(green) + "," + str(blue))
            else:
                colorScheme.append(str(red) + ",0," + str(blue))
        return colorScheme
        
    def checkAllSequences(self):
        progress = 0
        for fileData in self.fileList:
            fileName, binMismatches, startIndex = fileData.split(":")  #the last two values will come in as strings, but need to be used as ints
            binMismatches = int(binMismatches)
            startIndex = int(startIndex)
            file = open(args.inputDirectory + "/" + fileName, 'r')
            wholeFile = file.read()
            file.close()
            wholeFile = wholeFile.split("\n")
            for line in wholeFile:
                if line:
                    mismatches = binMismatches #initialize this counter to however many mismatches we got during our tree search
                    if line.count("\t") == 5:
                        chrom, begin, end, extendedSeq, score, strand = line.split("\t")
                    elif line.count("\t") == 4:
                        chrom, begin, end, extendedSeq, strand = line.split("\t")
                    else:
                        raise RuntimeError("Got an inappropriate number of tabs on this line: " + line)
                    refSeq, beforeStart, afterPam = extendedSeq.split("/")
                    pam, guide = refSeq.split("_")
                    for i in range(startIndex,len(self.guide)):
                        try:
                            if guide[i] != self.guide[i]:
                                mismatches += 1
                                if mismatches > args.mismatchTolerance:
                                    break
                        except IndexError:
                            raise RuntimeError("ABORTED: Encountered an error reading " + fileName + " where we got an error comparing input sequence " + self.guide + " to " + guide + ".  This could be due to a corrupted, shortened sequence in the data file, or a bug in the program.")
                        extendedRefGuide = beforeStart + guide[::-1]
                        extendedGuide = extendedRefGuide[-(len(beforeStart) + len(self.guide))]
                        extendedPam = pam[::-1] + afterPam
                        extendedSiteSeq = extendedGuide + extendedPam
                        if i == len(self.guide) - 1:
                            mismatchSites = []  #find the position in the guide of all mismatches, indexed to the base right before the PAM being [0]
                            for j in range(0,len(self.guide)):
                                if guide[j] != self.guide[j]:
                                    mismatchSites.append(j)
                                    if len(mismatchSites) == mismatches:  #once we have a number of mismatch index values equal to our number of mismatches, we can stop
                                        break                            
                            matchGuide = guide[:len(guide)]
                            matchGuide = matchGuide[::-1]
                            matchSeq = matchGuide + pam[::-1]
                            matchSeqExtended = matchSeq
                            guideDiff = len(guide) - len(self.guide) #accounting for a longer guide sequence in the stored reference
                            if guideDiff != 0:
                                matchSeq = matchSeq[guideDiff:]
                                if strand == "+":
                                    begin = str(int(begin) + guideDiff)
                                if strand == "-":
                                    end = str(int(end) - guideDiff)
                            
                            self.matchTable[mismatches].append(MatchSite(chrom, begin, end, matchSeq, str(1000*((len(guide)-mismatches)/len(guide))), strand, self.colorScheme[mismatches], mismatches, extendedSiteSeq, mismatchSites))
                            if args.verbose:
                                print("\nFound Match")
                    progress += 1
                    if progress % 1000 == 0 and (args.verbose or args.workerID == "0"):
                        print("Processed " + str(progress) + " lines", end = "\r")
        print("Processed " + str(progress) + " lines")
                            
    def reportResult(self):
        if args.workerID == "0":
            return self.matchTable
        else:
            import pickle
            self.tempDir = args.tempDir
            outputFile = open(self.tempDir + "/result/" + args.workerID, "wb")
            pickle.dump(self.matchTable, outputFile)
            outputFile.close()
            # output = open(self.tempDir + "/result" + args.workerID, "w")
            # for line in self.matches:
            #     output.write("\t".join(line) + "\n")  #check if this works more efficiently from a pickle
            # output.close()
            clockOut = open(self.tempDir + "/completed/" + args.workerID + ".done", "w")
            clockOut.close()

#===================================================FASTA indexing objects.  Requires a FASTA and FAI as input and will output a directory containing a list of targets for the system from the genome.=======================

class FASTAIndexLine(object):
    
    def __init__(self, line):
    # read from start to length + (length // 50) + start
        import re
        line = line.split("\t")
        line[0] = re.sub(r'chr','',line[0])
        self.contig = line[0]
        self.length = int(line[1])
        self.start = int(line[2])
        self.lineBases = int(line[3])
        self.lineBytes = int(line[4])
        self.end = self.length + ((self.lineBytes-self.lineBases)*(self.length // self.lineBases)) #this accounts for the fact that length is counted in bases and not bytes, and missed all the newline bytes that terminate each line
        self.endpoint = self.length + ((self.lineBytes-self.lineBases)*(self.length // self.lineBases)) + self.start

class ParallelIndexJob(object):
    
    def __init__(self, contig, start, end, workerID):
        self.contig = contig
        self.start = start
        self.end = end
        self.workerID = workerID
        self.jobName =  str(contig) + "." + str(workerID)
        self.chunkStartBase = 0
        
    def __str__(self):
        return str(self.contig) + "." + str(self.workerID)

class FASTASupervisor(object):
    
    def __init__(self):
        import os
        printStartUp()
        reportUsage("INDEX")
        if not self.isAnEnsemblSpecies(args.species):  #make sure that the species they entered is one that is annotated, or make them set an option to ignore this
            if not args.clobber:
                raise RuntimeError("ABORTED: " + args.species.upper() + " is not a valid ensembl species.  Please check your naming of this species.  If this is known not to be an ensembl species, rerun with clobber mode on (argument '-9') to ignore this issue.")
        redundantGenome = self.suitableIndexedGenomeExists()
        if redundantGenome:
            if not args.clobber:
                seq, genome, species = redundantGenome.split(".")
                print("Suitable indexed genome already exists.  Indexed genome info:")
                print("Sequence " + seq[::-1])
                print("  Genome " + genome)
                if not args.directToCompiler:
                    raise RuntimeError("ABORTED: Suitable genome exists.  Please delete existing one (or run in clobber mode, not recommended).")
                else:
                    if not args.recreateTree:
                        print("Attempting to compile directly.")
                    else:
                        print("Attempting to recreate saved tree structure.")
        self.countFileName = args.genomeListDirectory + "genomeData/" + args.sequence[::-1].upper() + "." + args.genome.upper() + "." + args.species.upper()
        if not args.directToCompiler and os.path.isfile(self.countFileName + ".gather"): #checking for an existing gather file and deleting it if it exists
            os.remove(self.countFileName + ".gather")
        if not args.directToCompiler and os.path.isfile(self.countFileName):  #and removing an existing countfile as well
            os.remove(self.countFileName)
        if args.directToCompiler and not redundantGenome:
            raise RuntimeError("ABORTED: Unable to find the genome for going direct to bin compilation.")
        if redundantGenome and not args.directToCompiler:
            import shutil
            shutil.rmtree(args.genomeListDirectory + redundantGenome)
        self.getFiles(args.inputfile)
        self.createTempDir()
        self.createOutputDir()
        if not args.directToCompiler:
            if args.ordered:
                self.faiJobs()
            else:
                self.createParallelJobs()
                if args.cluster:
                    while len(self.parallelJobs) > args.maxParallelJobs:
                        print("WARNING: Current chunk size generated too many parallel jobs.  Increasing chunk size by 50% and trying again.")
                        args.chunkSize = args.chunkSize * 1.5
                        self.createParallelJobs()
                    self.assignParallelJobs()
                    self.monitorJobs()
                if args.standAlone:
                    self.runJobQueue()
                self.gatherCounts()
        self.runBinCompiler()
        self.createTreePickle()
        if not args.noCleanup:
            self.cleanup()
    
    def suitableIndexedGenomeExists(self):
        import os
        if not os.path.isdir(args.genomeListDirectory):
            return False
        seqPam, seqGuide = args.sequence[::-1].split("_")
        directoryContents = os.listdir(args.genomeListDirectory)
        for item in directoryContents:
            if not item[0] == "." and "." in item and "_" in item and "NNN" in item:
                itemSeq, itemGenome, itemSpecies = item.split(".")
                if itemGenome == args.genome:
                    if args.species.upper() != itemSpecies:  #If someone is trying to index a genome as being from a different species than an already annotated genome of the same name, warn them and require them to set the clobber option to do it.  They really should not be doing that.
                        if not args.clobber:
                            raise RuntimeError("ABORTED: Warning: This exact genome has already been indexed as species " + itemSpecies + " it should not also be indexed as " + args.species.upper() + ".  If you wish to actually have this situation (not recommended), please set the clobber option in arguments (argument '-9').")
                    itemPam, itemGuide = itemSeq.split("_")
                    if seqPam == itemPam and len(seqGuide) <= len(itemGuide):
                        return item
        return False
    
    def isAnEnsemblSpecies(self, species):
        import urllib.request
        url = 'http://rest.ensembl.org/overlap/region/' + species.lower() + '/1:1000000-1000001?feature=gene'
        try:
            ensembl = urllib.request.urlopen(url)
            ensembl = ensembl.read().decode('utf-8')
            if "Can not find internal name for species" in ensembl:
                return False
        except urllib.error.HTTPError as error:
            message = error.read().decode('utf-8')
            if "Can not find internal name for species" in message:
                return False
            else:
                return True
        except urllib.error.URLError:
            print("Unable to reach/find ensembl server.  Please confirm you are connected to the internet.")
            return True
        return True
    
    def getFiles(self, fastaName):
        try:
            self.fasta = open(fastaName)
            firstLine = self.fasta.readline()
            if not ">" in firstLine:
                raise RuntimeError("ABORTED: " + fastaName + " does not appear to be a properly formatted FASTA file.  Please check to be sure that it follows FASTA standards.")
            self.fasta.close()
        except FileNotFoundError:
            raise RuntimeError("ABORTED: " + fastaName + " was not found.  This file was passed as the reference genome.")
        try:
            self.fai = open(fastaName + ".fai",'r')
        except FileNotFoundError:
            try:
                self.fai = open(fastaName[:-4] + ".fai", 'r')
            except FileNotFoundError:
                raise RuntimeError("ABORTED: No FASTA index (.fai) file could be found for " + fastaName + " please run a FASTA indexer and try again.")
    
    def createOutputDir(self):
        import os
        if not os.path.isdir(args.genomeListDirectory):
            os.mkdir(args.genomeListDirectory)
        if not os.path.isdir(args.genomeListDirectory + "genomeData"):
            os.mkdir(args.genomeListDirectory + "genomeData")
        outputDirectory = args.genomeListDirectory + args.sequence[::-1] + "." + args.genome + "." + args.species
        if not args.directToCompiler:
            if os.path.isdir(outputDirectory) and not args.clobber:
                raise RuntimeError("ABORTED: This genome/system combination has already been indexed.")
            else:
                os.mkdir(outputDirectory)
        self.outputDirectory = outputDirectory        
    
    def faiJobs(self):
        contigJobs = []
        rawLine = self.fai.readline()
        while rawLine:
            line = FASTAIndexLine(rawLine)
            contigJobs.append(line)
            rawLine = self.fai.readline()
        for job in contigJobs[1:]:
            self.createJobBash(job)
            self.submitJob(job)
        myJob = contigJobs[0]
        args.chromosome = myJob.contig
        args.start = str(myJob.start)
        args.length = str(myJob.end)
        myRun = FASTAreader()
        print("Completed this job.  Parallel jobs may still be running.")
        
    def createParallelJobs(self):
        contigData = []
        rawLine = self.fai.readline()
        while rawLine:
            line = FASTAIndexLine(rawLine)
            contigData.append(line)
            rawLine = self.fai.readline()
        self.contigList = []
        for line in contigData:
            self.contigList.append(str(line.contig))        
        parallelJobs = []
        windowLength = len(args.sequence) - 1  #the minus 1 accounts for the underscore separating the guide and pam
        for line in contigData:
            chunkSize = args.chunkSize
            chunkNumber = 0
            contigFinished = False
            contigStartByte = line.start
            contigEndByte = line.endpoint
            while not contigFinished:
                contig = line.contig
                start = contigStartByte + (chunkSize * chunkNumber)
                end = chunkSize + start
                if end >= contigEndByte:
                    contigFinished = True
                    readLength = contigEndByte - start
                    chunkNumber += 1
                else:
                    readLength = chunkSize + windowLength -1  #this will read windowLength - 1 bytes into the next chunk.  This means that the last window of this chunk will be one byte before the first windw of the next one
                    chunkNumber += 1
                parallelJobs.append(ParallelIndexJob(contig, start, readLength, chunkNumber))
        self.parallelJobs = parallelJobs
        
    def assignParallelJobs(self):    
        if not args.forceJobIndex:
            self.myJobIndex = len(self.parallelJobs) // 2  #making this instance take the job in the middle so that it less likely to be running through a string of pure "N"s
        else:
            self.myJobIndex = int(args.forceJobIndex)
        for i in range(0,len(self.parallelJobs)):
            if i != self.myJobIndex:
                self.createJobBash(self.parallelJobs[i],self.parallelJobs[i].workerID)
                self.submitJob(self.parallelJobs[i],self.parallelJobs[i].workerID)
        myJob = self.parallelJobs[self.myJobIndex]
        args.chromosome = myJob.contig
        args.start = str(myJob.start)
        args.length = str(myJob.end)
        args.workerID = str(myJob.workerID)
        self.myRun = FASTAreader()
        print("Completed this job. Checking/monitoring other parallel jobs.")
        
    def runJobQueue(self):
        import os
        import time
        import datetime
        startTime = datetime.datetime.now()
        jobList = {'queued':[],'running':[],'complete':[]}
        maxSimultaneousJobs = args.maxParallelJobs #no further calculation is needed here, since FASTAworkers don't launch subprocesses like search managers do
        print("Allowing only " + str(maxSimultaneousJobs) + " running jobs at once.")
        jobList['queued'] = self.parallelJobs
        while jobList['queued'] or jobList['running']:
            try:
                while jobList['queued'] and len(jobList['running']) < maxSimultaneousJobs:
                    self.createJobBash(jobList['queued'][0],jobList['queued'][0].workerID)
                    self.submitJob(jobList['queued'][0],jobList['queued'][0].workerID)
                    jobList['running'].append(jobList['queued'][0])
                    del jobList['queued'][0]
                while len(jobList['running']) >= maxSimultaneousJobs or len(jobList['queued']) == 0:
                    newlyCompleted = []
                    for i in range(0, len(jobList['running'])):
                        if args.ordered:
                            touchFileName = jobList['running'].contig
                        else:
                            touchFileName = jobList['running'][i].contig + "." + str(jobList['running'][i].workerID)
                        if os.path.isfile(self.tempDir + "/completed/" + touchFileName):
                            newlyCompleted.append(i)
                    newlyCompleted.sort(reverse = True)
                    if newlyCompleted:
                        for completedIndex in newlyCompleted:
                            jobList['complete'].append(jobList['running'][completedIndex])
                            del jobList['running'][completedIndex]
                    if not jobList['running'] and not jobList['queued']:
                        break
                    time.sleep(10)
            except KeyboardInterrupt:
                for key in list(jobList.keys()):
                    print(key)
                    for item in jobList[key]:
                        print("\t" + item.jobName)
                    if yesAnswer("Continue with run?"):
                        continue
                    else:
                        raise RuntimeError("ABORTED: By your command.")
        runTime = datetime.datetime.now() - startTime
        print ("Parallel index completed in " + (str(runTime)))
        
    def calculateRAM(contigSize):
        pass  #skipping this method, as it seems like everything can run with 2G or less
    
    def createTempDir(self):
        import re
        import os
        import datetime
        successful = False
        while not successful:
            currenttime = datetime.datetime.now()
            currenttime = str(currenttime)
            currenttime = re.sub(r'\W','',currenttime)
            self.tempDir = args.scratchFolder + '.indexJob' + currenttime
            args.tempDir = self.tempDir
            if os.path.isdir(self.tempDir):
                continue
            try:
                os.mkdir(self.tempDir)
            except OSError:
                continue
            successful = True
        os.mkdir(self.tempDir + "/completed")
        os.mkdir(self.tempDir + "/progress")
        os.mkdir(self.tempDir + "/compilerBash")
        os.mkdir(self.tempDir + "/compiled")
        return True
    
    def createJobBash(self, job, workerID = False):
        import os
        self.bash = self.tempDir + "/" + job.contig + "." + str(workerID) + ".sh"
        bashFile = open(self.bash, 'w')
        bashFile.write("#! /bin/bash\n")
        #bashFile.write("module load python/3.4\n")
        if not workerID:
            bashFile.write(pythonInterpreterAbsolutePath + " dsNickFury" + currentVersion + ".py --mode FASTAWorker --chromosome " + job.contig + " --start " + str(job.start) + " --length " + str(job.end) + " --sequence " + args.sequence + " --inputfile " + os.path.abspath(args.inputfile) + " --genome " + args.genome + " --tempDir " + args.tempDir + " --species " + args.species + " --treeLevel1 " + str(args.treeLevel1) + " --treeLevel2 " + str(args.treeLevel2) + " --genomeDirectory " + args.genomeListDirectory + "\n")
        else:
            bashFile.write(pythonInterpreterAbsolutePath + " dsNickFury" + currentVersion + ".py --mode FASTAWorker --workerID " + str(workerID) + " --chromosome " + job.contig + " --start " + str(job.start) + " --length " + str(job.end) + " --sequence " + args.sequence + " --inputfile " + os.path.abspath(args.inputfile) + " --genome " + args.genome + " --tempDir " + args.tempDir + " --chunkSize " + str(args.chunkSize) + " --species " + args.species + " --treeLevel1 " + str(args.treeLevel1) + " --treeLevel2 " + str(args.treeLevel2) + " --genomeDirectory " + args.genomeListDirectory.replace(" ",'\ ') + "\n")
        bashFile.close()
    
    def submitJob(self, job, workerID = False):
        if args.cluster:
            import os
            import subprocess
            import time
            if not workerID:
                shortName = "NickFury" + job.contig
            else:
                shortName = "NF." + job.contig + "." + str(workerID)    
            command = "qsub -cwd -V -N " + shortName + " -l h_data=2G,time=2:59:59 -e " + os.getcwd() +  "/schedulerOutput/ -o " + os.getcwd() + "/schedulerOutput/ " + self.bash
            if not args.mock:
                submitted = False
                failCounter = 0
                while not submitted:
                    result = os.system(command)
                    if result == 0:
                        submitted = True
                    else:
                        failCounter += 1
                        if failCounter > 50:
                            raise RuntimeError("Unable to submit job to queue after 50 attempts.  Please troubleshoot your scheduler and try again.")
                        print("Failed submission.  Waiting 5 seconds and retrying.")
                        time.sleep(5)
            else:
                print ("MOCK SUBMIT: " + command + " " + arguments)
        if args.standAlone:
            if not workerID:
                shortName = "NickFury" + job.contig
            else:
                shortName = "NF." + job.contig + "." + str(workerID)
            print("Submitting " + shortName)
            command = "bash " + self.bash
            if not args.mock:
                import subprocess
                subprocess.Popen(command, shell = True)
            else:
                print ("MOCK SUBMIT: " + command)
    
    def monitorJobs(self):
        import time
        import os
        allDone = False
        while not allDone:
            completedItems = os.listdir(self.tempDir + "/completed")
            #completedItems.append(str(args.chromosome + "." + str(args.workerID)))  #adding this instance's job to the completed job list
            for job in self.parallelJobs:
                checkJob = job.jobName
                #print("Checking " + checkJob)
                if not checkJob in completedItems:
                    #print("It was not found.")
                    allDone = False
                    time.sleep(60)
                    break
                else:
                    #print("It was found.")
                    allDone = True
        #print("Found all files.")
        print("All parallel jobs completed.  Finishing up.")
        return True

    def gatherCounts(self):
        import re
        counts = {}
        alreadyCounted = {}
        for contig in self.contigList:
            counts[contig] = 0
            alreadyCounted[contig] = []
        gatherFile = open(self.countFileName +  ".gather", 'r')
        rawData = gatherFile.read()
        gatherFile.close()
        data = rawData.split("\n")
        for datum in data:
            if datum:
                contig, workerID, hitCount = datum.split("\t")
                if workerID in alreadyCounted[contig]:
                    continue #protection against unintentional double counting if the job was previously stopped and restarted
                else:
                    counts[contig] += int(hitCount)
                    alreadyCounted[contig].append(workerID)
        output = open(self.countFileName, 'w')
        for contig in self.contigList:
            output.write(contig + "\t" + str(counts[contig]) + "\n")
        output.close()
    
    def runBinCompiler(self):
        self.createBinCompilerJobs()
        if not args.recreateTree:
            self.runBinCompilerJobs()
            self.monitorCompilerJobs()
    
    def createBinCompilerJobs(self):
        import os
        self.bigBinList = []
        for item in os.listdir(self.outputDirectory):
            if os.path.isdir(self.outputDirectory + os.sep + item) and item.endswith(".targetbin"):
                self.bigBinList.append(item.replace(".targetbin",""))
        if not self.bigBinList:
            raise RuntimeError("Quit with error.  Was expecting a list of bins to compile, but did not get one.")
        jobNumber = args.maxParallelJobs
        if jobNumber < 1 or len(self.bigBinList) < jobNumber:
            jobNumber = len(self.bigBinList)
        jobList = []
        for i in range(0,jobNumber):
            jobList.append([])
        assignmentCounter = 0  #just initializing this value.  I can mod it by the jobNumber in the loop to know where to assign a bin
        for bigBin in self.bigBinList:
            jobList[assignmentCounter % jobNumber].append(bigBin)
            assignmentCounter += 1
        assignmentCounter = 0 #now using this to count job numbers
        for job in jobList:
            if not args.recreateTree:
                self.createBinCompilerBash(job, str(assignmentCounter))
            assignmentCounter += 1
        self.parallelCompileJobs = jobNumber
            
    def createBinCompilerBash(self, jobList, jobNumber):
        import os
        noCleanup = ""
        if args.noCleanup:
            noCleanup = "--noCleanup "
        jobNumber = str(jobNumber) #this should come in as a string, but just to be safe
        bashFile = open(self.tempDir + "/compilerBash/" + jobNumber + ".sh", 'w')
        bashFile.write("#! /bin/bash\n")
        bashFile.write(pythonInterpreterAbsolutePath + " dsNickFury" + currentVersion + ".py --mode compiler --workerID " + jobNumber + " --bins " + ",".join(jobList) + " --sequence " + args.sequence + " --genome " + args.genome + " --tempDir " + args.tempDir + " --species " + args.species + " " + noCleanup + " --genomeDirectory " + args.genomeListDirectory.replace(" ",'\ ') + "\n")
        bashFile.close()
        
    def runBinCompilerJobs(self):
        import os
        import subprocess
        import time
        for job in range(0,self.parallelCompileJobs):
            if args.cluster:
                shortName = "Aug" + str(job)
                command = "qsub -cwd -V -N " + shortName + " -l h_data=2G,time=2:59:59 -e " + os.getcwd() +  "/schedulerOutput/ -o " + os.getcwd() + "/schedulerOutput/ " + self.tempDir + "/compilerBash/" + str(job) + ".sh"
                if not args.mock:
                    submitted = False
                    failCounter = 0
                    while not submitted:
                        result = os.system(command)
                        if result == 0:
                            submitted = True
                        else:
                            failCounter += 1
                            if failCounter > 50:
                                raise RuntimeError("Unable to submit job to queue after 50 attempts.  Please troubleshoot your scheduler and try again.")
                            print("Failed submission.  Waiting 5 seconds and retrying.")
                            time.sleep(5)
                else:
                    print ("MOCK SUBMIT: " + command + " " + arguments)
            if args.standAlone:
                shortName = "Aug" + str(job)
                print("Submitting " + shortName)
                command = "bash " + self.tempDir + "/compilerBash/" + str(job) + ".sh"
                if not args.mock:
                    import subprocess
                    subprocess.Popen(command, shell = True)
                else:
                    print ("MOCK SUBMIT: " + command)
        
    def monitorCompilerJobs(self):
        import os
        import time
        print("All compiler jobs submitted.  Monitoring jobs for completion.")
        completed = False
        while not completed:
            for i in range(0, self.parallelCompileJobs):
                if os.path.isfile(self.tempDir + os.sep + "compiled" + os.sep + str(i) + ".done"):
                    completed = True
                else:
                    completed = False
                    print("Currently awaiting job " + str(i), end = "\r")
                    time.sleep(5)
                    break
        print() #ends previous line without overwriting it
        print("All jobs reported as done.")
       
    def createTreePickle(self):
        import os
        import pickle
        treeStructure = {}
        print("Generating tree level 1")
        for bigBin in self.bigBinList:
            print("Generating level 2 for " + bigBin, end = "\r")
            treeStructure[bigBin] = []   #making this one a set to avoid any possibility of duplication since we don't care about order
            binDir = os.listdir(self.outputDirectory + os.sep + bigBin + ".targetbin")
            for item in binDir:
                if os.path.isfile(self.outputDirectory + os.sep + bigBin + ".targetbin" + os.sep + item) and item.endswith(".targets"):
                    size = os.path.getsize(self.outputDirectory + os.sep + bigBin + ".targetbin" + os.sep + item)
                    treeStructure[bigBin].append((item.replace(".targets",""),size))
        outputFile = open(self.outputDirectory + os.sep + "tree.pkl", 'wb')
        pickle.dump(treeStructure, outputFile)
        outputFile.close()
        print() #ends previous line without overwriting it
        print("Tree structure generated and stored for quick retrieval.")
           
    def cleanup(self):
        import os
        import shutil
        if not args.directToCompiler:
            os.remove(self.countFileName + ".gather")
        shutil.rmtree(self.tempDir)

class TargetTree(object):
    
    def __init__(self, level1, level2): #initialize our target tree object.  Only thing we need to start off knowing is how many bases to make each level (ints)
        self.targetHash = {}
        self.level1 = int(level1)
        self.level2 = int(level2)
        
    def add(self, site):
        pam, guide = site.sequence.split("_")
        if len(guide) < self.level1 + self.level2:
            raise RuntimeError("Combined bin length is greater than the set guide length.  Guide length: " + str(len(guide)) + " bins: " + str(self.level1) + ", " + str(self.level2) + ".")
        bigBin = guide[:self.level1]
        smallBin = guide[self.level1:self.level1 + self.level2]
        sequenceString = "/".join([site.sequence, site.beforeStart, site.afterPAM])
        writeString = "\t".join([site.contig, str(site.start), str(site.end), sequenceString, site.strand]) + "\n"
        try:  #try to add the leaf directly on the tree in the appropriate location
            self.targetHash[bigBin].append([smallBin, writeString])
        except KeyError:  #if the appropriate twig is not present, create the twig
            self.targetHash[bigBin] = []
            self.targetHash[bigBin].append([smallBin,writeString])
            
    def dump(self, directory, chromosome, jobID):
        import os
        import pickle
        directory = str(directory)  #almost impossible that this would come in as anything else
        jobID = str(jobID)  #quite possible that this could come in as an int type
        chromosome = str(chromosome)
        bigBins = list(self.targetHash.keys())
        written = 0
        totalFiles = len(bigBins)
        for bigBin in bigBins:
            smallBinDataList = self.targetHash[bigBin]
            if not os.path.isdir(directory + os.sep + bigBin + ".targetbin"):
                try:
                    os.mkdir(directory + os.sep + bigBin + ".targetbin")
                except OSError:  #this will happen if another process creates the bin directory during the short time between us checking for and not finding it and us trying to make it in this process
                    pass
            dumpFile = open(directory + os.sep + bigBin + ".targetbin/" + os.sep + chromosome + "." + jobID + ".dump", "wb")
            pickle.dump(smallBinDataList, dumpFile)
            dumpFile.close()
            written += 1
            print(str(written) + " of " + str(totalFiles) + " target collections written.", end = "\r")
        print() #this just ends the line without overwriting it
        
class TargetFound(object):
    
    def __init__(self, contig, start, end, sequence, beforeStart, afterPAM, strand):
        self.contig = str(contig)
        self.start = str(start)
        self.end = str(end)
        self.sequence = sequence[::-1]
        self.afterPAM = afterPAM
        self.beforeStart = beforeStart
        self.strand = strand

class SequenceSearch(object):
    
    def __init__(self, inputFile, contigStart, contigLength, windowsize, pamList, beforeStartExtension = 4, afterPAMextension = 3):
        self.beforeStartExtension = int(beforeStartExtension)
        self.afterPAMextension = int(afterPAMextension)
        self.maxExtension = max(self.beforeStartExtension, self.afterPAMextension)
        self.lastGroup = 0
        self.done = False
        self.windowsize = windowsize
        self.start = 0  #start is inclusive
        self.end = self.windowsize #end is not inclusive (keeping with BED standards)
        self.pamList = pamList
        self.pamLength = len(pamList[0])  #calling the first item in the list so I don't just get the number of possible pams
        self.extendedStart = self.getExtendedStart(inputFile, contigStart)
        self.extendedEnd = self.getExtendedEnd(inputFile, contigStart, contigLength)
        inputFile.seek(int(contigStart))
        self.refSeq = inputFile.read(int(contigLength))
        self.refSeq = self.refSeq.replace("\n","")
        self.refSeq = self.refSeq.upper()
        self.refSeqLength = len(self.refSeq)

        
    def getExtendedStart(self, inputFile, contigStart):
        try:
            inputFile.seek(int(contigStart) - self.maxExtension - 20)
        except ValueError:  #if we are before the start of the file
            return False
        extension = inputFile.read(self.maxExtension + 20) #read in the (larger than we need) chunk of file from before the contig of interest
        extension = extension.replace("\n","") #get rid of end of line characters (they'll mess us up at the next step)
        for character in extension[-(self.maxExtension + 10):]:
            if character.upper() not in ['A','T','G','C','N']:  #this will trip off if we are seeing the contig name line in the extension (we won't get extensions near the start or end of the contig)
                return False
        if len(extension) < self.maxExtension:
            return False
        else:
            return extension[-self.maxExtension:]
        
    def getExtendedEnd(self, inputFile, contigStart, contigLength):
        try:
            inputFile.seek(int(contigStart) + int(contigLength))
        except ValueError:  #note that this should never actually happen unless the python standard changes.  If we seek past the end of the file, we will just keep reading a bunch of nothing (and will catch that later)
            return False
        extension = inputFile.read(self.maxExtension + 20)
        if not len(extension) < self.maxExtension:  #if we didn't read anything because we reached the end of the file
            return False
        extension = extension.replace("\n","")
        for character in extension[:self.maxExtension + 1]:  #we can use a shorter window here, since we are guaranteed to hit the > symbol denoting a new contig before we hit the contig name itself.  Contig names are unlikely, but not certain to trip this off.  The > is guaranteed to.
            if character.upper() not in ['A','T','G','C','N']:
                return False
        if len(extension) < self.maxExtension:
            return False
        else:
            return extension[:maxExtension]
        
    def nextMatch(self):
        self.forwardMatch = False
        self.reverseMatch = False
        if self.start // 10000 > self.lastGroup and (args.verbose or not args.workerID):
            print("Tested " + str((self.start // 10000)*10000), end = "\r")
            self.lastGroup = self.start // 10000
        self.sequence = self.refSeq[self.start:self.end]
        if ">" in self.sequence:
            raise RuntimeError("Ran off end of chromosome.  > in sequence: " + self.sequence)
        if self.sequence[-1] == "N":
            self.nInLastPositionJump()
            return False
        if "N" in self.sequence:
            return False
        if self.sequence[-self.pamLength:].upper() in self.pamList:
            guide = self.sequence[:-self.pamLength]
            pam = self.sequence[-self.pamLength:]
            self.forwardMatch = guide + "_" + pam
            for extension in range(self.afterPAMextension,0,-1):  #Start a loop that will iterate 3, 2, 1.  It will end before hitting 0 and we will be left with an empty string value (which we will try to handle after this)
                try:  #if we have the sequence, we grab what parts of it we can here
                    self.forwardAfterPAM = self.refSeq[self.end:self.end + extension]  #if this works, we had the sequence and quit the loop
                    break
                except IndexError:  #if we were off the edge of the sequence (something that will only happen at the very beginning or end)
                    self.forwardBeforeStart = ""
                    continue  #try taking a smaller extension
            if len(self.forwardAfterPAM) != self.afterPAMextension:
                if not self.extendedEnd:
                    self.extendedEnd = "X" * self.afterPAMextension
                missingLetterCount = self.afterPAMextension - len(self.forwardAfterPAM)
                extraLetters = self.extendedEnd[:missingLetterCount]  #we should already have verified that the extension was of the proper length.  If this throws an exception, that needs to be fixed, probably at the getExtension method level
                self.forwardAfterPAM = self.forwardAfterPAM + extraLetters
            for extension in range(-self.beforeStartExtension,0):
                try:
                    self.forwardBeforeStart = self.refSeq[self.start + extension:self.start]
                    break
                except IndexError:
                    self.forwardBeforeStart = ""
                    continue
            if len(self.forwardBeforeStart) != self.beforeStartExtension:
                if not self.extendedStart:
                    self.extendedStart = "X" * self.beforeStartExtension
                missingLetterCount = self.beforeStartExtension - len(self.forwardBeforeStart)
                extraLetters = self.extendedStart[-missingLetterCount:]
                self.forwardBeforeStart = extraLetters + self.forwardBeforeStart
        else:
            self.forwardMatch = False
        revComp = str(ReverseComplement(self.sequence))
        if revComp[-self.pamLength:].upper() in self.pamList:
            guide = revComp[:-self.pamLength]
            pam = revComp[-self.pamLength:]
            self.reverseMatch = guide + "_" + pam
            for extension in range(-self.afterPAMextension,0):
                try:
                    self.reverseAfterPAM = str(ReverseComplement(self.refSeq[self.start + extension:self.start]))
                    break
                except IndexError:
                    self.reverseAfterPAM = ""  #this will be reset if the loop completes and will stay an empty string if we are at the end of the contig
                    continue
            if len(self.reverseAfterPAM) != self.afterPAMextension:
                if not self.extendedStart:
                    self.extendedStart = "X" * self.afterPAMextension
                missingLetterCount = self.afterPAMextension - len(self.reverseAfterPAM)
                if not "X" in self.extendedStart:
                    extraLetters = str(ReverseComplement(self.extendedStart))[:missingLetterCount]
                else:
                    extraLetters = self.extendedStart[:missingLetterCount]
                self.reverseAfterPAM = self.reverseAfterPAM + extraLetters
            for extension in range(self.beforeStartExtension,0,-1):
                try:
                    self.reverseBeforeStart = str(ReverseComplement(self.refSeq[self.end:self.end + extension]))
                    break
                except IndexError:
                    self.reverseBeforeStart = ""
                    continue
            if len(self.reverseBeforeStart) != self.beforeStartExtension:
                if not self.extendedEnd:
                    self.extendedEnd = "X" * self.beforeStartExtension
                missingLetterCount = self.beforeStartExtension - len(self.reverseBeforeStart)
                if not "X" in self.extendedEnd:
                    extraLetters = str(ReverseComplement(self.extendedEnd))[-missingLetterCount:]
                else:
                    extraLetters = self.extendedEnd[-missingLetterCount:]
                self.reverseBeforeStart = extraLetters + self.reverseBeforeStart
        else:
            self.reverseMatch = False
        return (self.forwardMatch or self.reverseMatch)
    
    def nInLastPositionJump(self):
        self.start += self.windowsize - 1
        self.end += self.windowsize - 1
            
    def advance(self):
        self.start += 1
        self.end += 1
        self.done = self.end > self.refSeqLength
        
    def getNextMatch(self):
        self.first = True
        while not self.nextMatch() and not self.done or self.first:
            self.first = False
            self.advance()
        return (not self.done)
        
    
class FASTAreader(object):
    
    def __init__(self):
        self.hitCount = 0
        self.chunkStart = self.getChunkStart()
        self.outputDirectory = args.genomeListDirectory + args.sequence[::-1] + "." + args.genome + "." + args.species
        self.fileChromosome = self.getFileChromosome
        windowsize = len(args.sequence) - 1  #the minus 1 is because there is an underscore between the guide and pam
        guide, pam = args.sequence.split("_")
        pamList = self.createPamList(pam)
        inputFile = open(args.inputfile, 'r')
        self.runSearchJob(SequenceSearch(inputFile, args.start, args.length, windowsize, pamList))
        self.clockOut()
            
    def getChunkStart(self):
        lineDifference = self.getLineDifference()
        if args.workerID:
            chunkStartByte = int(args.chunkSize) * (int(args.workerID) - 1)
            chunkStart = chunkStartByte - (lineDifference * (chunkStartByte // self.lineBytes))
            #print("ChunkStartByte: " + str(chunkStartByte))
            #print("ChunkStart: " + str(chunkStart))
        else:
            chunkStart = 0
        return chunkStart
    
    def getLineDifference(self):
        inputFile = open(args.inputfile, 'r')
        characterCountCheck = inputFile.readline()
        while ">" in characterCountCheck:
            characterCountCheck = inputFile.readline()
        inputFile.close()
        self.lineBytes = len(characterCountCheck)
        lineBases = len(characterCountCheck.strip())
        lineDifference = self.lineBytes - lineBases
        #print("Line diff: " + str(lineDifference))
        return lineDifference
    
    def getFileChromosome(self):
        try:
            chromosome = int(args.chromosome)
            chromosome = str(chromosome).zfill(2)
        except ValueError:
            chromosome = args.chromosome
        if chromosome == "M":
            fileChromosome = "zM"
        else:
            fileChromosome = chromosome
        return fileChromosome
    
    def createPamList(self, pam):
        degeneratePam = False
        for character in pam:
            if character not in ["A","T","G","C"]:
                degeneratePam = True
        if not degeneratePam:
            pamList = [pam]
        else:
            pamList = list(NondegenerateBases(pam))
        return pamList
    
    def getOutputFileName(self):
        if not args.workerID:
            outputFileName = self.outputDirectory + "/" + self.fileChromosome + "c" + str(self.hitCount // 10000).zfill(9)
        else:
            outputFileName = self.outputDirectory + "/" + self.fileChromosome + "c" + str(args.workerID).zfill(3) + str(self.hitCount // 10000).zfill(9)
        return outputFileName
    
    def runSearchJob(self, searchJob):
        targetTree = TargetTree(args.treeLevel1, args.treeLevel2) #initializing the object to store all of our found CRISPR targets
        while searchJob.getNextMatch():
            if searchJob.forwardMatch:
                site = TargetFound(args.chromosome, (searchJob.start + self.chunkStart + 1), (searchJob.end + self.chunkStart + 1 + 1), searchJob.forwardMatch, searchJob.forwardBeforeStart, searchJob.forwardAfterPAM, "+") # The plus 1 in the position is because chromosome data is indexed to 0 while chromosome positions are indexed to 1.  The second +1 for the end location is to account for the BED file standard end base not being inclusive (like python indexing).
                targetTree.add(site)
                self.hitCount += 1
            if searchJob.reverseMatch:
                site = TargetFound(args.chromosome, (searchJob.start + self.chunkStart + 1), (searchJob.end + self.chunkStart + 1 + 1), searchJob.reverseMatch, searchJob.reverseBeforeStart, searchJob.reverseAfterPAM, "-")
                targetTree.add(site)
                self.hitCount += 1
        targetTree.dump(self.outputDirectory, args.chromosome, args.workerID)
         
    def clockOut(self):
        if not args.workerID:
            touchFile = open(args.tempDir + "/completed/" + args.chromosome, 'w')  #This is the clockout
            touchFile.close()
            countFileName = args.genomeListDirectory + "genomeData/" + args.sequence[::-1] + "." + args.genome + "." + args.species.upper() + ".gather"
            countFile = open(countFileName, 'a')
            countFile.write(args.chromosome + "\t" + str(self.hitCount) + "\n")
            countFile.close()
        else:
            self.countFileName = args.genomeListDirectory + "genomeData/" + args.sequence[::-1] + "." + args.genome + "." + args.species.upper() + ".gather"
            countFile = open(self.countFileName, 'a')
            countFile.write(args.chromosome + "\t" + args.workerID + "\t" + str(self.hitCount) + "\n")
            countFile.close()
            touchFile = open(args.tempDir + "/completed/" + args.chromosome + "." + str(args.workerID), 'w')
            touchFile.close()
            
class bigBinCompiler(object):
    
    def __init__(self):
        import os
        self.genomeDirectory = args.genomeListDirectory + args.sequence[::-1] + "." + args.genome + "." + args.species
        self.binList = args.bins.split(",")
        processedBins = 0
        print("Processed " + str(processedBins) + " of " + str(len(self.binList)) + " level 1 bins.")
        for largeBin in self.binList:
            self.compile(largeBin)
            processedBins += 1
            print("Processed " + str(processedBins) + " of " + str(len(self.binList)) + " level 1 bins.")
        self.clockOut()
        
    def compile(self, largeBin):
        import os
        import pickle
        import time
        binDir = self.genomeDirectory + os.sep + largeBin + ".targetbin"
        dirList = os.listdir(binDir)
        targetCollector = []
        dumpFiles = []
        for item in dirList:
            itemPath = binDir + os.sep + item
            if os.path.isfile(itemPath) and item.endswith(".dump"):
                dumpFiles.append(itemPath)
        print("Found " + str(len(dumpFiles)) + " collection files to process.")
        for file in dumpFiles:
            fileHandle = open(file, 'rb')
            targets = pickle.load(fileHandle)
            fileHandle.close()
            targetCollector += targets
        print("Total targets: " + str(len(targetCollector)))
        outputFileHash = {}
        print("Splitting targets by level 2 sequence")
        for target in targetCollector:
            try:
                outputFileHash[target[0]]["data"] += target[1]
            except KeyError:
                outputFileHash[target[0]] = {}
                outputFileHash[target[0]]["fileName"] = binDir + os.sep + target[0] + ".targets"
                outputFileHash[target[0]]["data"] = target[1]
        totalFiles = len(outputFileHash.keys())
        writeCount = 0
        print("Written " + str(writeCount) + " of " + str(totalFiles) + " files.", end = "\r")
        for key in list(outputFileHash.keys()):
            outputFile = open(outputFileHash[key]["fileName"],'w')
            outputFile.write(outputFileHash[key]["data"])
            outputFile.close()
            writeCount += 1
            print("Written " + str(writeCount) + " of " + str(totalFiles) + " files.", end = "\r")
        print("All " + str(writeCount) + " files written!  Cleaning up collectors.")
        if not args.noCleanup:
            for dumpFile in dumpFiles:
                os.remove(dumpFile)
        print("Clean up complete.")        
                        
    def clockOut(self):
        touchFile = open(args.tempDir + "/compiled/" + str(args.workerID) + ".done", 'w')
        touchFile.close()    
            
#=====================================================Execution code===========================================================================

def main():
    import datetime
    import os
    if not os.path.isdir("schedulerOutput"):  #Used for writing scheduler output of subprocesses to a single folder, otherwise this folder can start getting messy.  Only needed for cluster operation, not single server.
       os.mkdir("schedulerOutput")
    startTime = datetime.datetime.now()
    arguments = Args()
    global args
    args = arguments
    del arguments
    if args.mode == 'index':
        run = FASTASupervisor()
    elif args.mode == 'FASTAWorker':
        run = FASTAreader()
    elif args.mode == 'search':
        run = SearchSupervisor()
    elif args.mode == 'worker':
        run = WorkerJob()
    elif args.mode == 'selection':
        run = TargetSelection()
    elif args.mode == 'compiler':
        run = bigBinCompiler()
    runTime = datetime.datetime.now() - startTime
    print (args.mode.upper() + " run completed in " + (str(runTime)))
    
main()