library(DBI)
library(duckdb)

named_matrix <- function(mat) {
  apply(mat, 1, function(row) as.list(row), simplify = FALSE)
}

transform <- function(df, file) {
  con <- dbConnect(duckdb())
  duckdb_register(con, "results", df)
  out <- dbGetQuery(con, paste(readLines(file, warn = FALSE), collapse = "\n"))
  dbDisconnect(con, shutdown = TRUE)
  out
}
