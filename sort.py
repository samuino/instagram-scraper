#Author Details :
# Siam Al Huq
# For further help contact
# Mail : siam.alhuq786@gamil.com
# Git : https://github.com/samuino


import json

class ins:
    def __init__(self,url,like):
        self.url=url
        self.like=like

    def __repr__(self):
        return repr((self.url,self.like))
test = input("enter the name of the user you wanted to scrap data and after the name type .json : ")
with open(test,encoding='utf-8-sig') as f:
    data = json.load(f)


img=[]
for x in data[0:]:
    print (x['images']['standard_resolution']['url'])
    print (x['likes']['count'])
    img.append(ins(x['images']['standard_resolution']['url'],x['likes']['count']))



img=sorted(img,key=lambda object1: object1.like,reverse=True)

for x in img[0:20]:
    print(x.url, x.like)
name=""
for x in test:
    if(x!='.'):
        name+=x
    else:
        name+='.'
        name+='t'
        name+='x'
        name+='t'
        break


f= open(name,'w')
for x in img[0:20]:
    f.write(str(x.like)+"  "+x.url+"\n")
