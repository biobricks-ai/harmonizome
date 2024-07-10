#! /usr/bin/bash

export localpath=$(pwd)
export rawpath=$localpath/raw

for dir in "$rawpath"/**;
do
    dirname=$(basename "$dir")
    mkdir "brick/$dirname"
    for file in "$dir"/*.txt.gz;
    do
        name=$(basename "$file" .txt.gz)
        duckdb -c "copy (select * from read_csv('$file', delim='\t')) to 'brick/$dirname/$name.parquet' (format parquet)"
    done
done