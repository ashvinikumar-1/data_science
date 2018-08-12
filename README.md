# data_science
Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. 

With loc and iloc you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer.


# Recognizing tidy data
For data to be tidy, it must have:

Each variable as a separate column.
Each row as a separate observation.

melting a DataFrame using pd.melt().
There are two parameters you should be aware of: id_vars and value_vars.
The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape),
while the value_vars represent the columns you do wish to melt into rows.
By default, if no value_vars are provided, all columns not set in the id_vars will be melted.
This could save a bit of typing, depending on the number of columns that need to be melted.