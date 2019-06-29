import pickle
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
muncul = {}
for huruf in alfabet:
    muncul[huruf]=0

daftarkata = pickle.load(open("kata.p","rb"))

def count(word, char):
  hit = 0
  for c in word:
    hit += (char == c)
  return hit

for kata in daftarkata :
    for huruf in alfabet:
        muncul[huruf] += count(kata,huruf)

prop = []
total = 0

for huruf in muncul :
    total+=muncul[huruf]

for huruf in alfabet:
    prop.append(muncul[huruf]*1.0/total)


