from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        hand.sort()
        hand_counts = Counter(hand)

        for hands in hand:
            if hand_counts[hands]:
                for i in range(hands, hands + groupSize):
                    if not hand_counts[i]:
                        return False
                    hand_counts[i] -= 1
        return True


        #     group = [] 
        #     if hand[i] <= hands <= hand[i + groupSize -1]:
        #         group.append(hands)
        #     if len(group) == groupSize:
        #         for x in group:
        #             hand_counts[x]-=1 
        # if hand_counts.values() == 0:
        #     return True
        # return False 







        