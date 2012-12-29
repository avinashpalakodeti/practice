class Paginator(object):	
	def __init__(self,items,items_per_page,page_no=None):
		self.items = items
		self.items_per_page = items_per_page
		self.page_no = page_no
		#deal with the different data type		
		
		try:  			
			if isinstance(self.items,list):
				print "you have passed list"
			else:
				raise TypeError	
		except TypeError:
			print "please pass list"
			raise SystemExit	
		self.item_count = len(self.items)
	def total_pages(self):
		
		if self.item_count == 0:
			return 0
		elif self.item_count > 1 and self.item_count < self.items_per_page:
			return 1
		elif self.item_count > self.items_per_page:
			pages = self.item_count%self.items_per_page
			page_count = self.item_count/self.items_per_page
			if pages == 0:
				return page_count
			else:
				return page_count+1

	def page_items(self,page_no):
		pass

	""" returns whether next page exists or not """
	def is_next_page(self):
		pass

	""" returns whether previous page exists or not """
	def is_previous_page(self):
		pass
a="dsfds"
page=Paginator(a,5)
page.total_pages()

