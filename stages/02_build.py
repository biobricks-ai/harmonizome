import pandas as pd
import sys
import pyarrow as pyarrow
import pyarrow.parquet as pq
from pathlib import Path
from pyarrow.csv import read_csv, ParseOptions
import fastparquet as fastparquet
import os

raw_path = Path("raw")
brick_path = Path("brick")

for file in raw_path.iterdir():
    if file.is_dir():
        out_dir = "brick/" + file.name
        os.mkdir(out_dir)
        for f in file.iterdir():
            out_path = f.with_suffix(".parquet")
            csv: pyarrow.Table = read_csv(f, parse_options=ParseOptions(delimiter="\t"))
            pq.write_table(csv, f"{out_dir}/{out_path.name}")