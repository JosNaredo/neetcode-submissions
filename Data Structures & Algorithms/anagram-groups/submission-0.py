class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_group = {k:{} for k in range(len(strs))}
        for i, word in enumerate(strs):
            for j in word:
                if main_group[i].get(j) != None:
                    main_group[i][j] += 1
                else:
                    main_group[i][j] = 1

        new_strs = []
        used_index = []
        for i in range(len(strs)):
            temporal_list = []
            if i in used_index:
                continue
            else:
                temporal_list.append(strs[i])
                used_index.append(i)
                for j in range(i+1, len(strs)):
                    if main_group[i] == main_group[j]:
                        temporal_list.append(strs[j])
                        used_index.append(j)
            new_strs.append(temporal_list)

        return new_strs