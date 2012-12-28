class Paginator(object):
	mylist=[1,2,3,4,5,6,7,8,9,10]	
	def __init__(self,items,items_per_page):
		self.items = items
		self.items_per_page = items_per_page

	
	def total_pages(self):
		if self.items==0:
			print "0 per page"		
		elif self.items%self.items_per_page==0:
			print self.items/self.items_per_page
		else:
			print (self.items/self.items_per_page)+1
		if self.items<self.items_per_page and self.items>1:
			print "1 per page"
			
			


	def total_items(self):
		length=len(self.mylist)
		print length

	def previous_page(self):
		pass 

	def next_page(self):
		pass

	def page_items(self,page_no,mylist):
		print mylist
		for ind,itm in enumerate(mylist):
			print("x["+str(ind)+"]="+str(itm)) 

page=Paginator(100,2)
page.total_pages()
page.total_items()
page.page_items(2,page.mylist)


