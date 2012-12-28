class Paginator(object):	
	def __init__(self,items,items_per_page):
		self.items = items
		self.items_per_page = items_per_page

	
	def total_pages(self,items,items_per_page):

		if len(self.items)<self.items_per_page and len(self.items)>1:
			print "1 per page"		
		
		elif len(self.items)==0:
			print "empty"		
		elif len(self.items)%self.items_per_page==0:
			print len(self.items)/self.items_per_page
		else:
			print (len(self.items)/self.items_per_page)+1
			
			


	def total_items(self):
		length=len(self.items)
		print length

	def previous_page(self):
		pass 

	def next_page(self):
		pass

	def page_items(self,page_no,items,items_per_page):
		print mylist
		for ind,itm in enumerate(mylist):
			print("x["+str(ind)+"]="+str(itm)) 
mylist=[]					
page=Paginator(mylist,3)
page.total_pages(mylist,5)
page.total_items()
page.page_items(2,mylist,10)


