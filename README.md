# Benchmarks

These are extremely simple benchmarks. There are many things that make these
tests very "unscientific." Take these numbers with a grain of salt

## postgres

Across 100 tests, creating then opening the wallet (measured in seconds):

Indy:
```
== Raw ==
Total: 67.0744800567627
Average create: 0.6630573940277099
Average open: 0.007466027736663819
Average create + open: 0.6705234217643737
== Derived ==
Total: 240.01718854904175
Average create: 1.5328075361251832
Average open: 0.8673277854919433
Average create + open: 2.4001353216171264
```

Askar:
```
Raw
Total: 65.16856503486633
Average create: 0.6448825454711914
Average open: 0.00587733268737793
Average create + open: 0.6507598781585693
Argon2i Mod
Total: 205.73217153549194
Average create: 1.349460892677307
Average open: 0.7061620259284973
Average create + open: 2.0556229186058044
```

## SQLite - Memory

| Key Derivation Method | Indy | Askar                |
|-----------------------|------|----------------------|
| raw                   | N/A  | 0.002950096130371094 |
| argon2i_mod           | N/A  | 0.7896870136260986   |
