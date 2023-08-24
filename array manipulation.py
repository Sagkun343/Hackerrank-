def matchingStrings(stringList, queries):
    output_list = []
    for i in range(len(queries)):
        counter = 0
        for k in range(len(stringList)):
            if queries[i] in stringList[k]:
                counter += 1
            if k == len(stringList)-1:
                output_list.append(counter)
    return output_list


print(matchingStrings(["aba",'baba','aba','xzxb'],['aba','xzxb','ab']))