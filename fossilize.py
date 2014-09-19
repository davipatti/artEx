'''
                Fossilize

        A script to generate artificial fossils

    When using this program please cite: 
    
        Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. 
        Phylogeny, paleontology, and primates: do incomplete fossils bias the 
        tree of life? Systematic Biology. doi:10.5061/dryad.tk87q

    The MIT License (MIT)
    
    Copyright (c) 2014 Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
'''
import os.path


def processData(template, data_to_alter):
    template_counter, dta_counter = 0, 0
    output_data = ''

    while (template_counter < len(template)):

        if template[template_counter] == '?':
            output_data += '?'

        elif data_to_alter[dta_counter] == '{':
            output_data += '{'
            while data_to_alter[dta_counter] != '}':
                dta_counter += 1
                output_data += data_to_alter[dta_counter]

        else:
            output_data += data_to_alter[dta_counter]

        if template[template_counter] == '{':
            while template[template_counter] != '}':
                template_counter += 1

        if data_to_alter[dta_counter] == '{':
            while data_to_alter[dta_counter] != '}':
                dta_counter += 1

        template_counter += 1
        dta_counter += 1

    return output_data


def getUserInput(prompt):
    user_input = ''

    while len(user_input) == 0:
        user_input = raw_input(prompt)
        if len(user_input) == 0:
            print 'You didn\'t enter anything. '

    return user_input


def parseString(data_string):

    trimmed_string = data_string.strip()

    if '\t' in trimmed_string:
        split = trimmed_string.partition('\t')

    elif '{' in trimmed_string:
        bracket_pos = trimmed_string.find('{')

        if ' ' in trimmed_string[:bracket_pos]:
            split = trimmed_string.partition(' ')
        else:
            split = ('', '', trimmed_string)

    else:
        split = trimmed_string.partition(' ')

    if split[1] != '':
        parsed_data = {'name': split[0].strip(), 'data': split[2].strip()}
    else:
        parsed_data = {'name': 'NoNameGiven', 'data': trimmed_string}

    return parsed_data


def doRepeat(prompt):
    answer = raw_input(prompt)

    if answer in ('y', 'yes', 'yep', 'ye'):
        repeat = 1

    elif answer in ('n', 'no', 'nope', 'nah'):
        repeat = 0

    else:
        print 'Well you didn\'t give a useful answer so I\'ll assume you '\
              'meant no.'
        repeat = 0

    return repeat


def checkFile(path):
    full_path = os.path.realpath(path)
    if os.path.isfile(full_path):
        return {'path': full_path, 'error': False}
    else:
        return {'path': full_path, 'error': True}


def mainProgram(temp_filepath='', to_alter_filepath=''):
    repeat = 1

    if temp_filepath == '' and to_alter_filepath == '':
        # run program to accept and output individual strings
        while repeat == 1:
            template_string = getUserInput(
                'Please enter template string (with/without name): ')
            template_data = parseString(template_string)

            to_alter_string = getUserInput(
                'Please enter string to alter (with/without name): ')
            to_alter_data = parseString(to_alter_string)

            output_string = processData(
                template_data['data'], to_alter_data['data'])

            print '\nAltered string:'
            print str(to_alter_data['name']) + '\t' + str(output_string)

            repeat = doRepeat(
                '\nWould you like to run the program again? (y or n) : ')

    else:
        # run program on two files
        template_file = checkFile(temp_filepath)
        to_alter_file = checkFile(to_alter_filepath)

        if template_file['error'] or to_alter_file['error']:
            print 'At least one of the files you entered does not exist, '\
                  'please check the file paths entered.'
        else:
            output_path = os.path.join(
                os.path.dirname(to_alter_file['path']),
                'altered_' + os.path.basename(to_alter_file['path'])
                )

            with open(template_file['path'], 'r') as temp, open(to_alter_file['path'], 'r') as to_alter, open(output_path, 'a', 0) as output_file:
                template_line = temp.readline()
                to_alter_line = to_alter.readline()

                while template_line != '':
                    template_string = parseString(template_line)
                    to_alter_string = parseString(to_alter_line)

                    output_string = processData(
                        template_string['data'], to_alter_string['data'])

                    output_file.write(
                        str(to_alter_string['name'] + '\t'
                            + output_string + '\n'))

                    template_line = temp.readline()
                    to_alter_line = to_alter.readline()

            print 'The program was run in batch mode. '\
                  'Output can be found in', output_path


if __name__ == "__main__":
    import sys
    print "\n\t\t\tFossilize\n\tA script to generate artificial fossils\n\n"\
          "Copyright (C) 2014 Pattinson DJ, Thompson RS, Piotrowski A, Asher "\
          "RJ\n\n"\
          "When using this program please cite:\n\n"\
          "Pattinson DJ, Thompson RS, Piotrowski A, Asher RJ. 2014. "\
          "Phylogeny, paleontology, and primates: do incomplete fossils "\
          "bias the tree of life? Systematic Biology. "\
          "doi:10.5061/dryad.tk87q\n\n"\
          "This program comes with ABSOLUTELY NO WARRANTY. This is free "\
          "software, and you are welcome to redistribute it under certain "\
          "conditions. Please see the source file for more details.\n\n"\
          "----------"


    if len(sys.argv) == 1:
        mainProgram()
    elif len(sys.argv) == 3:
        mainProgram(sys.argv[1], sys.argv[2])
    else:
        print "Start the program with no arguments for manual string "\
              "processing or with the paths of two files containing the template "\
              "strings and strings to alter.\n"
