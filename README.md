On your computer, in the root directory of this repository, create a folder titled `data`. Within that folder, add the `ebnerd_demo`, `ebnerd_small`, `ebnerd_large`, and/or `ebnerd_testset` folders and their respective data.

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
│       └── ...
├── feature_engineering.ipynb
└── ...
```

Be sure to include a `.gitignore` file that contains at least `/data` and `/data_processed` to prevent your client from uploading the dataset files.