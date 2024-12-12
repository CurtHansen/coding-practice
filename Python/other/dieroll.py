from random import choice

def trial():
    rolls = 0
    while True:
        rolls += 1
        outcome = choice([1,2,3,4,5,6])
        if outcome==2:
            break
        elif outcome%2==1:
            rolls = 0
    return rolls


if __name__ == '__main__':
    ntrials = 1000
    results = []
    for i in range(ntrials):
        results.append(trial())
    print(sum(results)/ntrials)