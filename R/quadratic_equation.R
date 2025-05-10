findRoots <- function(a, b, c) {
  root <- sqrt(b^2 - 4*a*c)
  denominator <- 2 * a
  x1 <- (-b + root) / denominator
  x2 <- (-b - root) / denominator
  
  return(c(x1, x2))  # Return as a vector
}

print(findRoots(2, 10, 8))