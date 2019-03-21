from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlpull
from urllib.request import Request

#Gets the site in html
def site_get(site):
	req = Request(site,headers={'User-Agent': agent})
	webClient = urlpull(req)    #gets page
	site_html = webClient.read()
	webClient.close()
	page_soup = soup(site_html, "html.parser")	#html parser
	return page_soup


site = 'https://www.gsmarena.com/makers.php3'
agent = 'Chrome/35.0.1916.47'

main_soup = site_get(site)
container1 = main_soup.findAll('div',{'class':'st-text'})
container2 = container1[0]
container3 = container2.findAll('a')
container4,sub_site,phone_site = [],[],[]
for i in range(len(container3)):
	container4.append(str(container3[i]))
	sub_site.append('https://www.gsmarena.com/'+container4[i][container4[i].find('"')+1:container4[i].find('"',container4[i].find('"')+1)])
#print(sub_site)
for i in range(len(sub_site)):
	sub_soup = site_get(sub_site[i])
	container1 = sub_soup.findAll('div',{'class':'makers'})
	container2 = container1[0]
	container3 = container2.findAll('a')
	container4 = []
	for j in range(len(container3)):
		container4.append(str(container3[j]))
		phone_site.append('https://www.gsmarena.com/'+container4[j][container4[j].find('"')+1:container4[j].find('"',container4[j].find('"')+1)])

#print(phone_site)
filename = "gsmarena.csv"
f = open(filename,"w")
phone_soup = site_get(phone_site[0])
container1 = phone_soup.findAll('td',{'class':'nfo'}),
container2 = str(container1[-1])
headers = (str(container2[container2.find('=',container2.find('=')+2)+2:container2.find('"',27)]))
for i in range(len(container1)-1):
	container2 = str(container1[i])
	headers.append("," + str(container2[container2.find('=',container2.find('=')+2)+2:container2.find('"',27)]))

print(headers)
#for i in range(len(phone_site)):
	#phone_soup = site_get(phont_site[i])
	#container1 = phone_soup.findAll('td',{'class':'nfo'})
	#for j in range(len(container1)-1):
		#f.write(container1[j].next + ",")
	#f.write(container1[-1].next)