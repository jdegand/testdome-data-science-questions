loadData <- function(file) {
    df <- read.csv(file, header = FALSE)
    df[, 2][df[, 2] == 0] <- "yellow"
    colnames(df) <- c("id", "color")
    return(df)
}

text = "0.0,blue\n1.0,0\n2.0,red"
print(loadData(textConnection(text)))