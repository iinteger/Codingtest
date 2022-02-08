def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def make(numbers, numbers_list, target_length, target_numbers, numbers_set):
    # target_length : 새로 만들어질 숫자 길이
    # target_numbers : 새 문자를 이어붙일 기존 숫자 리스트
    temp_list = []
    check_duplicate = []

    for i, target_number in enumerate(target_numbers):
        for j in range(len(numbers)):
            if j not in target_number[1]:
                for k in range(target_length):
                    new_number = target_number[0][:k] + numbers[j] + target_number[0][k + 1:]
                    if int(new_number) not in numbers_set:
                        using_index = target_numbers[i][1] + [j]
                        temp_list.append([new_number, using_index])
                        numbers_set.append(int(new_number))

    numbers_list.append(temp_list)
    return numbers_list, numbers_set


def solution(numbers):
    # numbers_list는 len(numbers)개의 리스트로 이루어져있고
    # 각 리스트는 ["i길이 숫자", [사용된 인덱스]] 로 이루어짐
    numbers_list = []
    # numbers_set은 완성된 숫자들을 중복 없이 저장하는 리스트
    numbers_set = []

    # 1자릿수 숫자를 먼저 초기화
    temp_list = []
    for i in range(len(numbers)):
        temp_list.append([numbers[i], [i]])

        if int(numbers[i]) not in numbers_set:
            numbers_set.append(int(numbers[i]))

    numbers_list.append(temp_list)

    # 가능한 조합의 숫자 생성
    for i in range(1, len(numbers)):
        numbers_list, numbers_set = make(numbers, numbers_list, i + 1, numbers_list[i - 1], numbers_set)

    # numbers_set = []  # 만든 숫자들의 중복 제거
    # for i in range(len(numbers_list)):
    #     for j in range(len(numbers_list[i])):
    #         if int(numbers_list[i][j][0]) not in numbers_set:
    #             numbers_set.append(int(numbers_list[i][j][0]))

    # numbers_set = set([int(i[0]) for each_digit_list in numbers_list for i in each_digit_list])

    prime_count = 0
    for i in numbers_set:
        if is_prime(i):
            prime_count += 1

    return prime_count

# make를 호출할때마다 target_numbers에 아직 사용하지 않은 인덱스의 문자들을 붙이며 새로운 숫자 생성
# 중복에 관계없이 가능한 모든 경우를 생성한 뒤 중복을 제거한 경우 2가지 테스트케이스에서 시간초과
# 아예 숫자를 생성할 때 중복을 체크하며 생성했더니 통과