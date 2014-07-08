from setuptools import setup

setup(
	name='ebar2csv',
	version='0.1.0',
	author='smoucka',
	description='Convert ESRI Business Analyst report output to CSV.',
	packages=['ebar2csv'],
	entry_points={
		'console_scripts': [
			'ebar2csv=ebar2csv.ebar2csv:launch',
		],
	},
	install_requires=['lxml>= 3.3.3'],
)