import logging

import psycopg2
import psycopg2.extensions
from creativiousUtilities.logging import Logger
import mysql.connector
import uuid

# @DeprecationWarning
# class PostsqeSQLController:
#     def __init__(self, dbname: str = "postgres", host: str = "localhost", port: int = 5432, user: str = "postgres", password: str = "Temp1234!"):
#         """Provides interface with PostgreSQL type databases with easy access without needing to use SQL language
#         Currently only supports Asynchronous type connections"""
#         self.dbname: str = dbname
#         self.logger = Logger(name="SQLController", subname=dbname, debug=False).getLogger()
#         self.logger.debug("SQLController Object Created")
#         self.__connectionInfo = {
#             "dbname": dbname,
#             "host": "localhost",
#             "port": port,
#             "user": user,
#             "password": password
#
#         }
#         self.connection: psycopg2.extensions.connection = None
#         self.cursor: psycopg2.extensions.cursor = None
#         self.__connected:bool = False
#         self.__connect()
#     def __connect(self):
#         self.logger.debug(f"Attempting connection to Database ({str(self.dbname)})")
#         if not self.__connected:
#             try:
#                 self.connection = psycopg2.connect(
#                     dbname = self.__connectionInfo["dbname"],
#                     host = self.__connectionInfo["host"],
#                     port = self.__connectionInfo["port"],
#                     user = self.__connectionInfo["user"],
#                     password = self.__connectionInfo["password"]
#                 )
#                 self.__connected = True
#                 self.cursor = self.connection.cursor()
#                 self.logger.debug(f"Established successful connection to Database ({str(self.dbname)})")
#             except Exception as e:
#                 logging.error(str(e))
#         else:
#             self.logger.warning(f"Attempted to connect to Database ({str(self.dbname)}) but already connected!")
#
#     def shutdown(self):
#         if self.__connected:
#             try:
#                 self.cursor.close()
#                 self.connection.close()
#                 self.logger.debug("Turned off SQL Connection and Cursor!")
#             except Exception as e:
#                 logging.error(str(e))
#
#     def createTable(self, name):
#         pass
#
#     class Table:
#         def __init__(self, name):
#             self.name = name



class MySQL:
    def __init__(self):
        self.connections = {

        }
        self.__connection_template = {"object": None}
        pass
    def connect(self, host: str, user: str, password: str, database: str, port: int = 3306):
        ID = str(uuid.uuid4().int)
        connection = {}
        connection["object"] = mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)
        self.connections[ID] = connection
        return self.connections[ID]






