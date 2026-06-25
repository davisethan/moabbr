library(netmeta)
source("utils.R")

nma <- function(df, greater_is_better) {
  paired <- transform(df, "nma.sql")
  m <- netmeta(
    TE = md,
    seTE = se,
    treat1 = treat1,
    treat2 = treat2,
    studlab = study,
    data = paired,
    sm = "MD",
    method.tau = "DL",
    method.random.ci = "t-dist",
    common = FALSE,
    random = TRUE,
    prediction = TRUE,
    correlated = TRUE
  )
  z <- m$TE.random / m$seTE.random
  pval <- 2 * pt(-abs(z), df = m$df.Q)
  diag(z) <- NA
  diag(pval) <- NA
  small_values <- if (greater_is_better) "bad" else "good"

  list(
    p_scores = as.list(netrank(m, small.values = small_values)$Pscore.random),
    league = list(
      md = named_matrix(replace(m$TE.random, diag(nrow(m$TE.random)) == 1, NA)),
      lower = named_matrix(replace(m$lower.random, diag(nrow(m$lower.random)) == 1, NA)),
      upper = named_matrix(replace(m$upper.random, diag(nrow(m$upper.random)) == 1, NA)),
      z = named_matrix(z),
      pval = named_matrix(pval)
    ),
    heterogeneity = list(
      tau2 = m$tau^2,
      tau = m$tau,
      i2 = m$I2,
      i2_lower = m$lower.I2,
      i2_upper = m$upper.I2,
      q = m$Q,
      q_df = m$df.Q,
      q_pval = m$pval.Q
    ),
    prediction = list(
      lower = named_matrix(replace(m$lower.predict, diag(nrow(m$lower.predict)) == 1, NA)),
      upper = named_matrix(replace(m$upper.predict, diag(nrow(m$upper.predict)) == 1, NA))
    )
  )
}
