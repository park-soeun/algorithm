def solution(begin, target, words):
    
    queue = []
    visited = [0] * len(words)
    for i in range(len(words)):
        if words[i] == target:
            visited[i] = 1
            queue.append(target)
    if target not in words:
        return 0
    while queue:
        tmp = queue.pop()
        for i in range(len(words)):
            if words[i] == tmp:
                tmp_value = visited[i]
        for i in range(len(words)):
            if visited[i] == 0:
                for j in range(len(target)):
                    if words[i][j + 1:] == tmp[j + 1:] and words[i][:j] == tmp[:j]:
                        visited[i] = tmp_value + 1
                        queue.append(words[i])
                        break
    return max(visited)
    
    
