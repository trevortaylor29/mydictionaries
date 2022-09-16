codes = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','I':'9',
         'J':'0','K':'=','L':'{','M':'+','N':'-','O':'`','P':'~','Q':'_','R':'[',
         'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'!',
         'b':'@','c':'#','d':'$','e':'%','f':'^','g':'&','h':'*','i':'(','j':')',
         'k':'k','l':'c','m':'d','n':'E','o':'f','p':'G','q':'h','r':'i','s':'j',
         't':'b','u':'L','v':'m','w':'n','x':'o','Y':'p','z':'q'}

infile = open("info_security.txt", "r")
encrypt = open('encrypted.txt', 'w')
readfile=infile.read()

for i in readfile:
    if i in codes:
        encrypt.write(codes[i])
    else:
        encrypt.write(i)

encrypt.close()