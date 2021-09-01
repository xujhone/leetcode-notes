class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # word: status
        # -2: unvisited, -1: unprocessed, >= 0: distance
        status = {word: -2 for word in wordList}

        if endWord not in status:
            return 0

        def findNeighbors(word):
            word = list(word)
            res = []
            for i in range(len(word)):
                tmp = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word[i] = ch
                    tmpWord = ''.join(word)
                    if tmpWord in status:
                        res.append(tmpWord)

                word[i] = tmp

            return res

        beginSet = {beginWord}
        endSet = {endWord}

        status[beginWord] = -1
        status[endWord] = -1

        dist = 1

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            beginSetNext = set()

            for word in beginSet:
                status[word] = dist

                for nbr in findNeighbors(word):
                    if status[nbr] == -2:
                        beginSetNext.add(nbr)
                        status[nbr] = -1
                    elif nbr in endSet:
                        return dist + 1

            beginSet = beginSetNext

            dist += 1

        return 0
