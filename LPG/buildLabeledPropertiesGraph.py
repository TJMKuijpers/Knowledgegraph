# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:19:22 2021

@author: tkuijpe1
"""

import os
import pandas as pd
import csv

class buildLabeledPropertiesGraph(fileLocationData=None):
    
    def __init__(self):
        self.fileLocation=fileLocationData
        self.data=None
        self.LPG=None
        self.dataType='LPG'
        
    def checkFileExistence(self):
        statusFileExists=os.path.isfile(self.fileLocation)
        return statusFileExists
    
    def loadFile(self:
        statusFile=checkFileExistence()
        if statusFile=True:
            # File exist and we can read it
            if self.fileLocation.endswith('.txt'):
                self.data=pd.read(self.fileLocation,sep="\t")
            if self.fileLcation.endswith('.csv'):
                # Check automatically if sep is ";" or ","
                self.data=pd.read(self.fileLocation,sep=",")
            else:
                print('Only text and csv files are supported')
        else:
            print('File does not exist')
            
    
    def createLPGInteractions():