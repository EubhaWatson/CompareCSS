# Compare CSS

This is a simple JuPyTer Notebook script that: 

1. Finds all CSS files within a given directory (and its subdirectories).

2. Compares files contents for similarity. 

3. Sorts the output from highest percentage of similarity to lowest.

4. Outputs everything to a `results.txt` file.

It was written to compare student assignment submissions for large projects and to help flag _overly_ similar code.


## Notes

On Line 37, the path for the output is hard-coded to a file on my desktop. **Change this** to suit your own needs.


## Known Issues (That I'm Too Lazy To Fix)

- The error handling is extremely minimal (a simple loop with a try/catch block).

- When comparing hundreds of files, it can take several minutes to finish. It would be a lot more efficient with a proper pairing algorithm (so that the same files aren't paired together multiple times).

- Often, comparing `file` to `file2` will yield different results than `file2` to `file`. This means this script shouldn't be used to actually calculate percentage similarity; instead, it's just to flag two files with a high similarity so that they can be manually checked.

- If two files are empty (or nearly empty), there can be a false positive. Again, this doesn't indicate plagiarism, and is why everything should be manually checked.