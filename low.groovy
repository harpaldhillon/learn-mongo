def matchPattern(String text, String text1, String pattern) {
    isMatch = (text =~ pattern)
    return isMatch[0].replace(text1, "")
}

// Example usage
def text = """
- low 10 100
- medium 8 80
- high 5 50
- critical 1 10
"""

text1 = "critical "
def pattern = [/critical./, /high./, /medium./, /low./]
println matchPattern(text, text1, pattern[1]).split(" ")
