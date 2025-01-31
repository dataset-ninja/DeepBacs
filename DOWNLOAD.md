Dataset **DeepBacs E. Coli** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzExNDJfRGVlcEJhY3MgRS4gQ29saS9kZWVwYmFjcy1lLi1jb2xpLURhdGFzZXROaW5qYS50YXIiLCAic2lnIjogIkdUSHFJaS9VeEFWYk02aFVMN2o2YUhQKzlzSEVQQXErRjZ0WFVyazZoREE9In0=)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='DeepBacs E. Coli', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Antibiotic_profiling_examples.png](https://zenodo.org/record/5551057/files/Antibiotic_profiling_examples.png?download=1)
- [DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip](https://zenodo.org/record/5551057/files/DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1)
- [DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip](https://zenodo.org/record/5551057/files/DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1)
