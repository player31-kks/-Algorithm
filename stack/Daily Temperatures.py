from typing import List

def dailyTemperatures(temperatures: List[int])-> List[int]:
    stack = []
    result =[]
    for current_idx,current_temp in enumerate(temperatures):
        while stack and stack[-1][1] < current_temp:
            idx,temp = stack.pop()
            result.append([idx,current_idx-idx])
        stack.append((current_idx,current_temp))

    for idx,value in stack:
        result.append([idx,0])

    return [value for idx,value in result]


if __name__ == '__main__':
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(dailyTemperatures([30,40,50,60]))
    print(dailyTemperatures([30,60,90]))





