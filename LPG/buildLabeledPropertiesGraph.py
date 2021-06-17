# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:19:22 2021

@author: tkuijpe1
"""

import os
import pandas as pd
import csv

class buildLabeledPropertiesGraph:
    
    def __init__(self,fileLocationData):
        self.fileLocation=fileLocationData
        self.data=None
        self.LPG=None
        self.dataType='LPG'
        
    def checkFileExistence(self):
        statusFileExists=os.path.isfile(self.fileLocation)
        return statusFileExists
    
    def loadFile(self):
        statusFile=self.checkFileExistence()
        if statusFile:
           if self.fileLocation.endswith('.txt'):
              self.data=pd.read(self.fileLocation,sep="\t")
           if self.fileLcation.endswith('.csv'):
              self.data=pd.read(self.fileLocation,sep=",")
           else:
                print('Only text and csv files are supported')
        else:
            print('File does not exist')
            
    
    def createLPGInteractions(self):
        # Relationship is in format (object - relation - object)
        return None
    def createObjectNodes(self):
        return None
        
    def addPropertiesToNodes():
        return None
    
    
    
