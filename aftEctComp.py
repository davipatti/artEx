from __future__ import division
import dendropy
import argparse

'''
This script takes:
- an ECT string
- a file containing rows of AFTs
- the number of taxa

It returns for each AFT-ECT comparison:
-the number of ECT clades absent from the AFT
-the number of ECT clades lost due to poor resolution in the AFT
-the number of ECT clades lost due to topological rearrangement

These values were checked against the first dataset analyses (which were done
by eye) and differed in 6.29 percent of cases, which I attribute to human
error in the first analysis.
'''

parser=argparse.ArgumentParser(
    description='This script does AFT-ECT comparisons.'
                'For a given AFT-ECT pair it outputs:'
                ' (A) ECT clades absent from the AFT'
                ' (B) AFT clades absent from the ECT'
                ' (C) n clades lost due to poor resolution (PR), and'
                ' (D) n clades lost due to topological rearrangement (TR).'
                ' NOTE: C and D are with respect to ECT clades absent from '
                ' the AFT\n'
                ' templateAverages.txt also refers to ECT clades absent from'
                ' AFTs.')
parser.add_argument(
    '-e', '--ECT', required=True,
    help='Single line file containing ECT. E.g.:\n'
         '(Alouatta,(Aotus,(Cebus,Saimiri)))')
parser.add_argument(
    '-a', '--AFT', required=True,
    help='File containing (list of) AFTs.')
parser.add_argument(
    '-n', '--nTax', required=True, type=int,
    help='The number of taxa in the trees.')
args=parser.parse_args()

ntaxa = args.nTax

print "Loading ECT:"

# Make ECT
with open(args.ECT) as ECTfileObj:
    ECT_string = ECTfileObj.readline().rstrip().replace(';', '')
ECT = dendropy.Tree.get_from_string(ECT_string, schema='newick')

ECT.print_plot()

ECTstring_openBrackets = ECT_string.count('(')

# Text file for writing AFT-ECT comparisons
AFT_ECT_comparisons = open('AFT-ECTcomparisons.txt', 'w')

# Labels columns
AFT_ECT_comparisons.write('Template\t'
                          'Subject\t'
                          'ECT-clades-absent-from-AFT\t'
                          'AFT-clades-absent-from-ECT\t'
                          'PR\t'
                          'TR\n')

# Template dictionary
template_dict = {}

# Subject counter
subject_counter_dict = {}

with open(args.AFT) as AFTfileObj:
    for line in AFTfileObj:
        split_line = line.split('\t')
        template = split_line[0]
        subject = split_line[1]
        AFTstring = split_line[2].rstrip().replace(';', '')
        print "Comparing %s:%s AFT" % (template, subject)

        # AFT tree object
        AFT = dendropy.Tree.get_from_string(AFTstring, schema='newick')

        # AFT_ECT_comparison
        # false_positives_and_negatives returns a tuple:
        #   - first element is the number of AFT clades not in the ECT
        #   - second element is the number of ECT clades not in the AFT
        false_positives_and_negatives = ECT.false_positives_and_negatives(AFT)
        AFT_clades_absent_from_ECT = false_positives_and_negatives[0]
        ECT_clades_absent_from_AFT = false_positives_and_negatives[1]

        # calculates number of ECT clades lost from AFT due to Poor Resolution 
        # (PR) by subtracting the number of open brackets found in the AFT
        # string from the number expected in a fully resolved topology with
        # ntaxa (=ntaxa - 1)
        AFT_openBrackets = AFTstring.count('(')
        PR = ECTstring_openBrackets - AFT_openBrackets

        # Calculates number of ECT clades lost from AFT due to Topological
        # Rearrangements (TR)
        TR = ECT_clades_absent_from_AFT - PR

        # Writes metric to output file
        AFT_ECT_comparisons.write(template + '\t' + \
                                  subject + '\t' + \
                                  str(ECT_clades_absent_from_AFT) + '\t'+ \
                                  str(AFT_clades_absent_from_ECT) + '\t'+ \
                                  str(PR) + '\t' + \
                                  str(TR) + '\n')

        # Template averages
        # Adds the template to the template dictionary if not already there
        if template not in template_dict:
            template_dict[template] = 0

        # Adds number of ECT clades absent from AFT to template key
        template_dict[template] += ECT_clades_absent_from_AFT

        # Adds the template to the subject counter dictionary if not there
        if template not in subject_counter_dict:
            subject_counter_dict[template] = 0

        # Adds 1 every time a given template is processed to the subject counter
        subject_counter_dict[template] += 1

print "\nAFT-ECT comparisons written to 'AFT-ECTcomparisons.txt'\n"

template_averages = open('templateAverages.txt', 'w')

for template in template_dict:
    template_dict[template] = template_dict[template] / subject_counter_dict[template]
    template_averages.write(template + '\t' + str(template_dict[template]) + '\n')

print "\nAverage number of ECT clades absent from AFT for a given template\n"\
      "written to 'templateAverages.txt'.\n"

AFT_ECT_comparisons.close()
template_averages.close()

print "Done"
