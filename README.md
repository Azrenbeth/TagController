# TagController
Multi-level tag controller for emulating a tagged memory using an in-memory table.
Zeroing of the in memory tag table can be disabled by building with `-D NO_TAGTABLE_ZEROING`.

# Part III projct information

## Code files

`[N]` indicates that a file or directory of files is new and created by me

`[O]` indicates that the file already existed but was edited/extended by me in a significant way

`[-]` indicates that this file was not modified

```
   .
[N]├── analysis/*
[-]├── Benchmark
[-]│   ├── BenchHashTable.c
[O]│   ├── BenchModelDRAM.bsv
[-]│   ├── BenchRegFileAssoc.bsv
[-]│   ├── BenchRegFileHash.bsv
[N]│   └── RunRequestsFromFile.bsv
[-]├── BlueStuff/*
[O]├── Makefile
[-]├── TagController
[-]│   ├── AXI_Helpers.bsv
[-]│   ├── CacheCore
[O]│   │   ├── Bag.bsv
[O]│   │   ├── CacheCorderer.bsv
[O]│   │   ├── CacheCore.bsv
[-]│   │   ├── SDPMem.bsv
[-]│   │   ├── UGFFFullOfUniqueInts.bsv
[-]│   │   └── VnD.bsv
[-]│   ├── Debug.bsv
[-]│   ├── Fabric_Defs.bsv
[-]│   ├── MasterSlaveCHERI.bsv
[-]│   ├── MemTypesCHERI.bsv
[N]│   ├── Merge.bsv (Based on similar file in BERI)
[-]│   ├── MultiLevelTagLookup.bsv
[N]│   ├── PipelinedTagLookup.bsv (Based on MultiLevelTagLookup.bsv)
[-]│   ├── RoutableCHERI.bsv
[O]│   ├── TagControllerAXI.bsv
[O]│   ├── TagController.bsv
[-]│   └── TagTableStructure.bsv
[-]├── tagsparams.py
[-]└── Test
[-]    ├── bluecheck/*
[-]    ├── DUT.bsv
[-]    ├── Hash.c
[O]    ├── MemoryClient.bsv
[-]    ├── ModelDRAM.bsv
[-]    ├── RegFileAssoc.bsv
[-]    ├── RegFileHash.bsv
[-]    ├── TestEquiv.bsv
[O]    └── TestMemTop.bsv
```

## Tag controller versions 

The 4 versions of the tag controller built for the simulations discussed in the report can be found in branches of this repository:

`original_latency` - original single-cache

`incremental_latency` - improved single-cache

`not_ooo_no_write_resps` - simple pipelined

`final_latency` - out-of-order pipelined