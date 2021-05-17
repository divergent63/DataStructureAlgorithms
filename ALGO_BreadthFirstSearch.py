
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


def BreadthFirstSearch(word_graph, word_item):
    q = DST_Queue.queue_test()

    # for idx, word_item in enumerate(word_graph):
    q.push(word_item)

    word_item.State = 0
    word_item.Dis = 0
    word_item.Pre = None
    # SetState(word_item, 0)
    # SetDistance(word_item, 0)
    # SetPre(word_item, None)

    while q.__sizeof__() > 0:
        word_item.State = 1
        next_node_all = q.pop().GetAdjIDs()
        for qnext_item in list(next_node_all):            # 获取所有邻节点
            word_graph.GetNode(qnext_item).State = 0
            # SetState(qnext_item, 0)
        for qnext_item in list(next_node_all):  # 获取所有邻节点
            if word_graph.GetNode(qnext_item).State == 0:           # 邻节点未探索
                q.push(word_graph.GetNode(qnext_item))

                word_graph.GetNode(qnext_item).State = 1
                word_graph.GetNode(qnext_item).Dis += 1
                word_graph.GetNode(qnext_item).Pre = word_item
                # SetState(qnext_item, 1)
                # SetDistance(qnext_item, idx+1)          # 距离加1
                # SetPre(qnext_item, word_item)           # 设置qnext_item的前驱节点为word_item

                word_item = word_graph.GetNode(qnext_item)

        word_item.State = 2

    return word_graph


def TransversePath(node):
    path_lst = [node.GetVID()]
    while node.Pre is not None:
        path_lst.append(node.Pre.GetVID())
        node = node.Pre
    return path_lst


if __name__ == '__main__':

    word_graph = BuildWordGraph('./datasets/fourletterwords.txt')
    BreadthFirstSearch(word_graph, word_graph.GetNode('ABOS'))
    print(TransversePath(word_graph.GetNode('ACID')))
