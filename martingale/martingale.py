#coding:utf8
import random
import math

WIN  = 1
LOSE = 0

def gambling_50_percent(pocket, pay):
    result = random.randint(0, 1)
    if result == WIN:
        pocket += pay
    else:
        pocket -= pay
    return result, pocket

def play_a_round(win_time_to_stop, pocket, pay, n):
    money_when_start = pocket
    root_pay = pay

    for i in xrange(win_time_to_stop):
        win_or_lose, pocket = gambling_50_percent(pocket, pay)
        if win_or_lose == WIN:
            pay *= n
        else:
            pay = root_pay
            break
    print pocket, pay
    return pocket - money_when_start, pocket > money_when_start

if __name__ == '__main__':
    round_times = 10
    win_times, lose_times = 0, 0
    get_money = 0
    for i in xrange(round_times):
        win_money, snowball = play_a_round(
            win_time_to_stop=4,
            pocket=63,
            pay=1,
            n=2)
        get_money += win_money
        if snowball:
            win_times += 1
        else:
            lose_times += 1
    print "Get: {get_money}, Win: {win_times}/{round_times}, Lose: {lose_times}/{round_times}" \
    .format(**{
        "round_times": round_times,
        "get_money": get_money,
        "win_times": win_times,
        "lose_times": lose_times
    })
