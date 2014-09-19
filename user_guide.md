# *Fossilize* User Guide
### Aleks Piotrowski, David Pattinson

Fossilize was written to aid the production of artificial fossils employed in artificial extinction analysis. See the reference below for more details, and cite that reference when using the program:

Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. **Phylogeny, paleontology, and primates: do incomplete fossils bias the tree of life?** *Systematic Biology.* doi:10.5061/dryad.tk87q

Fossilize takes character states from a subject taxon's and modifies them based on data from a template fossil, whereby characters missing (= ‘?’) in the template fossil are treated as missing in the subject taxon.

## Installation

Fossilize was written in Python so can be run on any computer with a recent distribution of Python installed. It was written and tested in version 2.7.8 but may work in others. 

See [here](https://www.python.org/downloads/) to download Python and for information on it’s installation.

## Example data

Example data can be found in the example data folder. These files can be used to run Fossilize in batch mode, or single lines can be extracted for single string processing.

- `morph.txt` contains example subject taxon data
- `template.txt` contains example data for a template fossil
- `altered_morph.txt` is the batch mode’s output if `morph.txt` and `template.txt` are used as the subject and template strings respectively

---

## Usage

The program is command line based and has two modes of operation, manual or batch string processing.

### Manual / Single String Processing

In this mode you input directly the template fossil data and subject taxon data, via the command prompt. The result is then computed and returned output to the user via the command prompt. This mode is best if you just have a few sets of artificial fossils to generate.
Run the file fossilize.py with no arguments:

~~~
>python fossilize.py
~~~

Initially you will see a screen prompting you for a ‘template string’:

~~~
			Fossilize
	A script to generate artificial fossils

Copyright (C) 2014 Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ

When using this program please cite:

Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. Phylogeny, paleontology, and primates: do incomplete fossils bias the tree of life? Systematic Biology. doi:10.5061/dryad.tk87q

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions. Please see the source file for more details.

Please enter template string (with/without name):
~~~

The template string is a string of characters representing your template fossil data.
There are two formats that the program accepts; these are:

Format 1:
<template_string>

e.g.:
1?0???0100??0???????11?0??????????????????????????

Format 2:
<name> <template_string>

e.g.:
Darwinius_masillae 1?0???0100??0???????11?0??????????????????????????

This allows for a name to be included before the template fossil data. The name and template string must be separated by either a single space or tab.
Enter your template fossil data in either of these formats and hit Enter.

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

Here the name is ‘2’ and is separated from the taxon data by a tab.
Polymorphisms must be enclosed within curly braces ‘{}’.
Enter your subject taxon data and hit Enter to proceed.
