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

def test_benchmark_buy_sell_once(benchmark):
    benchmark(buy_sell_helper)

def buy_sell_helper():
    batch = pool.get_batch_of_minions(tavern_tier=4,batch_size=5)
    pool.put_batch_of_minions_back_in_pool(batch)


def test_benchmark_buy_sell_each_tier(benchmark):
    benchmark(test_buy_at_each_tier)


def test_buy_at_each_tier():
    tiers = [1,2,3,4,5,6]
    sizes = [3,4,4,5,5,6]

    batches = []

    for index in range(6):
        size = sizes[index]
        tier = tiers[index]
        batch = pool.get_batch_of_minions(tavern_tier=tier,batch_size=size)


        batches.append(batch)

    for b in batches:
        pool.put_batch_of_minions_back_in_pool(b)

def test_benchmark_full_game(benchmark):
    benchmark(full_game_test)

def full_game_test():
    minions = []

    tiers = [1] * 2 + [2] * 3 + [3] * 4 + [4] * 4 + [5] * 6 + [6] * 8
    sizes = [3] * 2 + [4] * 3 + [4] * 4 + [5] * 4 + [5] * 6 + [6] * 8

    for index in range(6):
        size = sizes[index]
        tier = tiers[index]
        batch = pool.get_batch_of_minions(tavern_tier=tier,batch_size=size)

        pick = batch[0]
        batch.remove(pick)

        if len(minions) == 7:
            minion_to_sell = minions.pop()
            pool.put_minion_back_in_pool(minion_to_sell)

        minions.append(pick)

        pool.put_batch_of_minions_back_in_pool(batch)


    pool.put_batch_of_minions_back_in_pool(minions)




