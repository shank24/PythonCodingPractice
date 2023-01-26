import re

str="Paragraphs are the building blocks of papers. " \
    "Many students define paragraphs in terms of length: " \
    "a paragraph is a group of at least five sentences, " \
    "a paragraph is half a page long, etc. " \
    "In reality, though, the unity and coherence " \
    "of ideas among sentences is what constitutes a paragraph. " \
    "A paragraph is defined as " \
    "a group of sentences or a single sentence that forms a unit" \
    "(Lunsford and Connors 116). " \
    "Length and appearance do not determine whether a section " \
    "in a paper is a paragraph. " \
    "For instance, in some styles of writing, " \
    "particularly journalistic styles, " \
    "a paragraph can be just one sentence long." \
    " Ultimately, a paragraph is a sentence or" \
    "group of sentences that support one main idea. " \
    "In this handout, we will refer to this as the controlling idea" \
    "because it controls what happens in the rest of the paragraph."

x = re.search(r"\w{9}", str)
print(x.group())

exact_word=re.search(r"paragraph",str)
print(exact_word.group())

findEx=re.findall(r'\ba',str)
print(findEx)
print(len(findEx))


#Find By Boundary For Paragraph
findBoundaryPara=re.findall(r"\bparagraph",str)
print(findBoundaryPara)
print(len(findBoundaryPara))

findBoundaryThe=re.findall(r"\bthe",str)
print(findBoundaryThe)
print(len(findBoundaryThe))



