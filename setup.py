from setuptools import setup

setup(
	name='esri-ba-report-to-csv',
	version='0.1.0',
	author='smoucka',
	description='Convert ESRI Business Analyst report output to CSV.',
	packages=['esri-ba-report-to-csv'],
	entry_points={
		'console_scripts': [
			'esri-ba-report-to-csv = esri-ba-report-to-csv.esri-ba-report-to-csv:launch',
		]
	},
	install_requires=['lxml>= 3.3.3'],
)