"""Analyze [MOABB](https://neurotechx.github.io/moabb/) machine learning benchmarks with R.

Adapts MOABB evaluation results for the [tombolo](https://pypi.org/project/tombolo/) Python package.

Requires Docker with the [tombolo](https://hub.docker.com/r/ethandavisecd/tombolo) image pulled:

```
docker pull ethandavisecd/tombolo:latest
```
"""

from .run import bnma, nma
from . import plots

__all__ = ["nma", "bnma", "plots"]
