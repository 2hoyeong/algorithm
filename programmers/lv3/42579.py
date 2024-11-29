# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범

def solution(genres, plays):
    answer = []

    famous_genre = dict()
    orgn_chart = list(zip(genres, plays))
    for i in range(len(plays)):
        if genres[i] not in famous_genre:
            famous_genre[genres[i]] = 0
        famous_genre[genres[i]] += plays[i]
    famous_genre = sorted(famous_genre.items(), key=lambda x : x[1], reverse=True)
    chart_idx = sorted([i for i in range(len(orgn_chart))], key=lambda x : orgn_chart[x][1], reverse=True)

    famous_chart = dict()
    for c in chart_idx:
        chart = orgn_chart[c]
        if chart[0] not in famous_chart:
            famous_chart[chart[0]] = []
        famous_chart[chart[0]].append(c)

    for g in famous_genre:
        answer.append(famous_chart[g[0]][:2])

    flattened_answer = [item for sublist in answer for item in sublist]
    answer = flattened_answer

    return answer
