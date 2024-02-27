import sys

class Cards:
    '''This class store the information about cards rank and suit'''
    def __init__(self,rank,suit):
        '''This method initialize the class with rank and suit'''
        self.rank = rank
        self.suit = suit

    def __str__(self):
        '''This is how it will print'''
        if self.rank == 1:
            rank = 'A'
        elif self.rank == 11:
            rank = 'J'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 13:
            rank = 'K'
        else:
            rank = self.rank
        return f'{self.suit} of {rank}'

class DeckOfCards:
    def __init__(self):
        self.records = list()
    
    def sorted_index(self, rank, suit):
        card = Cards(rank, suit)
        len_of_records = len(self.records)
        if len_of_records == 0:
            self.records.append(card)

    def __str__(self):
        string = ''
        for record in self.records:
            string += f'{Cards.__str__(record)}\n'
        return string
