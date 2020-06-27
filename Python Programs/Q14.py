def addTags(tag,word):
    return "<%s>%s</%s>" % (tag,word,tag)
print(addTags('i','Python'))
print(addTags('b','Python Tutorials'))