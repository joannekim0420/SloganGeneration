import numpy as np
import torch
import json
from collections import namedtuple
import warnings
import argparse
from transformers import T5Tokenizer, T5ForConditionalGeneration, MT5ForConditionalGeneration
from googletrans import Translator
from torch import cuda
import re

device = 'cuda' if cuda.is_available() else 'cpu'

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=" ", type=str, help="description of company")
    parser.add_argument("--language", default="en", type=str, help="choose korean or english to generate slogan", choices=["en","ko","trans"])
    parser.add_argument("--num_sequences", type=int, default= 1, help="number of slogans to generate")
    
    args = parser.parse_args()
    print("input args:\n", json.dumps(vars(args), indent=4, separators=(",", ":")))
    return args

def main(args):
    torch.manual_seed(42) 
    np.random.seed(42)    
    torch.backends.cudnn.deterministic = True
    
    predictions = []
    if args.language == "en":
        model_path = "./infer_model/t5-ensg-Noise1+ep60" 

        tokenizer = T5Tokenizer.from_pretrained(model_path , config="./infer_model/t5-ensg-Noise1+ep60/tokenizer_config.json")
        
        model = T5ForConditionalGeneration.from_pretrained(model_path, config="./infer_model/t5-ensg-Noise1+ep60/config.json") #, ignore_mismatched_sizes=True

        model = model.to(device)
        
        inputs = tokenizer('generate slogan: '+args.input, max_length = 512, return_tensors="pt", truncation=True).to(device)
        outputs = model.generate(
                                input_ids = inputs['input_ids'], 
                                attention_mask = inputs['attention_mask'],
                                num_beams=5, 
                                num_return_sequences = args.num_sequences,
                                max_new_tokens = 50
                                )

        preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in outputs]
        predictions.extend(preds)
        print(*predictions, sep="\n")
        
    elif args.language == "ko":
        model_path = "./infer_model/mt5-kr0131-Noise1+ep1200"
        
        tokenizer = T5Tokenizer.from_pretrained(model_path, config="./infer_model/mt5-kr0131-Noise1+ep1200/tokenizer_config.json")  
        model = MT5ForConditionalGeneration.from_pretrained(model_path, config="./infer_model/mt5-kr0131-Noise1+ep1200/config.json") 
        model = model.to(device)
        
        inputs = tokenizer(args.input, max_length = 512, return_tensors="pt", truncation=True).to(device)
        outputs = model.generate(
                                input_ids = inputs['input_ids'], 
                                attention_mask = inputs['attention_mask'],
                                num_beams=5, 
                                num_return_sequences = args.num_sequences,
                                max_new_tokens = 50
                                )

        preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in outputs]
        predictions.extend(preds)
        print(*predictions, sep="\n")
        
    elif args.language == "trans":
        translator = Translator()
        tmp = []
        input_trans = translator.translate(args.input, src="ko", dest="en")
        print(input_trans.text)
        model_path = "./infer_model/t5-ensg-Noise1+ep60" 
        tokenizer = T5Tokenizer.from_pretrained("t5-small") 
        model = T5ForConditionalGeneration.from_pretrained("t5-small") #, ignore_mismatched_sizes=True

        tokenizer = T5Tokenizer.from_pretrained(model_path , config="./infer_model/t5-ensg-Noise1+ep60/tokenizer_config.json") 
        model = T5ForConditionalGeneration.from_pretrained(model_path, config="./infer_model/t5-ensg-Noise1+ep60/config.json") #, ignore_mismatched_sizes=True
        model = model.to(device)
        
        inputs = tokenizer('generate slogan: '+input_trans.text, max_length = 512, return_tensors="pt", truncation=True).to(device)
        outputs = model.generate(
                                input_ids = inputs['input_ids'], 
                                attention_mask = inputs['attention_mask'],
                                num_beams=5, 
                                num_return_sequences = args.num_sequences,
                                max_new_tokens = 20
                                )

        preds = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in outputs]
        tmp.extend(preds)
        
        for t in tmp:
            output_trans = translator.translate(t, src="en", dest="ko")
            
            output_trans = re.sub('[-=+,#/\:^@*\"※~ㆍ』.‘|\(\)\[\]`\'…》\”\“\’·]', '', output_trans.text)
            predictions.append(output_trans.strip())
        print(*predictions, sep="\n")
    
    else:
        assert args.language in ["en","kr","trans"], "language not provided" 
        
if __name__ == '__main__':
    args = parse_arguments()
    main(args)