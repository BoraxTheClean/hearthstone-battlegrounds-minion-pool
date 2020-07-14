import pytest
from minion_pool import MinionPool

def test_initilization(excluded_tribe='Demons'):
    pool = MinionPool(excluded_tribe)
    size_of_pools = [0]*6
    for tribe in pool.TRIBES:
        units = pool.UNITS_BY_TRIBE[tribe]
        for tier in range(len(units)):
            size_of_pools[tier] += len(units[tier]) * pool.QUANTITIES_PER_TIER[tier]

    for i in range(len(size_of_pools)):
        size = size_of_pools[i]
        print(size)
        assert len(pool.pool[i]) == size


