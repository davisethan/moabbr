"""Python interface to the moabbr Docker image for network meta-analysis of MOABB benchmarks.

Compares BCI decoding pipelines across datasets using frequentist NMA
(`nma`) and Bayesian NMA (`bnma`) as a sensitivity analysis. Requires
[Docker](https://www.docker.com) with the moabbr image available locally.

Source: [github.com/davisethan/moabbr](https://github.com/davisethan/moabbr)
"""

from .run import bnma, nma

__all__ = [nma.__name__, bnma.__name__]
