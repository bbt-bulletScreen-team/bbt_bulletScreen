import ahocorasick

def bulletCheck(message):
    check=ahocorasick.Automaton()
    orignWds=[]
    aimWds=[]
    with open('unSeenWord.txt',encoding='utf-8') as f:
        for line in f.readlines():
            line=line.strip()
            orignWds.append(str(line))
        for index,word in enumerate(orignWds):
            check.add_word(word,(index,word))
    check.make_automaton()
    for i in check.iter(message):
        wd=i[1][1]
        aimWds.append(wd)
    for x in aimWds:
        text=message.replace(x,'*'*len(x))
    return text

