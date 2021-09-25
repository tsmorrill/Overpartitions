library(partitions)

cranks <- function(k, matrix){
  # Generate an integral matrix whose entries are the k-th residual cranks of the overpartitions
  # listed in matrix
  omega = rowSums(matrix == k)
  mu = rowSums(matrix %% k == 0 && matrix > omega)
  largest = matrix[1,]
  diff = (mu - omega)*(omega > 0)
  #cranks = matrix[1,]*(omega == 0) + (mu - omega)*(omega > 0)
  return(diff)
}

