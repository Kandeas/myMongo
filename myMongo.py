from pymongo import MongoClient

class MongoDuty:
	def __new__(cls):
		#Creates a new object
		obj = super().__new__(cls)

		#Set class atributes
		
		#All clientsDB online
		obj.__clientsDb = {}

		#All mongo tasks
		obj.__mongo = {
			'find_one':obj.__Find_One,
			'find':obj.__Find,
			'agregation':obj.__Agregation,
			'insert_one':obj.__Insert_One,
			'insert_many':obj.__Insert_Many,
			'update_one':obj.__UpDate_One,
			'update_many':obj.__UpDate_Many,
			'delete_one':obj.__Delete_One,
			'delete_many':obj.__Delete_Many
		}

		#Return the class method getData when the class is instantiated 
		return obj.__getData

	#This function receives the duty and its variables, runs the task and then returns the data
	def __getData(self, duty, *args):
		#Runs the duty and saves the recive data
		mongoDuty = duty(*args)

		#Clean the parameters
		parameters = {}

		#Checks if the DB has an online connection
		if not mongoDuty['on']['name'] in self.__clientsDb.keys():

			#Creates a new connection if it doesn't already exist
			self.__NewDb(mongoDuty['on'])
		
		#Get the collection from the DB 
		parameters['collection'] = self.__clientsDb[mongoDuty['on']['name']].get_collection(mongoDuty['this']['collection'])
		
		#Checks if the duty has a query
		parameters['query'] = mongoDuty['this']['query'] if 'query' in mongoDuty['this'].keys() else None
		
		#Checks if the duty has any value to insert or update
		parameters['value'] = mongoDuty['this']['value'] if 'value' in mongoDuty['this'].keys() else None

		#Runs the mongo task and saves the recive data
		data = self.__mongo[mongoDuty['do']](parameters)
		
		#Returns the data
		return data if data else None


	#---MONGO TASKS---
	def __NewDb(self, parameters):
		self.__clientsDb[parameters['name']] = MongoClient(parameters['client']).get_database(parameters['name'])
	
	def __Find_One(self, parameters):
		return parameters['collection'].find_one(parameters['query'])

	def __Find(self, parameters):
		return parameters['collection'].find(parameters['query'])

	def __Agregation(self, parameters):
		return parameters['collection'].aggregate(parameters['query'])

	def __Insert_One(self, parameters):
		try:
			return parameters['collection'].insert_one(parameters['value'])
		except:
			pass

	def __Insert_Many(self, parameters):
		try:
			return parameters['collection'].insert_many(parameters['value'])
		except:
			pass

	def __UpDate_One(self, parameters):
		value = {"$set": parameters['value']}
		parameters['collection'].update_one(parameters['query'], value)

	def __UpDate_Many(self, parameters):
		value = {"$set": parameters['value']}
		parameters['collection'].update_many(parameters['query'], value)

	def __Delete_One(self, parameters):
		parameters['collection'].delete_one(parameters['query'])

	def __Delete_Many(self, parameters):
		return parameters['collection'].delete_many(parameters['query'])