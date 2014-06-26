from lxml import etree

# Namespaces
ns = {'xs': 'http://www.w3.org/2001/XMLSchema',
	'msprop': 'urn:schemas-microsoft-com:xml-msprop',
	'msdata': 'urn:schemas-microsoft-com:xml-msdata'}
# List for dataset tag name
tagnames = []
# Import xml file and create ElementTree
tree = etree.parse('kish_data.xml')
# 
datasets = tree.xpath('//xs:element[@msprop:ImageColumns=""]', namespaces=ns)
for each in datasets:
	tagnames.append(each.get('name'))

# Get number of markets using first dataset
mkt_count = len(tree.xpath('//'+tagnames[0]))

# Access data
for n in range(0,mkt_count):
	for t in tagnames:
		print tree.xpath('//'+t)[n]