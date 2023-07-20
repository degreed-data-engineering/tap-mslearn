# tap-mslearn
This tap MSLearn was created by Degreed to be used for extracting data via Meltano into defined targets.

## Testing locally

To test locally, pipx poetry
```bash
pipx install poetry
```

Install poetry for the package
```bash
poetry install
```

To confirm everything is setup properly, run the following: 
```bash
poetry run tap-mslearn --help
```

To run the tap locally outside of Meltano and view the response in a text file, run the following: 
```bash
poetry run tap-mslearn > output/output.json 
```

A full list of supported settings and capabilities is available by running: `tap-mslearn --about`