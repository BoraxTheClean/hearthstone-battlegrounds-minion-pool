from random import randint
from random import shuffle
from interfaces.minion_pool_interface import MinionPoolInterface

class MinionSet(MinionPoolInterface):

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
        pool = set()

        for tribe in self.TRIBES: # Pirates, Murlocs, etc...
            units = self.UNITS_BY_TRIBE[tribe] #List of lists. Each list contains units of the given tribe of the same tier.
            for tier in range(len(units)):
                for unit in units[tier]:
                    for i in range(self.QUANTITIES_PER_TIER[tier]):
                        size_before = len(pool)
                        pool.add(unit+'-'+str(i))
                        size_after = len(pool)

                        if size_before == size_after:
                            print(unit)
                            print("Duplicate detected")

        return pool

    def put_batch_of_minions_back_in_pool(self,minions):
        for minion in minions:
            self.put_minion_back_in_pool(minion)

    def put_minion_back_in_pool(self,minion):
        self.pool.add(minion)

    def size(self):
        return len(self.pool)

    def get_batch_of_minions(self,tavern_tier,batch_size):
        minions_to_return = []

        while len(minions_to_return) != batch_size:
            element = self.pool.pop()
            if int(element[0]) <= tavern_tier:
                minions_to_return.append(element)
            else:
                self.pool.add(element)

        return minions_to_return
