def solution(str1, str2):
    str1_list = []
    for i in range(len(str1)-1):
        # 두 글자 모두 알파벳일때
        if ((90 >= ord(str1[i]) >= 65) or (122 >= ord(str1[i]) >= 97)) and ((90 >= ord(str1[i+1]) >= 65) or (122 >= ord(str1[i+1]) >= 97)):
            partial_str = str1[i:i+2]
            str1_list.append(partial_str.lower())
            
    str2_list = []
    for i in range(len(str2)-1):
        # 두 글자 모두 알파벳일때
        if ((90 >= ord(str2[i]) >= 65) or (122 >= ord(str2[i]) >= 97)) and ((90 >= ord(str2[i+1]) >= 65) or (122 >= ord(str2[i+1]) >= 97)):
            partial_str = str2[i:i+2]
            str2_list.append(partial_str.lower())

    union = []
    intersection = []
    unique_value = list(set(str1_list+str2_list))
    
    for value in unique_value:
        values_in_str1 = str1_list.count(value)
        values_in_str2 = str2_list.count(value)
        
        # 합집합 추가
        union.extend(max(values_in_str1, values_in_str2)*[value])

        # 교집합 추가
        if values_in_str1 != 0 and values_in_str2 != 0:
            intersection.extend(min(values_in_str1, values_in_str2)*[value])            
    if len(union) == 0:
        return 65536
    else:
        return int(len(intersection)/len(union) * 65536)