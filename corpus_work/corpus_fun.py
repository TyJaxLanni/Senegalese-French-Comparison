from bs4 import BeautifulSoup
import requests



def page_crawler(page_count, no_dups_set):
	#base url
	url = 'http://archives.aps.sn/'

	corpus = []

	#using this to change pages, not smart, but it's what i got
	page_iter_url = url

	#if we're done with the first page, start appending new info to the url
	if page_count>1:
		page_iter_url += "page/" + str(page_count)

	print("*************************************______________________________--************************************************************")
	print("URL: ", url)
	print("ITER URL: ", page_iter_url)
	print("PAGE: ", page_count)
	print("*************************************______________________________--************************************************************")
	
	#make sure this is at zero at each iteration of each page
	article_count = 0
	results = requests.get(page_iter_url)

	doc = BeautifulSoup(results.text, "html.parser")

	articles = doc.findAll('article')
	

	for article in articles:

		bad_bool = False

		#once this reaches 40, it means this is the last article in the page 
		article_count += 1

		art = article.find("a")
		link = art["href"]
		art_url = url + link[1:16]

		art_results = requests.get(art_url)
		art_doc = BeautifulSoup(art_results.text, "html.parser")
		dirty_paragraph = art_doc.find("p").getText().replace("&amp;nbsp", "").replace("\n","").replace("\t","")

		if dirty_paragraph in no_dups:
			print("duplicate!")
			continue
		no_dups.add(dirty_paragraph)
		
		#print(paragraph)
		paragraph = dirty_paragraph.split("&nbsp;")
		start_remove_index = paragraph[0].strip().find("(APS) -")
		end_remove_index = start_remove_index + 8 #+8
		paragraph[0] = paragraph[0].strip()[end_remove_index:]
		for p in paragraph:
			#sentence_count += 1
	
			if len(p) < 3:
				paragraph.remove(p)
				print("----------------------------------------")
				#sentence_count -= 1
				continue
	
			elif p[-1] != ".":
				bad_bool = True
				#sentence_count -= 1
				continue
		
			elif bad_bool == True:
				#sentence_count -= 1
				bad_bool = False
				continue
	
			print(p.strip())
			corpus.append(p.strip())
	
		print("article: ",article_count)
		#print("sentence: ",sentence_count)
		print("page: ",page_count)
	#now we need to go to the next page with another iteration		
		
	return(corpus, no_dups)

#-----------------------------------------------------------------------------------------

sentence_count = 0
page_count = 1
article_count = 0


corpus = []
no_dups = set()

with open("corpus.txt", "w") as f:

	counter = 0

	#while sentence_count < 10000:
	while sentence_count < 15000:
		corpus, no_dups= page_crawler(page_count, no_dups)

		sentence_count += len(corpus)
		print(sentence_count)
		for sentence in corpus:
			if sentence_count < 15000:
				print(sentence, file=f)
		
		#now we need to go to the next page with another iteration		
		page_count += 1
		counter += 1

