

#encoded.txt파일을 열어 encoded라는 변수에 저장
f=open('./encoded.txt','r')
encoded=f.read()
f.close()

afterjs=[] #전사완료된 자음,모음 저장을 위한 리스트 선언
#encoded 변수의 내용을 전사
word=encoded.split() #자음,모음 단위로 잘라 리스트로 저장
print('입력한 암호: ',word)


fullword=[] #완성된 단어를 위한 리스트 선언
for i in word: #리스트 안의 자음,모음의 수만큼 반복
    wordsplit=list(i) #알파벳 단위로 자름
    for k in wordsplit: #본격적인 전사과정
        if 'A' in k:
            k=k.replace('A','U') #A를 U로 전사해 변수에 저장
        if 'G' in k:
            k=k.replace('G','C') #전사해 변수에 저장
        elif 'C' in k:
            k=k.replace('C','G') #전사해 변수에 저장
        if 'T' in k:
            k=k.replace('T','A') #전사해 변수에 저장
        fullword.append(k)
        resultword="".join(fullword)
    fullword=[]
    afterjs.append(resultword)  # afterjs 리스트에 전사된 변수를 추가
print('전사된 암호: ',afterjs)

#암호해독과정 시작
finalresult=[] #최종결과를 담는 리스트 생성

#번역표를 if else문으로  해석
for z in afterjs:
    if z=='UUU' or z=='UUC':
        result='ㅍ'
    elif z=='UUA' or z=='UUG' or z=='CUU' or z=='CUC' or z=='CUA':
        result='ㄱ'
    elif z=='CUG':
        result='ㄴ'
    elif z=='AUU' or z=='AUC' or z=='AUA':
        result='ㅂ'
    elif z=='AUG':
        result='ㅛ'
    elif z=='GUU' or z=='GUC' or z=='GUA' or z=='GUG':
        result='ㅔ'
    elif z=='UCU' or z=='UCC' or z=='UCA' or z=='UGG':
        result='ㄹ'
    elif z=='CCU' or z=='CCC':
        result='ㅅ'
    elif z=='CCA' or z=='CCG':
        result='ㄷ'
    elif z=='ACU' or z=='ACC':
        result='ㅎ'
    elif z=='ACA' or z=='ACG':
        result='ㅒ'
    elif z=='GCU' or z=='GCC':
        result='ㅗ'
    elif z=='GCA'  or z=='GCG':
        result='ㅐ'
    elif z=='UAU'  or z=='UAC':
        result='ㅠ'
    elif z=='UAA' or z=='UAG':
        result='?'
    elif z=='CAU' or z=='CAC':
        result='ㅜ'
    elif z=='CAA' or z=='CAG':
        result='-'
    elif z=='AAU' or z=='AAC':
        result='ㅏ'
    elif z=='AAA' or z=='AAG':
        result='ㅣ'
    elif z=='GAU' or z=='GAC':
        result='ㅁ'
    elif z=='GAA' or z=='GAG':
        result='ㅈ'
    elif z=='UGU' or z=='UGC':
        result='ㅊ'
    elif z=='UGA' or z=='UGG':
        result='ㅋ'
    elif z=="CGU" or z=='CGC':
        result='ㅕ'
    elif z=='CGA' or z=='CGG':
        result='ㅖ'
    elif z=='AGU' or z=='AGC':
        result='ㅌ'
    elif z=='AGA' or z=='AGG':
        result='ㅇ'
    elif z=='GGU' or z=='GGC':
        result='ㅓ'
    elif z=='GGA' or z=='GGG':
        result='ㅑ'
    #만약 이중에 없는 단어 일경우 -> 에러 -> null로 표시
    else:
        result='{NULL}'

    finalresult.append(result)
print('해독된 암호: ',finalresult)