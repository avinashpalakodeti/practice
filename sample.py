class Paginator(object):
	mylist=[1,2,3,4,5,6,7,8,9,10]	
	def __init__(self,items,items_per_page):
		self.items = items
		self.items_per_page = items_per_page

	
	def total_pages(self):
		print self.items/self.items_per_page


	def total_items(self):
		length=len(self.mylist)
		print length

	def previous_page(self):
		pass 

	def next_page(self):
		pass

	def page_items(self,page_no):
		for items in (self.mylist[:2],self.mylist[2:4],self.mylist[4:6],self.mylist[6:8],self.mylist[8:10]):
			print items
page=Paginator(10,2)
page.total_pages()
page.total_items()
page.page_items(2)


