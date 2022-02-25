


class TextLoader:
    __path__: str
    __data__: list
    __trimmedChars__: str

    def __init__(self, path: str) -> None:
        
        self.__path__ = path
        self.__trimmedChars__ = ''' ' " ? , ) ( '''

        with open(self.__path__, "r") as f:
            self.__data__ = f.read().split('\n')
        
        self.__parse__()
        for line in self.__data__:
            print(line)
    
    def __parse__(self) -> None:
        self.__data__ = [ line.lower().split('.') for line in self.__data__ if line != "" ]
        self.__data__ = [ word for sentence in self.__data__ for word in (" ".join(sentence)).split(' ') ]
        self.__data__ = [ word.strip(self.__trimmedChars__) for word in self.__data__ if self.__validWord__(word) ]
    
    def __validWord__(self, word: str) -> bool:
        return  word != ""           and \
                not word.isnumeric()  \


    def createVocabulary(self) -> tuple:
        '''
        The method creates word dictionary from word list.
        return type: dictionary of word list, reversed dictionary of word list
        '''
        index = 1
        result = dict()
        reversed_result = dict()
        for word in self.__data__:
            result[word] = index
            reversed_result[index] = word
            index += 1
        return result, reversed_result



Vocabulary: dict = None
ReversedVocabulary: dict = None

## TODO LIST ##
# 1 -> text loader word vector == [[ the, generated, lorem, ipsum, is], ... ]
# 2 -> replace words by their corresponding index in the dictionary == [ [1, 131, 351, 615], ] -> LIST OF LIST
# 3 -> feed word2vec model with the output of the second step
# 4 -> word based vector -> { word: [400d vector] }
# 5 -> find the most similar words for the given input

# -1 -> Wikipedia Word2vec pre-trained model
# word2vec, doc2vec, graph2vec, node2vec

if __name__ == "__main__":

    textLoader = TextLoader("phd_test/dataset/data.txt")
    Vocabulary, ReversedVocabulary = textLoader.createVocabulary()
    print(Vocabulary, ReversedVocabulary)


    # __data__ -> [
    #   [] -> tokenized words that form a sentence
    #   []
    # ]

    #
    # vocab -> flatten __data__ -> [ ... ]
    # {word1: 1, word2: 2 ...}
    # 13: my
    # 51: name
    # --nx.graph -> you are supposed to create skip-gram edges--
    # [[13, 51, 213, 12, 213], ... ]
    # 
    # size of output [ [] ]  will be equal to the size of vocab dictionary
    # element of the output will be n-dimension (word2vec parameter) in terms of length
    # word1: [400d], word2: [400d]

    # cosine similary == semantic similarity


####### EXAMPLE #######
# my name is bahadir | your name is yagmur and you study for phd | she is hardworking and trying for the her best
# my: 1
# name: 2
# is: 3
# bahadir: 4
# your: 5
# yagmur: 6
# and: 7
# study: 8
# for: 9
# phd: 10
# she: 11
# hardworking: 12
# trying: 13
# the: 14
# her: 15
# best: 16

# 1 2 3 4 | 5 2 3 6 7 8 9 10 | 11 3 12 7 13 9 14 15 16
# (1,2), (1,3), (2,1), (2,3), (2,4) (3,1) (3,2) (3,4) (4,2) (4,3)
# sizeOfVocab x ndimension

# 1 2 3 10
# 4 5 6 11
# 7 8 9 12

# [ 0 0 1] X yukardaki max -> [7, 8, 9, 12]
# is: [7, 8, 9, 12]
# my: [1 ,2 ,3 10]
# name: [4, 5, 6, 11]
# cosine_similarity( is, name )
# you are stupıd
