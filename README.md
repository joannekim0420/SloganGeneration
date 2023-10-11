# SloganGeneration

Accpeted in CIKM 2023 short paper.  

[Title] Slogan Generation with Noise Perturbation  
[paper link](https://arxiv.org/abs/2310.04472)

## **Evironment**
### 1. Prepare Data   
<img src = "https://github.com/joannekim0420/SloganGeneration/blob/main/crawl_img.png" width="40%" height="%">    
	
 Data format should be source-target pair matching.    
- data from paper is crawled from (https://sloganlist.com) based on crawling_slogan.ipynb. 
- (your own data) prepare your own data in csv file with 2 column including source and target.


### 2. Download Cuda with adaptable version
> My version of torch version.
  ```
  torch                    1.13.0
torchaudio               0.12.1
torchmetrics             0.11.0
torchvision              0.14.0
  ```

### 3. Install necessary packages in requirements.txt
> installation
<pre><code>pip install -r requirement.txt</code></pre>


### 파일 설명
```bash
├── infer_model # where pretrained models are saved for inference 
│   ├── mt5-kr0131-Noise1+ep1200  #: pretrained korean model
│   │    ├── pytorch_model.bin  
│   │    ├── pytorch_model700.bin / pytorch_model800.bin 
│   │    └── tokenizer_config.json / config.json 
│   ├── t5-ensg-Noise1+ep50  #: english t5 small pre-trained model
├── crawling_slogan.ipynb # code for crawling slogans in sloganlist.com
├── inference.py  # inference code
└── requirements.txt #env settings

``` 

※ The model you want to use should be named 'pytorch_model.bin'.


## ▶ How to Run
	python inference.py --input "brand description~~" --num_sequences 5 --language "trans"
  
```
ㄴinput : brand description sentence
ㄴnum_sequences : number of slogans to generate
ㄴlanguage : slogan generation language currently supports korean and english. Korean->ko, English->en, KOEN Translation->trans 
```
	
