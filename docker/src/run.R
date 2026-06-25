library(jsonlite)
source("nma.R")
source("bnma.R")

commands <- list(
  nma = nma,
  bnma = bnma
)

args <- commandArgs(trailingOnly = TRUE)
command <- args[1]
greater_is_better <- args[2]

df <- read.csv(file("stdin"))
cat(toJSON(commands[[command]](df, greater_is_better), auto_unbox = TRUE, na = "null"))
