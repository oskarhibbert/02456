In the root directory of this repository, create a folder titled `data`. Within that folder, add the `ebnerd_demo`, `ebnerd_small`, `ebnerd_large`, and/or `ebnerd_testset` folders.

The repository or working directory should be structured as follows:

```
02456/
├── data/
│   ├── ebnerd_demo/
│   │   └── ...
│   ├── ebnerd_large/
│   │   └── ...
│   ├── ebnerd_small/
│   │   └── ...
│   └── ebnerd_testset/
│   │   └── ...
├── parquet_to_csv.py
├── summary_statistics.ipynb
└── ...
```

Be sure to include a `.gitignore` file that contains at least `/data` to prevent your client from uploading the large dataset files.

:-)
