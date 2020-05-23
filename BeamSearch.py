import StringDouble
import ExtractGraph
import heapq
import math

class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        g = self.graph
        sentence = pre_words
        probability = 0.0
        sentence_len = len(sentence.split())
        heap = [(probability, sentence)]
        while sentence_len < maxToken:
            new_heap = []
            for prev_prob, s in heap:
                l = len(s.split())
                wrd = s.split()[l - 1]
                if wrd == "</s>":
                    # if the end of the sentence is detected, directly add to heap
                    if len(new_heap) == beamK:
                        heapq.heappushpop(new_heap, (prev_prob, s))
                    else:
                        heapq.heappush(new_heap, (prev_prob, s))
                else:
                    #if not the end of the sentence, compute the score and add to heap
                    next_words = g.graph.get(wrd)
                    for word, prob in next_words.items():
                        score = (1 / (math.pow(abs(l), param_lambda))) * (prev_prob + math.log(prob))
                        # add score and prefix to the heap, if heap length is greater than the beam width
                        #pop the lowest score from the heao
                        if len(new_heap) == beamK:
                            heapq.heappushpop(new_heap, (score, str(s + " " + word)))
                        else:
                            heapq.heappush(new_heap, (score, str(s + " " + word)))

            sentence_len += 1
            heap = new_heap
        probability, sentence = sorted(heap, reverse=True)[0]
        return StringDouble.StringDouble(sentence, probability)

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        sentence = ""
        probability = 0.0
        sentence_probability = self.beamSearchV2(pre_words, beamK, 0.0, maxToken)
        sentence = sentence_probability.string
        probability = sentence_probability.score
        return StringDouble.StringDouble(sentence, probability)