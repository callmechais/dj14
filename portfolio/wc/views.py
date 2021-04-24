from django.shortcuts import render
import operator,re

def home(request):
    return render(request, 'word.html',{"counttext":"100"})

def wc(request):
    words = request.GET['fulltext']
    words=re.sub(r"(\w*)\W*(\w*)",r"\1 \2",words)
    wordlist = words.split(" ")
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1

    sortword=sorted(worddict.items(), key=operator.itemgetter(1),reverse=True)
    print(sortword)
    return render(request, 'count.html',
                  {"words":words,
                   "worddict":sortword,
                   "len":len(wordlist)
                   })

def help(request):
    return render(request, 'help.html')