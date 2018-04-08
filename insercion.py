import logging
logging.basicConfig(filename='insercion.log', level=logging.DEBUG)

def insercion (list) :
  for i in range(1,len(list)) :
    aux=list[i]
    j=i
    while j>0 and list[j-1]>aux :
      list[j]=list[j-1]
      j-=1
    list[j]=aux
  return list
