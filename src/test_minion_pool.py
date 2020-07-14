import pytest
from minion_pool import MinionPool

def test_initilization(excluded_tribe='Demons'):
    global pool = MinionPool(excluded_tribe)
    size_of_pools = [0]*6
    for tribe in pool.TRIBES:
        units = pool.UNITS_BY_TRIBE[tribe]
        for tier in range(len(units)):
            size_of_pools[tier] += len(units[tier]) * pool.QUANTITIES_PER_TIER[tier]

    for i in range(len(size_of_pools)):
        size = size_of_pools[i]
        print(size)
        assert len(pool.pool[i]) == size

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

        tier = str(tier)

        for minion in batch:
            assert minion.startswith(tier)

        batches.append(batch)

    for b in batches:
        pool.put_batch_of_minions_back_in_pool(b)

    def test_get_batch_for_speed(benchmark):
        batch = pool.get_batch_of_minions(3,3)

        benchmark(pool.put_batch_of_minions_back_in_pool,batch)

        benchmark(pool.get_batch_of_minions,3,3)
