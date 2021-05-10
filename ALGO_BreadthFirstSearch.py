
import DST_Graph
import DST_Queue


# 词梯问题
def BuildWordGraph(file):
    with open(file) as f:
        word_data = f.readlines()

    buckets = {}
    for line in word_data:
        for i in range(len(line)-1):
            bucket = line[:i] + '_' + line[i+1:]
            if bucket not in buckets.keys():
                buckets[bucket] = []
                buckets[bucket].append(line[:-1])
            else:
                buckets[bucket].append(line[:-1])

    word_graph = DST_Graph.Graph()
    for word_key in buckets.keys():
        for word1 in buckets[word_key]:
            if word1 not in word_graph:
                word_graph.AddNode(word1)
            for word2 in buckets[word_key]:
                if word2 not in word_graph:
                    word_graph.AddNode(word2)
                if word1 != word2:
                    word_graph.AddEdge(word1, word2, weight=None)

    return word_graph


def BreadthFirstSearch(word_graph):
    q = DST_Queue.queue_test()
    for idx, word_item in enumerate(word_graph):
        q.push(word_item)

        word_item.state = 0
        word_item.dis = 0
        word_item.pre = None
        # SetState(word_item, 0)
        # SetDistance(word_item, 0)
        # SetPre(word_item, None)

        if q is not None:
            word_item.state = 1
            for qnext_item in q.pop().GetAdjIDs:            # 获取所有邻节点
                qnext_item.setColor(0)
                # SetState(qnext_item, 0)
            for qnext_item in q.pop().GetAdjIDs:  # 获取所有邻节点
                if qnext_item.state == 0:           # 邻节点未探索
                    q.push(qnext_item)

                    qnext_item.state = 1
                    qnext_item.dis += 1
                    qnext_item.pre = word_item
                    # SetState(qnext_item, 1)
                    # SetDistance(qnext_item, idx+1)          # 距离加1
                    # SetPre(qnext_item, word_item)           # 设置qnext_item的前驱节点为word_item

            word_item.state = 2

    return word_graph


def transverse(node):

    pass


if __name__ == '__main__':

    BuildWordGraph('./datasets/fourletterwords.txt')
