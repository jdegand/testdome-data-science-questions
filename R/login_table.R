loginTable <- function(idNameVerified, idPassword) {
    # Remove 'verified' column from idNameVerified
    idNameVerified <- idNameVerified[, c("id", "name")]

    # Convert matrix to data frame and rename columns
    idPasswordDF <- as.data.frame(idPassword)
    colnames(idPasswordDF) <- c("id", "password")

    # Merge data frames on 'id'
    mergedDF <- merge(idNameVerified, idPasswordDF, by = "id")

    # Print the final result
    print(mergedDF)
}

# Example usage
idNameVerified <- data.frame(id = c(1, 2), 
    name = c("JohnDoe", "AnnFranklin"),
    verified = c(TRUE, FALSE))
idPassword <- matrix(c(1, 2, 987340123, 187031122),
    nrow = 2,
    ncol = 2)

print(loginTable(idNameVerified, idPassword))