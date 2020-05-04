# https://programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬
# 찾아라 프로그래밍 마에스터

def solution(nums):
    pokemon = set(nums)
    return min(len(nums) / 2, len(pokemon))