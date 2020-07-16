import pytest
from minion_set import MinionSet

def test_initilization(excluded_tribe='Demons'):
    global pool 
    pool = MinionSet(excluded_tribe)
    size_of_pools = [0]*6
    for tribe in pool.TRIBES:
        units = pool.UNITS_BY_TRIBE[tribe]
        for tier in range(len(units)):
            size_of_pools[tier] += len(units[tier]) * pool.QUANTITIES_PER_TIER[tier]
    total_size = 0
    for i in range(len(size_of_pools)):
        size = size_of_pools[i]
        print(size)
        total_size = total_size + size

    assert total_size == pool.size()

def test_full_flow():
    tiers = [1,2,3,4,5,6]
    sizes = [3,4,4,5,5,6]

    batches = []

    for index in range(6):
        previous_pool_size = pool.size()
        size = sizes[index]
        tier = tiers[index]
        batch = pool.get_batch_of_minions(tavern_tier=tier,batch_size=size)

        assert len(batch) == size

        assert previous_pool_size - size == pool.size()

        for minion in batch:
            print(minion)
            minion_tier = int(minion[0])
            assert minion_tier <= tier

        batches.append(batch)

    for b in batches:
        pool.put_batch_of_minions_back_in_pool(b)

def test_get_batch_for_speed_set(benchmark):
    benchmark(get_batch_for_speed_helper)


def get_batch_for_speed_helper():
    batch = pool.get_batch_of_minions(tavern_tier=1,batch_size=3)
    pool.put_batch_of_minions_back_in_pool(batch)

