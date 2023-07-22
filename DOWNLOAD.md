Dataset **DeepBacs** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/y/v/2h/y3E1S2zNBB9jz2KYLTIPvA9uN7mebDP24A8O5Rhlg3C1ODILHhMKaTpQSoY1aSiaZzHZiaMn7DSMCbLvJ5VH95MtNvgKJrs9InpPx75gH4FVpddMINsCE8XdvMXK.tar)

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
