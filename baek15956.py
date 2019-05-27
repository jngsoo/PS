'''
 festival==kakao&&festival==2018&&haha==123456&&hoho!=123456
 festival==2018&&kakao==2018&&haha==123456&&hoho!=haha
 
 kakaocodefestival==-20180804&&hello!=-20180804
 kakaocodefestival==-20180804&&hello!=-20180804
 
 a==b&&b==c&&c==a
 a==b&&a==c
 
 int==float
 int==float
 
 a==A&&B==b
 A==a&&b==B
 '''

def find_min_max_str(la,lb):
    min = la[0]
    max = la[0]
    for i in la[1:]+lb:
        if len(i)<len(min):
            min = i
        elif len(i) > len(max):
            max = i
    return min,max

    
# a = ['1','23','456']
# b = ['23','5','6789']

# print(find_min_max_str(a,b))

q_for_equal = []

S = input()

split_and = S.split("&&")
print(split_and)

split_equal = []
# split_and = ['festival==kakao', 'festival==2018', 'haha==123456', 'hoho!=123456']
for i in split_and:
    split_equal.append(i.split("=="))
    if '==' in i:
        q_for_equal.append('==')


for i in range(len(split_equal)):
    if len(split_equal[i])==1:
        x,y = split_equal[i][0].split("!=")
        split_equal[i] = []
        split_equal[i].append(x)
        split_equal[i].append(y)
        q_for_equal.append('!=')

print(split_equal)

# split_equal = [['festival', 'kakao'], ['festival', '2018'], ['haha', '123456'], ['hoho', '123456']]
for i in range(len(split_equal)-1):
    if (split_equal[i][0] in split_equal[i+1]) or (split_equal[i][1] in split_equal[i+1]):
        min_str, max_str = find_min_max_str(split_equal[i],split_equal[i+1])

        for j in range(2):
            if split_equal[i][j] == max_str:
                if min_str not in split_equal[i]:
                    split_equal[i][j] = split_equal[i][j].replace(split_equal[i][j],min_str)
            elif split_equal[i+1][j] == max_str:
                if min_str not in split_equal[i+1]:
                    split_equal[i+1][j] = split_equal[i+1][j].replace(split_equal[i+1][j],min_str)

        
print(split_equal)

print(q_for_equal)


