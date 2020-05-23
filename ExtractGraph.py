class ExtractGraph:
    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "data\\assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        # Open sentences.txt and read the file
        #with open('assign1_sentences.txt', 'r') as file:
        with open(self.sentences_add, 'r') as file:
            text = file.read()
            words = text.split()
            for i in range(len(words) - 1):
                wrd = words[i]
                nxt_wrd = words[i + 1]
                if wrd == '</s>':
                    continue
                if wrd in self.graph:
                    # already in graph
                    next_words = self.graph.get(wrd)
                    if nxt_wrd in next_words:
                        next_words[nxt_wrd] = next_words.get(nxt_wrd) + 1
                    else:
                        next_words[nxt_wrd] = 1
                else:
                    g = {}
                    g[nxt_wrd] = 1
                    self.graph[wrd] = g
        for wrd in self.graph:
            next_words = self.graph.get(wrd)
            sum = 0
            for nxt_wrd in next_words:
                sum += next_words.get(nxt_wrd)
            for nxt_wrd in next_words:
                next_words[nxt_wrd] = next_words.get(nxt_wrd) / sum

        return

    def getProb(self, head_word, tail_word):
        next_words = self.graph.get(head_word, 0.0)
        if next_words == 0.0:
            return 0.0
        else:
            return next_words.get(tail_word, 0.0)
