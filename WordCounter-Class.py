import sys


class WordCounter:
    def __init__(self, filename):
        self.filename = filename

    def wordcounter(self):
        try:
            file = open(f'{self.filename}.txt')

        except FileNotFoundError:
            print('Ingresa un archivo valido, o en su caso una ruta valida hacia el archivo')
            sys.exit()

        wordsdic = {}

        for line in file:
            wordlist = line.lower().strip().split(' ')
            for word in wordlist:
                wordsdic[word] = wordsdic.get(word, 0) + 1

        valueslist = dict(sorted(wordsdic.items(), key=lambda item: item[1], reverse=True))
        keys = list(valueslist.keys())

        return keys[:10]


searchFile = input('Ingresa el nombre del archivo de texto: ')

tenwords = WordCounter(searchFile).wordcounter()

print(f'Las 10 palabras más repetidas en el texto son:')
print(*tenwords, sep='\n')
