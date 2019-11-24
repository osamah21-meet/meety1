#------------------------------------------------------------------------------------------------------#
users=[]                                                                                               #
posts=[]                                                                                               #
class Post():                                                                                          #
	def __init__(self,user,content):                                                                   #
		self.user=user                                                                                 #
		self.content=content                                                                           #
class user():                                                                                          #
	def __init__(self,name,email,password):                                                            #
		users.append(self)                                                                             #
		self.name=name                                                                                 #
		self.email=email                                                                               #
		self.password=password                                                                         #
		self.list1=[]                                                                                  #
	def add_friend(self,email):                                                                        #
		self.list1.append(email)                                                                       #
		print(self.name+" has added " + email +" as a friend")                                         #
	def remove_friend(self,email):                                                                     #
		self.list1.remove(email)                                                                       #
		print(self.name+" has removed "+email+" from friends")                                         #
	def add_post(self,text):                                                                           #
		posts.append(Post(self.email,text))                                                            #
		print(self.name+" has posted: "+text)                                                          #
	def get_userInfo(self):                                                                            #
		print("name: "+self.name)                                                                      #
		print("email: "+self.email)                                                                    #
		print("password: "+self.password)                                                              #
		print("friends: "+str( self.list1))                                                            #
		for x in posts:                                                                                #
			if(self.email==x.user):                                                                    #
				print("post: "+ str(x.content))                                                        #
	def __repr__(self):                                                                                #
		return self.name                                                                               #                                             
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
yazan.add_post("x test x")                                                                             #
yazan.get_userInfo()                                                                                   #
#------------------------------------------------------------------------------------------------------#
mo=user("yaza","yaza@gmail.com","yaza123")                                                             #
mo.add_friend("ma@gmail.com")                                                                          #
mo.add_friend("ad@gmail.com")                                                                          #
mo.remove_friend("ma@gmail.com")                                                                       #
mo.add_post("z test z")                                                                                #
mo.get_userInfo()                                                                                      #
#------------------------------------------------------------------------------------------------------#
print(users)                                                                                           #
#------------------------------------------------------------------------------------------------------#