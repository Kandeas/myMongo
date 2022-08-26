#---MONGO CONNECTIONS---
'''
> Connections should be described like this:

	<connection_name>:{
		client:<connectString>,
		'name':<db_name>
	}
'''

#An exemple of how to do
connectTo = {
	'myDB':{
		'client':"mongodb+srv://exemple:EX12345678@exempledata.jjv7q.gcp.mongodb.net/exemple_DB?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority",
		'name':'exemple_DB'
	},
}



#---MONGO DUTIES---
'''
> What are mongoDuties?
MongoDuties are functions that encapsulate your mongo queries and 
when called they require all parameters to be properly informed and 
returns a dictionary containing all the information to execute the mongo query.


> MongoDuties should be described like this:

	def mongoDutyName(arg1, arg2, arg...):
		return {
			'on':connectTo[<'someClient'>],
			'do':<'someTaskName'>,
			'this':{
				'collection':<'someColectionName'>,
				'query':{
					<'field1'>:<arg1>,
					<'field2'>:<arg2>
				}
			}
		}
'''

#An exemple of how to do
def getUserForLogIn(user, password):
	return {
		'on':connectTo['myDB'],
		'do':'find_one',
		'this':{
			'collection':'users',
			'query':{
				'userId':user,
				'password':password
			}
		}
	}

