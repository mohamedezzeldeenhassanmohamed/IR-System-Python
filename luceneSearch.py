import subprocess
import os
class luceneSearch:
    def search(self, query):
        os.chdir('Lucene')
        compile_process = subprocess.Popen(
            ['javac', '-cp', 'lucene-analyzers-common-4.2.1.jar;lucene-core-4.2.1.jar;lucene-queryparser-4.2.1.jar',
             'newSearcher.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        compile_output, error1 = compile_process.communicate()

        # print(compile_output.decode())
        # print(error1.decode())

        # run Java program
        run_process = subprocess.Popen(
            ['java', '-cp', '.;lucene-analyzers-common-4.2.1.jar;lucene-core-4.2.1.jar;lucene-queryparser-4.2.1.jar',
             'newSearcher', query], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error2 = run_process.communicate()
        os.chdir('..')
        output = str(output)
        start = output.index('\'')
        if len(output) > 3:
            end = output.index('\'', 3)
        else:
            end = start+1
        output = output[start+1:end]
        return output.split(',')

    @staticmethod
    def print(data):
        data.pop(len(data)-1)
        result = {}
        for index in range(len(data)):
            result[index + 1] = data[index]
        return result

