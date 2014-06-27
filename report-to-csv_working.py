from lxml import etree
import csv, argparse

class ReportParser(object):
	'''
	Parsing logic.
	'''
	
	def main(self):
		ap = argparse.ArgumentParser()
		ap.add_argument('infile', help='XML input file')
		arg = ap.parse_args()
		
		# Create CSV file, writer
		csvfile = open(arg.infile, 'wb')
		csvwriter = csv.writer(csvfile)

		# Namespaces
		ns = {'xs': 'http://www.w3.org/2001/XMLSchema',
			'msprop': 'urn:schemas-microsoft-com:xml-msprop',
			'msdata': 'urn:schemas-microsoft-com:xml-msdata'}

		# List for dataset tag name
		tagnames = []

		# Import xml file and create ElementTree
		tree = etree.parse('data.xml')

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
	
	def xtag(obj):
		'''
		Pass Element.tag method to parse function.
		'''
		return obj.tag
		
	def xtext(obj):
		'''
		Pass Element.text method to parse function.
		'''
		return obj.text

	def parse(iters, method):
		for n in range(0,iters):
			# Create list for row
			row = []
			for t in tagnames:
				for child in tree.xpath('//'+t)[n].getchildren():
					row.append(method(child))
			csvwriter.writerow(row)

def launch():
	parser = ReportParser()
	parser.main()
		
if __name__ == '__main__':
	launch()