def str = "[apple, banana, orange]"

// Remove leading and trailing square brackets and split by comma
def elements = str.substring(1, str.length() - 1).split(',')

// Create a new list and add each element
def list = elements.collect { it.trim() }

println(list) // Output: [apple, banana, orange]

