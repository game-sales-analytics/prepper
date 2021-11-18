# Prepper

Games sales analytics application initial dataset cleaner and parser CLI application. Given `dataset.csv`, the initial dataset for game sales data, it parses, validates, and cleans up the dataset, generating `clean-dataset.json`, as the output ready to be consumed by the application services. It also generates a file named `invalids.json` which contains information about the invalid entries of the `dataset.csv` which were removed during the cleanup stage.
