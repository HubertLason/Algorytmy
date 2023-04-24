def scal(tab1,tab2,l1,l2):
    tab3=[0]*(l1+l2)
    i=0
    j=0
    k=0

    while i<l1 and j<l2:
        if tab1[i]<tab2[j]:
            tab3[k]=tab1[i]
            k=k+1
            i=i+1
        else:
            tab3[k]=tab2[j]
            k=k+1
            j=j+1

    while i<l1:
        tab3[k]=tab1[i];
        k=k+1
        i=i+1

    while j<l2:
        tab3[k]=tab2[j];
        k=k+1
        j=j+1
    print(tab3)

tab1=[1,3,5,7,21]
tab2=[2,4,6,8,87]
scal(tab1,tab2,len(tab1),l2=len(tab2));