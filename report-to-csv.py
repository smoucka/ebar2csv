from lxml import etree
import csv

# xtag and xtext pass .tag and .text methods to parse function
def xtag(obj):
	return obj.tag
	
def xtext(obj):
	return obj.text

def parse(iter, method):
	for n in range(0,iter):
		# Create list for row
		row = []
		for t in tagnames:
			for child in tree.xpath('//'+t)[n].getchildren():
				row.append(method(child))
		csvwriter.writerow(row)

# Create CSV file, writer
csvfile = open('data_out.csv', 'wb')
csvwriter = csv.writer(csvfile)

# Namespaces
ns = {'xs': 'http://www.w3.org/2001/XMLSchema',
	'msprop': 'urn:schemas-microsoft-com:xml-msprop',
	'msdata': 'urn:schemas-microsoft-com:xml-msdata'}

# List for dataset tag name
tagnames = []

# Import xml file and create ElementTree
tree = etree.parse('kish_data.xml')

# Extract dataset tag names from schema, 
datasets = tree.xpath('//xs:element[@msprop:ImageColumns=""]', namespaces=ns)
for each in datasets:
	tagnames.append(each.get('name'))

#Get number of markets using first dataset
mkt_count = len(tree.xpath('//'+tagnames[0]))

# Access data. First call collects field headings, second collects values
parse(1,xtag)
parse(mkt_count,xtext)

# Close CSV file
csvfile.close()