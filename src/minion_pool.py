from random import randint
from interfaces.minion_pool_interface import MinionPoolInterface

class MinionPool(MinionPoolInterface):

    def __init__(self,excluded_tribe):
        if excluded_tribe == 'Neutral':
            raise Exception('Invalid Excluded Tribe, cannot exclude Neutral Minions')
        super().__init__()
        '''
        Inherited from Super:
            self.QUANTITIES_PER_TIER = [16,15,13,11,9,7]

            self.UNITS_BY_TRIBE = { ... }
        '''
        try:
            self.TRIBES.remove(excluded_tribe)
        except:
            raise Exception('Invalid Excluded Tribe')

        self.pool = self._generate_pool()



    def _generate_pool(self):
        #Initialize the pool with 6 empty buckets, one for each tier.
        pool = [[] for i in range(6)]

        for tribe in self.TRIBES: # Pirates, Murlocs, etc...
            units = self.UNITS_BY_TRIBE[tribe] #List of lists. Each list contains units of the given tribe of the same tier.
            for tier in range(len(units)):
                for unit in units[tier]:
                    pool[tier].extend([unit] * self.QUANTITIES_PER_TIER[tier])

        return pool

    def put_batch_of_minions_back_in_pool(self,minions):
        for minion in minions:
            self.put_minion_back_in_pool(minion)

    def put_minion_back_in_pool(self,minion):
        tier = int(minion[0])
        if tier > 6 or tier < 1:
            raise Exception("Invalid Tier")

        self.pool[tier-1].append(minion)

    def size(self):
        size = 0
        for i in self.pool:
            size += len(i)
        return size

    def get_batch_of_minions(self,tavern_tier,batch_size):
        number_of_valid_minions = 0
        for i in range(tavern_tier-1):
            number_of_valid_minions+= len(self.pool[i])


        random_ints = [randint(0,number_of_valid_minions) for i in range(batch_size)]

        minions_to_return = []

        print("Tier: "+str(tavern_tier))
        print("Size: "+str(batch_size))
        print("Random ints: "+str(random_ints))
        
        for rand_int in random_ints:
            current_tier = 0
            while rand_int > len(self.pool[current_tier]) - 1:
                rand_int = rand_int - len(self.pool[current_tier])
                current_tier = current_tier + 1

            selected_minion = self.pool[current_tier][rand_int]

            minions_to_return.append(selected_minion)

            self.pool[current_tier].remove(selected_minion)


        return minions_to_return
