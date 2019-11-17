class posts():
	def __init__(self,user,content):
		self.user=user
		self.content=content

class user():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.list1=[]
		self.list2=[]
	def add_friend(self,email):
		self.list1.append(email)

		print(self.name+" has added " + email +" as a friend")
	def remove_friend(self,email):
		self.list1.remove(email)
		print(self.name+" has removed "+email+" from friends")
	def add_post(self,text):
		self.list2.append(posts(self.name,text))
		print(self.name+" has posted: "+text)
	def get_userInfo(self):
		print("name: "+self.name)
		print("email: "+self.email)
		print("password: "+self.password)
		print("friends: "+str( self.list1))
		print("post: "+ str(self.list2))
#------------------------------------------------------------------------------------------------------#
adam=user("adam","adam@gmail.com","adam123")                                                           #
adam.add_friend("ahmad@gmail.com")                                                                     #
adam.add_friend("osama@gmail.com")                                                                     #
adam.remove_friend("ahmad@gmail.com")                                                                  #
adam.add_post("test1 test test1")                                                                      #
adam.add_post("diffrent post")                                                                         #     
adam.get_userInfo()                                                                                    #
#------------------------------------------------------------------------------------------------------#
yazan=user("yazan","yazan@gmail.com","yazan123")                                                       #
yazan.add_friend("osama@gmail.com")                                                                    #
yazan.add_friend("ahhmad@gmail.com")                                                                   #
yazan.remove_friend("osama@gmail.com")                                                                 #
yazan.add_post("mma for ever")                                                                         #
yazan.get_userInfo()                                                                                   #
#------------------------------------------------------------------------------------------------------#
