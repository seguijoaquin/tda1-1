def quicksort (list) :
  aux_quicksort(list,0,len(list)-1)
  return list

def aux_quicksort (list,left,right) :
  if left<right :
    pivot=list[(right+left)/2]
    l,r=left,right
    while l<=r :
      while list[l]<pivot : l+=1
      while list[r]>pivot : r-=1
      if l<=r :
        list[l],list[r]=list[r],list[l]
        l+=1
        r-=1
    if left<r : aux_quicksort(list,left,r)
    if l<right : aux_quicksort(list,l,right)
  return list
