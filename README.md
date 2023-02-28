# SloganGeneration

## **Evironment**
1. cuda 버전에 맞는 torch 다운
> training과 inference 시 사용한 torch 버전.
  ```
  torch                    1.13.0
torchaudio               0.12.1
torchmetrics             0.11.0
torchvision              0.14.0
  ```
2. requirements.txt 속 관련 패키지 설치 명령어 
<pre><code>pip install -r requirement.txt</code></pre>

## 파일 설명
```bash
├── infer_model #inference 시 필요한 사전 학습된 모델들이 저장되어 있는 곳
│   ├── mt5-kr0131-Noise1+ep1200  #: 한국어 사전 학습 모델
│   │    ├── pytorch_model.bin  #inference 시 실제로 참고하는 모델. 
│   │    ├── pytorch_model700.bin / pytorch_model800.bin  #inference에서 선택할 수 있는 후보 모델들이며, 파일명을 pytorch_model.bin으로 변경후 사용 가능.
│   │    └── tokenizer_config.json / config.json #inference 코드에서 사전 학습 모델 로드에 사용.
│   ├── t5-ensg-Noise1+ep50  #: 영어 t5 small 사전 학습 모델, config/gokenizer_config/pytorch_model 위와 설명 동일
│   ├── t5-ensg-Noise1+ep60  #: 영어 t5 small 사전 학습 모델
│   └── t5-ensg-Noise1+ep70  #: 영어 t5 small 사전 학습 모델
└── inference.py  #실제 inference 에 사용되는 코드

``` 

※ 사용하고자 하는 모델명은 반드시 pytorch_model.bin으로 되어있어야하고, pytorch_model.bin으로 지정된 모델은 1개이어야함. 

  - 예를 들어, pytorch_model800.bin을 사용하고자 하는 경우, 
  pytorch_model.bin의 파일명을 pytorch_model600.bin 등으로 변경해주고
	pytorch_model800.bin 을 pytorch_model.bin 으로 변경. 

※ 영어 학습 모델 변경시, inference 코드에서 파일명만 위 3개중 하나로 변경 가능

## ▶ How to Run
	<pre><code> python inference.py --input "브랜드 관련 설명" --num_sequences 5 --language "trans" </code></pre>
  
```
ㄴinput : 브랜드 관련 설명, 문장이 들어감
ㄴnum_sequences : 슬로건 생성 갯수
ㄴlanguage : 슬로건 생성 언어. 한국어-ko, 영어-en, 영어 번역-trans 사용가능
```
	
