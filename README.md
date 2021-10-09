# DVC - DL -TF -AIOPS demo
### commands
#### Download the data
https://drive.google.com/drive/u/0/folders/1tz4IOoJKdi999IRdqJY04VOifyllRzj1
```bash
creating conda env
conda create --prefix ./env python=3.7 -y
```

```bash
to activate the env
source activate ./env
```

```bash
install the requirements
 pip install -r requirements.txt 
```
```bash
git init
dvc init
```
### creating empty files
```bash
mkdir -p config/utils
touch config/config.yaml config/secrates.yaml
```