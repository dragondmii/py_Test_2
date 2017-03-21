#!/usr/bin/python

#####################
## module: py_exam_02.py
## Robert Epstein
## A01092594
#####################

import cv2
import argparse
import os
import sys

# you can use either re or fnmatch
# to implement generate_filenames.
# uncomment the import you need.
#import re
import fnmatch

# if you need/want to use numpy, uncomment
# the next import
#import numpy as np

ap = argparse.ArgumentParser()
# two optional arguments
ap.add_argument('-ip', '--imgpath', help = 'path to image')
ap.add_argument('-id', '--imgdir', help = 'path to image directory')
args = vars(ap.parse_args())

# takes a file name pattern fnpat and recursively
# generates a list of filenames that match the pattern in directory rootdir
def generate_file_names(fnpat, rootdir):
  for path, dirlist, filelist in os.walk(rootdir):
    for file_name in fnmatch.filter(filelist, fnpat):
      yield os.path.join(path, file_name)
  pass
                      
def classify_figure(image):
  '''
  if image contains triangle, return 'trie'
  if image contains diamond, return 'dmd'
  if image contains rectangle, return 'rec'
  if unable to classify, return 'unknown'
  '''
  ## your code
  count = 0
  array = []
  (h, w, num_c) = image.shape
  (B, G, R) = cv2.split(image)
  for height in xrange(h):
    for width in xrange(w):
      if B[height,width]==[0]:
        count += 1
    array.append(count)
    count = 0
  print array
  change_row = []
  for x in xrange(len(array)):
    if x != 0:
      change_row.append(array[x-1]-array[x])
  print change_row
  ## count number of white pixels in each row
  ## ignore first row of whites (where count goes from 0 to 1+
  ## make array of change in white pixels
  ## if change is always 0: object is rec
  ## next create change array for columns
  ## if change_row is of both signs (positive then negative) and change_column -
  ## - of both signs (positive then negative): object is dmd
  ## if change_row or change_column is all one sign: object is trie
  pass

def classify_figures_in_dir(imgdir):
    '''
    classify each image in imgdir and compute accuracy
    '''
    # your code
    pass

def area(image):
    '''
    compute the area of a figure in image
    '''
    # your code
    pass

def classify_figures_and_compute_areas_in_dir(imgdir):
    '''
    classify figures, compute their areas, and print out three largest rectangles,
    triangles, and diamonds.
    '''
    # your code
    pass

def test_classify_figure(imgp):
  img = cv2.imread(imgp)
  print classify_figure(img)
  del img

def test_area(imgp):
  img = cv2.imread(imgp)
  print area(img)
  del img

## uncomment/comment appropriate tests when debugging
if __name__ == '__main__':
  if args['imgpath'] is not None:
    test_classify_figure(args['imgpath'])
    #test_area(args['imgpath'])
  elif args['imgdir'] is not None:
    classify_figures_in_dir(args['imgdir'])
    #classify_figures_and_compute_areas_in_dir(args['imgdir'])
