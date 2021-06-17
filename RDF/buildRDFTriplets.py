# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:45:06 2021

@author: T.J.M. Kuijpers


Python script to transform edge list to RDF triplets
"""
import os
import pandas as pd
class buildRDFTriplets(fileLocationData=None):
    
    def __init__():
        self.fileLocation=fileLocationData
        self.data=None
        self.rdfTriplets=None
        self.dataType='RDFTriplets'
        
    def checkFileExistence():
        statusFileExists=os.path.isfile(self.fileLocation)
        return statusFileExists
    
    def loadFile():
        statusFile=checkFileExistence()
        if statusFile:
            # File exist and we can read it
            if self.fileLocation.endswith('.txt'):
                self.data=pd.read(self.fileLocation,sep="\t")
            if self.fileLcation.endswith('.csv'):
                # Check automatically if sep is ";" or ","
                self.data=pd.read(self.fileLocation,sep=)
            else:
                print('Only text and csv files are supported')
        else:
            print('File does not exist')
            
        
