import sys

class Cards:
    '''This class store the information about cards rank and suit'''
    def __init__(self,rank,suit):
        '''This method initialize the class with rank and suit'''
        self.rank = rank
        self.suit = suit

    def __ls__(self, other):
        if isinstance(other, Cards):
            return self.rank < other.rank and self.suit <= other.suit
        else:
            return 'Both must be same data type'

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

    def append(self,obj):
        self.records.append(obj)
    
    def sorted_index(self, rank, suit):
        card = Cards(rank, suit)
        len_of_records = len(self.records)
        if len_of_records == 0:
            self.records.append(card)
            return 'Data Added'

        start = 0
        end = len_of_records - 1
        mid = (start + end) // 2
        while start <= end:
            mid = (start + end) // 2
            if self.records[mid].rank == rank and self.records[mid].suit == suit:
                return 'Duplicate Entry, Data already exist'
            elif rank < self.records[mid].rank and suit <= self.records[mid].suit:
                end = mid - 1
            else:
                start = mid + 1
        if rank < self.records[mid].rank and suit <= self.records[mid].suit:
            self.records.insert(mid, card)
        else:
            self.records.insert(mid+1, card)

    def __str__(self):
        string = ''
        for record in self.records:
            string += f'{Cards.__str__(record)}\n'
        return string


c1 = Cards(3, 'Diamond')
lst = DeckOfCards()
c2 = Cards(1, 'Diamond')
lst.append(c2)
lst.append(c1)
lst.sorted_index(2, 'Diamond')
print(lst)
