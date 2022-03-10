# Benchmarks

These are extremely simple benchmarks. There are many things that make these
tests very "unscientific." Take these numbers with a grain of salt

## postgres

| Key Derivation Method | Indy               | Askar              |
|-----------------------|--------------------|--------------------|
| raw                   | 2.3764007568359373 | 0.6374470472335816 |
| argon2i_mod           | 2.3635244607925414 | 1.4669977188110352 |

## SQLite - Memory

| Key Derivation Method | Indy | Askar                |
|-----------------------|------|----------------------|
| raw                   | N/A  | 0.002950096130371094 |
| argon2i_mod           | N/A  | 0.7896870136260986   |
