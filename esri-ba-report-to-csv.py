from lxml import etree
import csv, argparse, os

class ReportParser(object):
	'''
	Parsing logic.
	'''
	def __init__(self, args=None):
		'''
		Digest input file argument.
		'''
		ap = argparse.ArgumentParser()
		ap.add_argument('infile', help='XML input file')
		ap.add_argument('outfile', help='Output file name (sans extension)')
		self.args = ap.parse_args()
	
	def main(self):
		'''
		Create output CSV, extract tags/fields and parse XML using lxml.
		'''
		# Create CSV file, writer
		infile_path = os.path.abspath(self.args.infile)
		head, tail = os.path.split(infile_path)
		
		csvfile = open(head + '\\' + self.args.outfile + '.csv', 'wb')
		self.csvwriter = csv.writer(csvfile)

		# Namespaces
		ns = {'xs': 'http://www.w3.org/2001/XMLSchema',
			'msprop': 'urn:schemas-microsoft-com:xml-msprop',
			'msdata': 'urn:schemas-microsoft-com:xml-msdata'}

		# List for dataset tag name
		self.tagnames = []

		# Import xml file and create ElementTree
		self.tree = etree.parse(self.args.infile)

		# Extract dataset tag names from schema 
		datasets = self.tree.xpath('//xs:element[@msprop:ImageColumns=""]', namespaces=ns)
		for each in datasets:
			self.tagnames.append(each.get('name'))

		#Get number of markets using first dataset
		mkt_count = len(self.tree.xpath('//' + self.tagnames[0]))

		# Access data. First call collects field headings, second collects values
		self.parse(1, self.xtag)
		self.parse(mkt_count, self.xtext)

		# Close CSV file
		csvfile.close()
	
	def xtag(self, obj):
		'''
		Pass Element.tag method to parse function.
		'''
		return obj.tag
		
	def xtext(self, obj):
		'''
		Pass Element.text method to parse function.
		'''
		return obj.text

	def parse(self, iters, method):
		'''
		Extract and append iteration
		Extract and append iteration
		'''
		for n in range(0,iters):
			row = []
			for t in self.tagnames:
				for child in self.tree.xpath('//'+t)[n].getchildren():
					row.append(method(child))
			self.csvwriter.writerow(row)

def launch():
	'''
	Launch instance of ReportParser
	
	Entry function for eventual command-line tool
	'''
	parser = ReportParser()
	parser.main()
		
if __name__ == '__main__':
	launch()