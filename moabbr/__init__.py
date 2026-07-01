"""[MOABB](https://neurotechx.github.io/moabb/) interface to [tombolo](https://pypi.org/project/tombolo/) for analysis of machine learning benchmarks.

Requires Docker with the tombolo image pulled:

```
docker pull ethandavisecd/tombolo:latest
```
"""

from .run import bnma, nma
from . import plots

__all__ = ["nma", "bnma", "plots"]
