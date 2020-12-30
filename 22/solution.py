def part2(player1_cards, player2_cards):
    def play_game(p1_cards, p2_cards):
        cache_p1 = [p1_cards.copy()]
        cache_p2 = [p2_cards.copy()]
        while len(p1_cards) and len(p2_cards):
            if cache_p1.count(p1_cards) > 1 or cache_p2.count(p2_cards) > 1:
                return 'Player 1'
            p1_card = p1_cards.pop(0)
            p2_card = p2_cards.pop(0)
            if p1_card <= len(p1_cards) and p2_card <= len(p2_cards):
                if play_game(p1_cards.copy()[:p1_card], p2_cards.copy()[:p2_card]) == 'Player 1':
                    p1_cards.extend([p1_card, p2_card])
                    cache_p1.append(p1_cards.copy())
                    cache_p2.append(p2_cards.copy())
                else:
                    p2_cards.extend([p2_card, p1_card])
                    cache_p1.append(p1_cards.copy())
                    cache_p2.append(p2_cards.copy())
            else:
                if p1_card > p2_card:
                    p1_cards.extend([p1_card, p2_card])
                    cache_p1.append(p1_cards.copy())
                    cache_p2.append(p2_cards.copy())
                else:
                    p2_cards.extend([p2_card, p1_card])
                    cache_p1.append(p1_cards.copy())
                    cache_p2.append(p2_cards.copy())
        if len(p1_cards):
            return 'Player 1'
        else:
            return 'Player 2'

    if play_game(player1_cards, player2_cards) == 'Player 1':
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(player1_cards.__reversed__())))
    else:
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(player2_cards.__reversed__())))


def part1(player1_cards, player2_cards):
    while len(player1_cards) and len(player2_cards):
        player1_card = player1_cards.pop(0)
        player2_card = player2_cards.pop(0)
        if player1_card > player2_card:
            player1_cards.extend([player1_card, player2_card])
        else:
            player2_cards.extend([player2_card, player1_card])
    if len(player1_cards):
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(player1_cards.__reversed__())))
    else:
        return sum(map(lambda x: (x[0] + 1) * x[1], enumerate(player2_cards.__reversed__())))


def parse(data):
    player1_cards = []
    player2_cards = []
    player_separation = data.index('')
    for i in range(1, player_separation):
        player1_cards.append(int(data[i]))
    for i in range(player_separation + 2, len(data)):
        player2_cards.append(int(data[i]))
    return player1_cards, player2_cards


if __name__ == '__main__':
    player1, player2 = parse([line.strip() for line in open('data.txt')])
    print('Part 1', part1(player1.copy(), player2.copy()))
    print('Part 2', part2(player1.copy(), player2.copy()))
