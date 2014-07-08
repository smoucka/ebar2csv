###ebar2csv	[e]sri [b]usiness [a]nalyst [r]eport [2] [csv]
=====================
Parses XML output from a ESRI Business Analyst report to CSV format.

Directory structure to locate XML file:
```
My Output Data
	Projects
		Project_Name
			Reports
				Report_Name
					data.xml
					metadata.xml
					Report_Name.pdf
```

**Installation:**

It is recommended that you use [virtualenv](http://virtualenv.readthedocs.org/en/latest/).

Either download a zipped copy or clone the repo to your local machine.

*While in an active virtual environment!* Jump into the project directory containing setup.py and run the following,
```
python setup.py install
```
Then
```
python setup.py clean --all
```
This second command will remove some of the temporary build files used during the install process. You can also delete the these files,
```
dist
ebar2csv.egg-info
```
At this point, you should be ready to go. Navigate to the location of the XML file you want to parse while still in your active virtualenv. The output CSV will be located in the same directory as your input file.

**Usage:**

```
ebar2csv infile outfile
```
Questions or suggestions? Open an issue.
