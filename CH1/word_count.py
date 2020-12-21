
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
        new_line = line.strip()
        word_list = new_line.split(sep=' ')
        for word in word_list:
            if word in self.all_words:
                self.all_words[word] = self.all_words[word] + 1
            else:
                self.all_words[word] = 1
        biggest = {}
        for word in self.all_words:
            if biggest == {} or self.all_words[word] > biggest_dic[biggest]:
                biggest = word
                biggest_dic = {word: self.all_words[word]}
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
# fhand = wc.openfile('words.txt')
fhand = wc.openfile('words.txt')
biggest_word = {}
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
print('The word with largest count is:', biggest_word)

print('Done')
