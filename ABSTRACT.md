The authors of the **DeepBacs** biomedical project highlight the rapid transformation of microscopy through Deep Learning (DL), which has enabled efficient analysis of complex data and often surpassed the performance of classical algorithms. As a result, there has been a significant effort to develop user-friendly tools that allow biomedical researchers, with limited computer science background, to leverage DL effectively. While such approaches have primarily focused on analyzing microscopy images from eukaryotic samples, they have been underutilized in microbiology.

To support researchers in their training process, the authors provide a specifically designed database of training and testing data, allowing bacteriologists to quickly explore how to analyze their data using DL techniques. The ultimate goal is to foster the efficient application of DL in microbiology, leading to the creation of novel tools for bacterial cell biology and antibiotic research.

Presented dataset contains training and test images of *E. coli cells* treated with different antibiotics for antibiotic phenotyping:

| Characteristic       | Value                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Data type            | Paired microscopy images (confocal fluorescence) and manual annotations                                                                         |
| Microscopy data type | Confocal fluorescence images of fixed E. coli cells stained for membrane (Nile Red) and DNA (DAPI) paired with annotations in PASCAL VOC format |
| Microscope           | Zeiss LSM710 confocal microscope with a Plan-Apo 63x oil objective (1.4 NA)                                                                     |
| Cell type            | Chemically fixed E. coli NO34 cells (MreB-sfGFPsw, kindly provided by Zemer Gitai) (untreated or drug-treated);                                 |
| Image size           | 400 x 400 px² (Pixel size: 84 nm)                                                                                                              |
