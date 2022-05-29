# YOLOV5: Image detection model
This repository contains an executable demonstration of YOLO and Tensorflow implementation for image detection.

## 1. Requirements Installation


## Installation
can be installed from PyPI using `pip` or your package manager of choice:

```bash
pip install git+https://github.com/berezerker/yolov5_package/
```
## Usage

This model implemention is executable as a CLI tool using the `yolov5_package` command. 
A basic model is given inside the package. Also runs with a provided image.

To be able to see the default working of the demo, simply type demo in the terminal and hit Enter.
```bash
demo
```

# pre-commit usage
To check for formatting errors, black and pylint was added.
Usage:
```bash
black .
```
It will modify files to be more appealing for working.
Pylint was added to pre-commit hooks, same as black.
The following command will display all the warnings and errors in formatting:
```bash
 pre-commit run -a
 ```
 After that, one can safely commit all changes.


![Example output of the model](image_testyolov5_output.jpg)
