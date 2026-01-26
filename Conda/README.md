# Conda Basics

GPU environment

https://developer.nvidia.com/cuda-downloads

https://repo.anaconda.com/miniconda/

https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh


1. Install

Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh 
```

Anaconda

```bash
bash Anaconda3-2022.05-Linux-x86_64.sh
```

installation finished.
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>>  YES

Unusual case

!!! very carful the export path bin </> :

```bash
sudo chown -R frazier:frazier /home/frazier/anaconda3
export PATH=/home/ubuntu/anaconda3/bin:$PATH
```

2. Deactivate base

```bash
conda config --set auto_activate_base false
```

3. Create empty/specific environment
```bash
conda create --name <myenv>
```

```bash
nano environment.yml
```

```yaml
name: <myenv>
channels:
  - pytorch
  - nvidia
dependencies:
  - python >= 3.8
  - pip
  - numpy>=1.20
  - click>=8.0
  - pillow=8.3.1
  - scipy=1.7.1
  - pytorch=1.9.1
  - cudatoolkit=11.1
  - requests=2.26.0
  - tqdm=4.62.2
  - ninja=1.10.2
  - matplotlib=3.4.2
  - imageio=2.9.0
  - pip:
    - glfw==2.2.0
    - pyopengl==3.1.5
    - imageio-ffmpeg==0.4.3
    - pyspng

```

```bash
conda env create --file=environment.yml
conda activate <env>
```

4. List environments

```bash
conda env list
```

5. installing/uninstalling from specific <channels>

```bash
conda install -c <channels> <pkg>
```

```bash
conda install -c anaconda scikit-learn
conda install -c conda-forge tensorboard
```

```bash
conda remove -n myenv scipy
```

6. conda remove environment

```bash
conda env remove -n <>
```

7. Update


Collecting package metadata (current_repodata.json): - WARNING conda.models.version:get_matcher(556): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.7.1.*, but conda is ignoring the .* and treating it as 1.7.1
done

```bash
conda update -n base -c defaults conda
```


8. conda install from requirments

```bash
conda install --yes --file requirements.txt
```
