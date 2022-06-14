&nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp;  <img src="https://github.com/ansfl/MEMS-IMU-Denoising/blob/main/figrues/Logo.png?raw=true" width="500" />


<!-- # MEMS-IMU-Denoising
This repository contains the experimental dataset associated with our paper "Data-Driven Denoising of Accelerometer Signals". -->

## Introduction
Modern navigation solutions are largely dependent on the performances of the standalone inertial sensors, especially at times when no external sources are available. During these outages, the inertial navigation solution is likely to degrade over time due to instrumental noises sources, particularly when using consumer low-cost inertial sensors. Conventionally, model-based estimation algorithms are employed to reduce noise levels and enhance meaningful information, thus improving the navigation solution directly. However, guaranteeing their optimality often proves to be challenging as sensors performance differ in manufacturing quality, process noise modeling, and calibration precision. In the literature, most inertial denoising models are model-based when recently several data-driven approaches were suggested primarily for gyroscope measurements denoising. Data-driven approaches for accelerometer denoising task are more challenging due to the unknown gravity projection on the accelerometer axes. To fill this gap, we propose several learning-based approaches and compare their performances with prominent denoising algorithms, in terms of pure noise removal: 

&nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp; <img src="https://github.com/ansfl/MEMS-IMU-Denoising/blob/main/figrues/VID_denoising.gif" width="700" class='center'/>

Next, we compare their effectiveness over the well-known stationary coarse alignment procedure, where roll and pitch angles are being evaluated from specific forces. Based on the benchmarking results obtained in field experiments, we show that: (i) learning-based models perform better than traditional signal processing filtering; (ii) non-parametric kNN algorithm outperforms all state of the art deep learning models examined in this study; (iii) denoising can be fruitful for pure inertial signal reconstruction, but moreover for navigation-related tasks, as both errors are shown to be reduced up to one order of magnitude.

&nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp; <img src="https://github.com/ansfl/MEMS-IMU-Denoising/blob/main/figrues/VID_levelling.gif" width="650" class='center'/>

## Dataset

<!-- Autonomous Navigation and Sensor Fusion Lab -->
Inertial measurements used in this research are based on a dataset previously published in the paper [`The Autonomous Platform Inertial Dataset`
](https://ieeexplore.ieee.org/document/9684368), using a unique device aligning between a [`Huawei P40`](https://www.gsmarena.com/huawei_p40-10153.php) smartphone and an Inertial
Lab [`MRU-P unit`](https://www.inertiallabs.com/mru-datasheet). 

&nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; 
&nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp;  <img src="https://github.com/ansfl/MEMS-IMU-Denoising/blob/main/figrues/Device_2.jpg?raw=true" width="425" />

Here however, to ensure stationarity of the accelerometer measurements, samples were extracted from platform at complete rest, at a large number of platform orientations. This way, accelerometer readings are guaranteed to reflect gravity projection only in a variety of roll (ϕ) and pitch (θ) angles. 

&nbsp; &nbsp;  &nbsp; &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp;  <img src="https://github.com/ansfl/MEMS-IMU-Denoising/blob/main/figrues/fig_test_set.png?raw=true" width="550" />

## Code

For convenience, two notebooks are provided, enabling reproduction of our results.

* **Full Mode** (GPU recommended) - Full solution pipeline from training to inference. 

* **Test Mode** (GPU free) - Direct inference and comparison between competing models, by uploading pretrained model weights, trained over *Intel i5-9600K CPU @ 3.70 GHz and NVIDIA GTX2080 GPU*. 

### Directory tree
<pre>
[root directory]
├── figures
├── data
├── execution
|   ├── Training Mode
|       └── *Training.ipynb*
|   └── Inference Mode
|       ├── *Inference.ipynb*
|       ├── RNN.pt
|       ├── Bi_LSTM.pt
|       └── Bi_GRU.pt
...
└── requirements.txt
<!--  Readme.md -->
</pre>


## Citation

If you found the experimental **DATA** useful for your research, please cite our paper:
```
@article{shurin2022autonomous,
  title={The Autonomous Platforms Inertial Dataset},
  author={Shurin, Artur and Saraev, Alex and Yona, Mor and Gutnik, Yevgeni and Faber, Sharon and Etzion, Aviad and Klein, Itzik},
  journal={IEEE Access},
  volume={10},
  pages={10191--10201},
  year={2022},
  publisher={IEEE}
}
```

If you found the paper's CODE helpful in your research, please cite our paper:

```
@article{engelsman2022datadriven,
  title={Data-Driven Denoising of Accelerometer Signals},
  author = {Engelsman, Daniel and Klein, Itzik}
  journal={arXiv preprint arXiv:2008.07397},
  url = {https://arxiv.org/abs/2206.05937},
  year={2022},
}
```
[<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/ArXiv_web.svg/250px-ArXiv_web.svg.png width=70/>](https://arxiv.org/abs/2206.05937)

<!-- ======================= JUNKYARD =======================  -->

<!-- &nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1Hq2kdrGidvbas2uoS_PyhQSY333reCq7/view?usp=sharing) -->


<!-- &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; 
&nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp; &nbsp;  &nbsp;  &nbsp;  <img src="https://github.com/Daniboy370/MEMS-IMU-Denoising/blob/main/Figrues/Bi-Directional-Uni.jpg?raw=true" width="650" />  -->
