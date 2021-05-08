
import DST_Graph
import DST_Queue


# 词梯问题
def BuildWordGraph(file):
    with open(file) as f:
        word_data = f.readlines()

    buckets = {}
    for line in word_data:
        for i in range(len(line)):
            bucket = line[:i] + '_' + line[i+1:]
            if bucket not in buckets.keys():
                buckets[bucket] = []
                buckets[bucket].append(line)
            else:
                buckets[bucket].append(line)

    word_graph = DST_Graph.Graph()
    # for word_key in buckets.keys():
    #     for word1 in buckets[word_key]:
    #         if word1 not in word_graph:
    #             word_graph.AddNode(word1)
    #         for word2 in buckets[word_key]:
    #             word_graph.AddEdge(word1, word2, weight=None)
    #
    # return word_graph


if __name__ == '__main__':

    BuildWordGraph('./datasets/fourletterwords.txt')
