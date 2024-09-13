import m5
from m5.objects import *
from common.cores.arm import ex5_big

class BP_tournament(TournamentBP):
    localPredictorSize = 64
    localCtrBits = 2
    localHistoryTableSize = 64
    globalPredictorSize = 1024
    globalCtrBits = 2
    choicePredictorSize = 1024
    choiceCtrBits = 2

# Bi-Mode Branch Predictor
class BP_BiMode(BiModeBP):
    globalPredictorSize = 8192
    globalCtrBits = 2
    choicePredictorSize = 8192
    choiceCtrBits = 2
    instShiftAmt = 2

class L1Cache(Cache):
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    tgts_per_mshr = 8
    writeback_clean = True


# Instruction Cache
class L1I(L1Cache):
    mshrs = 2
    size = "32kB"
    assoc = 2
    is_read_only = True


# Data Cache
class L1D(L1Cache):
    mshrs = 6
    size = "32kB"
    assoc = 2
    write_buffers = 16


# L2 Cache
class L2(Cache):
    tag_latency = 15
    data_latency = 15
    response_latency = 15
    mshrs = 16
    tgts_per_mshr = 8
    size = "2MB"
    assoc = 16
    write_buffers = 8
    clusivity = "mostly_excl"
    # Simple stride prefetcher
    prefetcher = StridePrefetcher(degree=8, latency=1, prefetch_on_access=True)
    tags = BaseSetAssoc()
    replacement_policy = RandomRP()

cpu_name = __name__
cpu_spec = (ex5_big.ex5_big, L1I, L1D, L2, BP_tournament)

