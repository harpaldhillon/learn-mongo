def removeTextBeforeFirstSlash(String imageName) {
    // Find the index of the first forward slash
    def indexOfSlash = imageName.indexOf('/')

    // Check if a forward slash was found
    if (indexOfSlash >= 0) {
        // Extract the substring starting from the character after the first forward slash
        def result = imageName.substring(indexOfSlash + 1)
        return result
    } else {
        // If no forward slash was found, return the original string
        return imageName
    }
}

// Example usage:
def imageName = "docker.io/conftest/this/image:v1"
def modifiedImageName = removeTextBeforeFirstSlash(imageName)
println modifiedImageName
