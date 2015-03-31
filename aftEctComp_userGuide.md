# *aftEctComp.py* User guide
##### David Pattinson

aftEctComp.py does AFT-ECT comparisons as described in:

- Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. **Phylogeny, paleontology, and primates: do incomplete fossils bias the tree of life?** *Systematic Biology.* doi:10.5061/dryad.tk87q

## Installation

Written and tested in Python 2.7.8 (but may work in others). Go [here](https://www.python.org/downloads/) to download Python and for information on it’s installation.

You will need to install [DendroPy](https://pythonhosted.org/DendroPy/).

## Inputs

Look in the example data folder.

- 'ECT.txt' contains an example ECT (from the reference above):

`(Dermoptera,Tupaia,(((((Alouatta,(Aotus,(Cebus,Saimiri))),Callicebus),(((Chlorocebus,Macaca),Colobus),(Hylobates,Pan))),Tarsius),((((Arctocebus,Perodicticus),(Loris,Nycticebus)),(Galago,Otolemur)),(((((Cheirogaleus,Microcebus),Lepilemur),Propithecus),(Lemur,Varecia)),Daubentonia))))`

- 'AFTsample.txt' contains AFTs for three templates (again from the reference above). An example line is:

`Absarokius	Alouatta	(Dermoptera,Tupaia,((((Alouatta,((Aotus,(Cebus,Saimiri)),Callicebus)),(((Chlorocebus,Macaca),Colobus),(Hylobates,Pan))),Tarsius),((((Arctocebus,Perodicticus),(Loris,Nycticebus)),(Galago,Otolemur)),(((((Cheirogaleus,Microcebus),Lepilemur),Propithecus),(Lemur,Varecia)),Daubentonia))));`

This is a tab delimited line. The first field is the template (`Absarokius`), the second field is the subject (`Alouatta`), and the final field is a newick format AFT.

## Usage

`python aftEctComp.py -h` brings up basic usage:

~~~
usage: aftEctComp.py [-h] -e ECT -a AFT -n NTAX

This script conducts AFT-ECT comparisons. For a given AFT-ECT pair it returns:
(A) ECT clades absent from the AFT, (B) n clades lost due to poor resolution
(PR), and (C) n clades lost due to topological rearrangement (TR).

optional arguments:
  -h, --help            show this help message and exit
  -e ECT, --ECT ECT     Single line file containing ECT. E.g.:
                        (Alouatta,(Aotus,(Cebus,Saimiri)))
  -a AFT, --AFT AFT     File containing (list of) AFTs.
  -n NTAX, --nTax NTAX  The number of taxa in the trees.
~~~~

To run the script on the example data (having cloned and changed directory into this repository):

`python aftEctComp.py -e example_data/ECT.txt -a example_data/AFTsample.txt -n 26`

## Outputs

`AFTECTcomparisons.txt` is a tab delimited file. Each line contains data for one AFT-ECT comparison. The headings are self-explanatory except PR (which is the number of ECT clades absent from the AFT due to poor resolution) and TR (which is the number of ECT clades absent from the AFT due to topological rearrangement).

`templateAverages.txt` contains the average number of ECT clades absent from each AFT for each template.
