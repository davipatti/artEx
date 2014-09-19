# *Fossilize* User Guide
#### Aleks Piotrowski, David Pattinson

Fossilize was written to aid the production of artificial fossils employed in artificial extinction analysis. See the reference below for more details, and cite that reference when using the program.

- Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. **Phylogeny, paleontology, and primates: do incomplete fossils bias the tree of life?** *Systematic Biology.* doi:10.5061/dryad.tk87q

Briefly, Fossilize takes character states from a subject taxon's and modifies them based on data from a template fossil, whereby characters missing (= ‘?’) in the template fossil are treated as missing in the subject taxon.

## Installation

Fossilize was written in Python so can be run on any computer with a recent distribution of Python installed. It was written and tested in version 2.7.8 but may work in others. 

Go [here](https://www.python.org/downloads/) to download Python and for information on it’s installation.

## Example data

Example data can be found in the example data folder. These files can be used to run Fossilize in batch mode, or single lines can be extracted for single string processing.

- `morph.txt` contains example subject taxon data
- `template.txt` contains example data for a template fossil
- `altered_morph.txt` is the batch mode’s output if `morph.txt` and `template.txt` are used as the subject and template strings respectively

## Usage

The program is command line based and has two modes of operation, manual or batch string processing.

### Manual / Single String Processing

In this mode you input directly the template fossil data and subject taxon data via the command prompt. The result is then computed and output to the user via the command prompt. This mode is best if you just have a few sets of artificial fossils to generate.

Run the file fossilize.py with no arguments:

~~~
>python fossilize.py
~~~

You should see a screen prompting you for a ‘template string’:

~~~
			Fossilize
	A script to generate artificial fossils

Copyright (C) 2014 Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ

When using this program please cite:

Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. Phylogeny,
paleontology, and primates: do incomplete fossils bias the tree of life?
Systematic Biology. doi:10.5061/dryad.tk87q

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. Please see the source
file for more details.

----------
Please enter template string (with/without name):
~~~

The template string is a string of characters representing your template fossil data.
There are two formats that the program accepts:

1. (template_string)
 e.g.: `1?0???0100??0???????11?0??????????????????????????`

2. (name) (template_string)
 e.g.: `Darwinius_masillae 1?0???0100??0???????11?0??????????????????????????`

The second allows for a name to be included before the template fossil data. The name and template string must be separated by either a single space or tab. Enter your template fossil data in either of these formats and hit Enter.

Next you will be prompted to enter a string to alter:

~~~
Please enter string to alter (with/without name):
~~~

This is a string containing your subject taxon's data and can take the same formats as the template string (see above).  
Your template string and string to alter must be the same length.
The string to alter might be:

~~~
2	1001200000100100000{1 2}11{0 1}1021200-112{3 4}02112-211112110
~~~

Here the name is `2` and is separated from the taxon data by a tab. Polymorphisms must be enclosed within curly braces `{}`. Enter your subject taxon data and hit Enter.

The altered taxon data is displayed and there is an option of running the program again by entering ‘y’ or ‘n’.

##### Example template, subject and resultant artificial fossils:

Template Fossil	
`Darwinius_masillae	1?0???0100??0???????11?0?????????`

Subject taxon
`2				1001200000100100000{1 2}11{0 1}1021200-11`

Artificial fossil
`2				1?0???0000??0???????11?1?????????`

The altered taxon data which is output will be preceded by the name of the taxon data that was input if a name was provided. In the example above the name `2` was given so is has been included at the beginning of the result.

### Batch /Multiple String Processing

In this mode you provide the program with two files which contain template fossil data (template strings) and taxon data (strings to be altered) respectively. The files should have one string of data, with or without a name at the beginning, per line with no blank lines between strings. Both files must have the same number of strings in, i.e. the same number of lines of text.

The program works through the file containing the template fossil data altering the string on the same line in the file containing the taxon data. The resulting output is saved in a file in the same directory as the file containing the strings it altered.

First create two text files containing your template fossil data and taxon data. The files must have the same number of lines. Each line in the template fossil data file is used as the template fossil data for the taxon data on the corresponding line in the taxon data file. 

See `template.txt` and `morph.txt` in the example data folder for examples of the template and taxon data. Note both files have the same number of lines. Note also that the data on every line in both of the files includes a name. This is not necessary; some or all of the lines may have the names omitted. The purpose of the names is to identify the taxon data that was modified in the resulting output file.

Save these files in the same directory as `fossilize.py`. (This is not compulsory, but makes running the program slightly more straightforward.)

Open a shell and navigate to the directory where `fossilize.py` and the data files are saved.

To run the program in this mode it must be run via the command prompt and given the paths of the files containing the fossil template data and the taxon data, in that order.

For example, on a Windows machine if `fossilize.py` is being run from `C:\Fossilize` and the files containing your data are `C:\Data\template.txt` and `C:\Data\taxon.txt` run:

~~~
C:\Fossilize>python fossilize.py ..\Data\template.txt ..\taxon.txt
~~~

If the files are in the same directory only their file names are needed.

Hit Enter to run the program.

When is finishes it will display a message indicating the name of the newly created file containing the altered taxon data. This is saved in the same directory as the file containing the original taxon data. In this example `altered_taxon.txt` contains the altered data (a copy of which can be found in the example data folder).
