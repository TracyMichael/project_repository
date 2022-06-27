# Module-Challenge-14

---

## Technologies


The Application has specific technologies that will be needed to run properly.


**Languages Required:** *Python*

**Libraries Required:** *Pandas, HVPlot, Holoviews, fbprophet, datetime, and PathLib

Before running the application the following Libraries will need to be imported:

```python
import pandas as pd
import numpy as np
from pathlib import Path
import hvplot.pandas
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from pandas.tseries.offsets import DateOffset
from sklearn.metrics import classification_report
```


Further details denoting requirements and verions are available in the requirements file.            

[Requirements](./requirements.txt)


---

## Installation Guide

This Machine Learning Trading Bot app will not work without the proper technologies listed above.  To ensure you have the applicable tools please install the requirements for the Crypto Investments Application using the text file in the Module-Challenge-14 folder as follows:

In The Terminal Run:

```python

pip install -r requirements.txt

```


---

## Usage


### **For Coders:** 

1. Read CSV into DataFrame, create simple moving averages (fast and slow) along with Strategy Returns.
2. Create signals for buy and sell instances.
3. Create Targets and Features, scale the data, and get results from a SVM model.
4. Check Outcomes and run a Logistic Regression Model on the data to see if outcomes change.  Charts will allow for visibility using Plot and HVPlot. (Save the Charts as a png file.)
5.  Compare the two Models to see which has the better outcome and look for improvements.

### **For Users:** 

The application is built to create a trading bot using Machine Learning

1. Create a Machine Learning Model to compare Actual Returns to Strategy Returns.
2. Use a Logistic Regression Model to compare Actual Returns to Strategy Returns.
3. Plot both charts to compare returns.


---

## Contributors

Tracy Davis <TracyMDavis88@gmail.com>

[Tracy Davis LinkedIn](https://www.linkedin.com/in/tracy-davis-mba-ma-2940a232/)

---

## License

MIT License

Copyright (c) [2022] [Tracy Davis]








