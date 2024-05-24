class Solution:
    '''
    input: words, maxWidth
    Constraints:
        pack as many words as you can in each line.
        Extra spaces between words should be distributed as evenly as possible.
        For the last line of text, it should be left-justified 
        no extra space is inserted between words.
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        count = 0
        line_len = 0
        start = 0
        result = []

        for i, word in enumerate(words):
            word_len = len(word)
            if line_len + count + word_len <= maxWidth:
                line_len += word_len
                count+=1
            else:
                line = self.format_line(start, count, line_len, maxWidth, words)
                result.append(line)
                start = i
                line_len = word_len
                count = 1
        
        last_line = self.format_last_line(start, words)
        result.append(last_line + ' '*(maxWidth - len(last_line)))

        return result

    def format_line(self, start, count, line_len, maxWidth, words):
        if count == 1:
            return (words[start] + ' '*(maxWidth - line_len))

        
        extra_space = maxWidth - line_len
        space = extra_space // (count-1)
        large_count = extra_space%(count-1)
        i = 1
        line = words[start]

        while i < count:
            if i <= large_count:
                line = line + (space+1)*' ' + words[i+start]
            else:
                line = line + space*' ' + words[i+start]
            
            i+=1

        return line

    def format_last_line(self, start, words):
        return ' '.join(words[start:])

