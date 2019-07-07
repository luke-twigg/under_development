#! python3

# import required libraries
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import tarfile

# import sys, and then the gdal_merge from the local file location
import sys
sys.path.append(r"C:\Program Files\QGIS 2.18\bin")
import gdal_merge

# setup TK window and hide so only dialogs are visible
root = Tk()
root.withdraw()

# user input of landsat tar.gz filenames to be extracted, abort if no files selected
fileraw = fd.askopenfilenames(initialdir = "/", title = "Select Landsat tar.gz files")
if len(fileraw) == 0:
    messagebox.showwarning("File Selection", "No files selected")
    quit()

# user input of output file location, abort if no folder selected
outlocation = fd.askdirectory(title="Please select an output folder")
if len(outlocation) == 0:
    messagebox.showwarning("Output location", "No output folder selected")
    quit()

# convert tuple of files into list, and loop through each tar file, performing extraction and merge
filelist = list(fileraw)
for infile in filelist:

    # if file is not a tar.gz file, skip
    if not infile.endswith(".tar.gz"):
        continue

    # establish file name
    filebase = os.path.basename(infile)[:-7]
    temploc = outlocation + "/" + filebase + "/"

    print("extracting file " + filebase)

    # extract image files to temporary subfolder
    tar = tarfile.open(infile, mode="r:gz")
    tar.extractall(temploc)






