library(partitions)

oparts <- function(N){
  # generate an integral matrix whose columns are the overpartitions of N
  # overlines denoted by negative integers
  
  if (N == 0){
    return(matrix(nrow=0, ncol=0))
  } else if (N == 1){
    return(matrix(c(1, -1), nrow=1))
  }
  
  # weight = sum of overlined parts
  weight <- 0:N
  
  ovr.list <- lapply(weight, function(i) -diffparts(i))
  
  ptn.list <- lapply(weight, function(i) parts(i))
  ptn.list[[1]] <- matrix(0)
  
  ovr.count <- lapply(ovr.list, function(M) ncol(M))
  ptn.count <- lapply(ptn.list, function(M) ncol(M))
  
  ovr.temp <- lapply(
    weight, function(i)
    rbind(ovr.list[[i+1]] %x% t(rep(1, ptn.count[[N-i+1]])),
          t(rep(1, ovr.count[[i+1]])) %x% ptn.list[[N-i+1]]
          )
    )

  ovr.temp <- lapply(
    ovr.temp, function(M)
    rbind(
      M, matrix(rep(0, ncol(M)*(N-nrow(M))), ncol=ncol(M))
    )
  )
  
  ovr.mat <- do.call(cbind, ovr.temp)
  return(ovr.mat)
}

OP <- function(N){
  return(ncol(oparts(N)))
}