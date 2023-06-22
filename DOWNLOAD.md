Dataset **DeepBacs** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/r/Q/QZ/sdaWMZcXZ75ki8rrIsRAC5jSHtoZ5lgXvkkm9fP2xf9yWS7OkYzBDMjkfzgx4zgKYwDAvI4Kqpu54zG1hhtqtgeEvfkBfIVQbjikuPQGu6IKxZutelD8ZOD8iJbV.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DeepBacs', dst_path='~/dtools/datasets/DeepBacs.tar')
```
The data in original format can be downloaded here:

- 🔗[Antibiotic_profiling_examples.png](https://zenodo.org/record/5551057/files/Antibiotic_profiling_examples.png?download=1)
- 🔗[DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip](https://zenodo.org/record/5551057/files/DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1)
- 🔗[DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip](https://zenodo.org/record/5551057/files/DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1)
