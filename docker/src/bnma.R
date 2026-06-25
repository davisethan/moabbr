library(gemtc)
library(rjags)
library(posterior)
source("utils.R")

bnma <- function(df, greater_is_better) {
  arm <- transform(df, "bnma.sql")
  network <- mtc.network(data.ab = arm)
  model <- mtc.model(
    network,
    likelihood = "normal",
    link = "identity",
    linearModel = "random",
    n.chain = 4
  )
  capture.output(
    results <- mtc.run(model, n.adapt = 5000, n.iter = 1e5, thin = 10),
    file = stderr()
  )
  draws <- as_draws_array(results$samples)
  diag <- summarise_draws(draws)
  sd_draws <- as_draws_array(results$samples)[, , "sd.d"]
  preferred_direction <- if (greater_is_better) 1 else -1
  rank <- rank.probability(results, preferredDirection = preferred_direction)
  sucra <- apply(rank, 1, function(p) {
    n <- length(p)
    sum(cumsum(p)[-n]) / (n - 1)
  })
  rel <- relative.effect.table(results)

  list(
    sucra = as.list(sucra),
    league = list(
      md = named_matrix(rel[, , "50%"]),
      lower = named_matrix(rel[, , "2.5%"]),
      upper = named_matrix(rel[, , "97.5%"])
    ),
    heterogeneity = list(
      sd = as.numeric(median(sd_draws)),
      sd_lower = as.numeric(quantile(sd_draws, 0.025)),
      sd_upper = as.numeric(quantile(sd_draws, 0.975))
    ),
    convergence = list(
      rhat_max = max(diag$rhat),
      ess_bulk_min = min(diag$ess_bulk),
      ess_tail_min = min(diag$ess_tail)
    )
  )
}
