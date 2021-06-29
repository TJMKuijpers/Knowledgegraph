# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:19:22 2021

@author: tkuijpe1
"""

import os
import pandas as pd
from neo4j import GraphDatabase


class LabeledPropertyGraph:

    def __init__(self, fileLocationData, fileLocationModel):
        self.fileLocation = fileLocationData
        self.modelLocation = fileLocationModel
        self.data = None
        self.nodes = None
        self.LPG = None
        self.dataType = 'LPG'

    def checkFileExistence(self):
        statusFileExists = os.path.isfile(self.modelLocation)
        return statusFileExists

    def loadFile(self):
        statusFile = self.checkFileExistence()
        if statusFile:
            if self.fileLocation.endswith('.txt'):
                self.data = pd.read_csv(self.fileLocation, sep="\t")
            elif self.fileLocation.endswith('.csv'):
                self.data = pd.read_csv(self.fileLocation, sep=",")
            else:
                print('Only text and csv files are supported')
        else:
            print('File does not exist')

    def createInteractions(self):
        # Relationship is in format (object - relation - object)
        return None

    def createObjectNodes(self):
        allNodes = [self.data.Parent, self.data.Child]
        allNodes_flat = set([item for x in allNodes for item in x])
        self.nodes = allNodes_flat

    def addPropertiesToNodes():
        return None


class connectGraphToNeo4j:

    def __init__(self, local_db_name, username, password):
        self.localhost = local_db_name
        self.password = password
        self.username = username
        self.graph = None
        self.create_interactions_batch = []

    def connect_to_database(self):
        self.graph = GraphDatabase.driver(self.localhost, auth=(self.username, self.password))

    def add_nodes_to_graph(self, nodestoadd, node_type, node_type_id):
        create_statement_batch=[]
        for x in nodestoadd:
            create_node = "CREATE (" + node_type + ":" + node_type_id + "{Name:" +"'"+x+"'" + "})"
            print(create_node)
            create_statement_batch.append(create_node)
        print("push nodes to neo4j database")
        session = self.graph.session()
        for i in create_statement_batch:
            session.run(i)
        print('nodes added')

    def add_interactions_to_graph(self, relationstoadd,node_type_id):
        # Interactions are based on the model
        create_interactions_batch=[]
        for x in range(0,relationstoadd.shape[0]):
            create_interactions="MATCH (a:"+node_type_id+"),(b:"+node_type_id+")"+" WHERE a.Name="+"'"+relationstoadd.Parent[x]+"'"+" AND b.Name="+ "'"+relationstoadd.Child[x]+"'"+ \
                                " CREATE (a)-[r:"+relationstoadd.Type[x]+"]->(b) "+ \
                                "RETURN r"
            create_interactions_batch.append(create_interactions)
        print(create_interactions_batch)
        # restart the session?
        self.create_interactions_batch=create_interactions_batch
        session=self.graph.session()
        for x in create_interactions_batch:
           session.run(x)
        print("Interactions added")


    def add_properties_to_nodes(self, propertiestoadd):
        return None
