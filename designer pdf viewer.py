def designerPdfViewer(h, word):
    max_height = 0
    for letter in word:
        if h[ord(letter)-97] > max_height:
            max_height = h[ord(letter)-97]
    return max_height * len(word)