class Paginator(object):	
	def __init__(self,items,items_per_page):
		self.items = items
		self.items_per_page = items_per_page

	
	def total_pages(self):

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

	def page_items(self):
		pass
mylist=[1,2,3,4,56]					
page=Paginator(mylist,8)
page.total_pages()
page.total_items()
page.page_items()


