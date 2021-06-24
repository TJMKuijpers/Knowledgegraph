# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:19:22 2021

@author: tkuijpe1
"""

import os
import pandas as pd
import seaborn as sns
from py2neo import Graph, Node, Relationship
class LabeledPropertyGraph:
    
    def __init__(self,fileLocationData,fileLocationModel):
        self.fileLocation=fileLocationData
        self.modelLocation=fileLocationModel
        self.data=None
        self.nodes=None
        self.LPG=None
        self.dataType='LPG'
        
    def checkFileExistence(self):
        statusFileExists=os.path.isfile(self.modelLocation)
        return statusFileExists
    
    def loadFile(self):
        statusFile=self.checkFileExistence()
        if statusFile:
           if self.fileLocation.endswith('.txt'):
              self.data=pd.read_csv(self.fileLocation,sep="\t")
           elif self.fileLocation.endswith('.csv'):
              self.data=pd.read_csv(self.fileLocation,sep=",")
           else:
                print('Only text and csv files are supported')
        else:
            print('File does not exist')
            
    
    def createInteractions(self):
        # Relationship is in format (object - relation - object)
        return None
    
    def createObjectNodes(self):
        allNodes=[self.Data.parent,self.Data.Child]
        allNodes_flat=set([item for x in allNodes for item in x])
        self.nodes=allNodes_flat

    def addPropertiesToNodes():
        return None
    
class connectGraphToNeo4j:

    def __init__(localhostname,username, password):
        self.localhost=localhostname
        self.password=password
        self.username=username
        self.graph=None

    def connect_to_database(self):
        graph = Graph(self.localhost, auth=(self.username,self.password))
        self.graph=graph
        # check if graph connection works

    def add_nodes_to_graph(self,nodestoadd):
        tx=self.graph.begin()
        for x in nodestoadd:
            tx.append("Create (node:Node name: $name) RETURN node", name=x)
        


    def add_interactions_to_graph(self,relationstoadd):

    def add_properties_to_nodes(self,proertiestoadd):
        return None