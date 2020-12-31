
class WordCount():
    
    all_words = dict()

    def openfile(self, fname):
        """
        open a file and force exeption
        """
        try:
            fh = open(fname, 'r')
        except:
            fh = ""
        return fh


    def get_word_with_largest_count(self, line):
        word_list = line.split()
        for word in word_list:
            self.all_words[word] = self.all_words.get(word, 0) + 1
        biggest = {}
        for word in self.all_words:
            if biggest == {} or self.all_words[word] > biggest_dic[biggest]:
                biggest = word
                biggest_dic = {word: self.all_words[word]}
        return biggest_dic


    def dict_elem_value(self, dict_elem):
        word_key = list(dict_elem)[0]
        word_value = dict_elem[word_key]
        return word_value

    def check_for_newer_largest_count(self, word, top_word):
        word_value = self.dict_elem_value(word)
        top_word_value = self.dict_elem_value(top_word)
        if word_value > top_word_value:
            return word
        else:
            return top_word


print('Begin')

wc = WordCount()
fhand = wc.openfile('words.txt')
biggest_word = dict()
count = 0
top_word = ''
for next_line in fhand:
    count = count + 1
    # print(count)
    next_line = next_line.strip()
    if next_line == '': continue
    
    top_word = wc.get_word_with_largest_count(next_line)
    # print(next_line)
    if biggest_word == {}:
        biggest_word = top_word
    else:
        biggest_word = wc.check_for_newer_largest_count(top_word, biggest_word)
        # print(biggest_word)


# print(wc.all_words)
for word, count in biggest_word.items():
    print('The word with largest count is:', word, count)

print('Done')
