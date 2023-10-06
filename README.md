# SloganGeneration

Accpeted in CIKM 2023 short paper. 

Title : Slogan Generation with Noise Perturbation
link : TBU

## **Evironment**
1. Prepare Data
	Data format should be source-target pair matching. 
	(data from paper) <pre><code> python crawl_Slogan.py </code></pre>
	(your own data) prepare your own data in csv file with 2 column including source and target. 

3. Download Cuda with adaptable version
> My version of torch version.
  ```
  torch                    1.13.0
torchaudio               0.12.1
torchmetrics             0.11.0
torchvision              0.14.0
  ```
3. install necessary packages in requirements.txt
> installation
<pre><code>pip install -r requirement.txt</code></pre>

## 파일 설명
```bash
├── infer_model #inference 시 필요한 사전 학습된 모델들이 저장되어 있는 곳
│   ├── mt5-kr0131-Noise1+ep1200  #: 한국어 사전 학습 모델
│   │    ├── pytorch_model.bin  
│   │    ├── pytorch_model700.bin / pytorch_model800.bin 
│   │    └── tokenizer_config.json / config.json 
│   ├── t5-ensg-Noise1+ep50  #: 영어 t5 small 사전 학습 모델
└── inference.py  #실제 inference 코드

``` 

※ The model you want to use should be named 'pytorch_model.bin'.


## ▶ How to Run
	python inference.py --input "brand description~~" --num_sequences 5 --language "trans"
  
```
ㄴinput : brand description sentence
ㄴnum_sequences : number of slogans to generate
ㄴlanguage : slogan generation language currently supports korean and english. Korean->ko, English->en, KOEN Translation->trans 
```
	
