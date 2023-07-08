import subprocess
import os
class luceneIndexing:
    def indexing(self):
        file = open('dataset/CISI - Copy.ALL', "r")
        text = file.read()
        file.close()
        docnum = 1
        docs = text.split('.I ')
        docs.pop(0)
        os.chdir('Lucene')
        for doc in docs:
            indxStart = doc.index(".W")
            indxEnd = doc.index(".X")
            content = doc[indxStart + 3:indxEnd].lower()
            if not os.path.exists("lucenedataset"):
                os.makedirs('lucenedataset')

            file = open(f'lucenedataset\\file{docnum}.txt', 'w')
            file.write(content)
            file.close()
            docnum += 1
        compile_process = subprocess.Popen(
            ['javac', '-cp', 'lucene-analyzers-common-4.2.1.jar;lucene-core-4.2.1.jar;lucene-queryparser-4.2.1.jar',
             'newIndex.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        compile_output, error1 = compile_process.communicate()

        # print(compile_output.decode())
        # print(error1.decode())

        # run Java program
        run_process = subprocess.Popen(
            ['java', '-cp', '.;lucene-analyzers-common-4.2.1.jar;lucene-core-4.2.1.jar;lucene-queryparser-4.2.1.jar',
             'newIndex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error2 = run_process.communicate()
        os.chdir('..')

        # print("Output:", output)
        # print("Error:", error2.decode())
# luceneIndexing().indexing()