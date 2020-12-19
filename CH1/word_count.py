class WordCount():
    def openfile(self, fname):
        """
        open a file and force exeption
        """
        try:
            fh = open(fname, 'r')
        except:
            fh = ""
        return fh

    def read_next_line(self, fh):
        try:
            line = fh.readline()
        except:
            line = ''
        return line

    def get_word_with_largest_count(self, line):
        new_line = line.strip()
        word_list = new_line.split(sep=' ')
        dic = dict()
        for word in word_list:
            if word in dic:
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
        biggest = {}
        for word in dic:
            if biggest == {} or dic[word] > biggest_dic[biggest]:
                biggest = word
                biggest_dic = {word: dic[word]}
        return biggest_dic


    def dict_elem(self, word):
        word_key = list(word)[0]
        word_value = word[word_key]
        return word_value

    def check_for_newer_largest_count(self, word, top_word):
        word_value = self.dict_elem(word)
        top_word_value = self.dict_elem(top_word)
        if word_value > top_word_value:
            return word
        else:
            return top_word

print('Begin')

wc = WordCount()
fhand = wc.openfile('words.txt')
biggest_word = {}
for line in fhand:
    next_line = wc.read_next_line(fhand)
    top_word = wc.get_word_with_largest_count(next_line)
    if biggest_word == {}:
        biggest_word = top_word
    else:
        biggest_word = wc.check_for_newer_largest_count(top_word, biggest_word)

print('The word with largest count is:', biggest_word)

print('Done')
