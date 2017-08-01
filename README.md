# Benchmark Tests

This repository contains several methods and datasets used for materials property prediction. 

## Jupyter Notebooks

deJong\_comp\_descriptors.ipynb:
Composition based attributes from [deJong 2016](https://www.nature.com/articles/srep34256)

Deml\_descriptors.ipynb:
Formation energy prediction using descriptors from [Deml 2016](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.085142)

Deml\_matminer.ipynb:
Comparison of predictions using the [predict\_Etot\_dHf](https://github.com/ademl/predict_Etot_dHf) code (method described in [Deml 2016](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.085142))

Dey\_replication.ipynb:
Band gap prediction using the method from [Dey 2014](http://dx.doi.org/10.1016/j.commatsci.2013.10.016)

Meredig\_replication.ipynb:
Formation energy prediction from [Meredig 2014](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.89.094104)

Ward\_glass\_formation.ipynb:
Glass formation prediction using the method from [Ward 2016](https://www.nature.com/articles/npjcompumats201628)

Ward\_replication.ipynb:
Band gap, formation energy, and volume prediction using the method from [Ward 2016](https://www.nature.com/articles/npjcompumats201628)

## Datasets
bandgap.data:
Band gap dataset from [Ward 2016](https://www.nature.com/articles/npjcompumats201628)

deml\_dataset.csv:
Formation energy dataset from [Deml 2016](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.93.085142)

deml\_predictions.csv:
Formation energy predictions generated using deml\_dataset.csv and [predict\_Etot\_dHf](https://github.com/ademl/predict_Etot_dHf) code

dey\_element\_data.csv:
Element property data used in [Dey 2014](http://dx.doi.org/10.1016/j.commatsci.2013.10.016)

dey\_training\_set.csv:
Training set for band gap prediction from [Dey 2014](http://dx.doi.org/10.1016/j.commatsci.2013.10.016)

glass.data:
Glass formation dataset from [Ward 2016](https://www.nature.com/articles/npjcompumats201628)

meredig\_binary\_hull.data:
Binary hull training data from [Meredig 2014](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.89.094104)

meredig\_prediction\_set.csv:
Prediction set from [Meredig 2014](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.89.094104)

meredig\_stable\_ternary.data:
Stable ternary training data from [Meredig 2014](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.89.094104)

oqmd\_all.data:
Full oqmd dataset from [Ward 2016](https://www.nature.com/articles/npjcompumats201628)
