# Compare CSS

This is a simple Python script that: 

1. Finds all CSS files within a given directory (and its subdirectories).

2. Creates permutations of pairs.

  > Note: This means that File A will be compared to File B, but the script will be prevented from comparing File B to File A (i.e. doing the same work a second time). 

3. Compares files contents for similarity. 

4. Sorts the output from highest percentage of similarity to lowest.

5. Calculates the average percentage of similarity between all pairings. 

6. Outputs everything to a `results.txt` file.

It was written to compare student assignment submissions for large projects and to help flag _overly_ similar code. If two assignments are flagged as sharing a large amount of the same code, they should be manually reviewed for said similarities. 


## Notes

The path for the output is the users desktop. This should work across most operating systems (Linux, macOS, Windows). 


## Known Issues (That I'm Too Lazy To Fix)

- The error handling is extremely minimal (a simple loop with a try/catch block).

- If two files are empty (or nearly empty), there can be a false positive. Again, this doesn't indicate plagiarism, and is why everything should be manually checked.
