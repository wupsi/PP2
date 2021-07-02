if os.path.exists('scores.txt'):
    with open('scores.txt') as best_score:
        lines = best_score.readlines()
        num, num1 = '', ''
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if '0' <= lines[i][j] <= '9' and i == 0:
                    num += lines[i][j]
                if '0' <= lines[i][j] <= '9' and i == 1:
                    num1 += lines[i][j]
        num = int(num)
        num1 = int(num1)
        if num < score:
                lines[0] = f'Best score: {score}'
                    lines[1] = f'Score: {score + num1}'
                    with open('scores.txt', 'w') as best:
                        for i in lines:
                            best.write(i)
            else:
                with open('scores.txt', 'w') as best_score:
                    best_score.write(f'Best score: {score}\nScore: {score}')
