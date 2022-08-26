#Import the MongoDuty 
from mongoDB import MongoDuty

#Import the Duties from the file (any file name)
from someDuties import *

#Instantiating the class
mongo = MongoDuty()

#Running the duty getUserForLogIn
mongo(getUserForLogIn,'exempleUser','EX12345678')