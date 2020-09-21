import pandas as pd
from simpletransformers.classification import ClassificationModel
import os
import pickle
os.environ["TOKENIZERS_PARALLELISM"] = "false"

print("Loading model...")
model = ClassificationModel('bert', 'scibert_20000_input_2_epoch/outputs/best_model', num_labels=19, use_cuda=True, args={"fp16": False, "n_gpu": 4, "eval_batch_size": 4096})
print("Finished loading model...")

def classify(inp, model):
    print(f"Loading input {inp}...")
    with open(f"{inp}", "r") as f:
        input_list = []
        for line in f:
            input_list.append(line.split(",")[0])
    print("Finished loading input.")
    print(f"Classification in progress for {inp}...")
    with open(f"{inp}labeled.txt", "w") as g:
        predictions, raw_outputs = model.predict(input_list)
        for item in predictions:
            g.write(f"{item}\n")
    print("Finished classification")

#If necessary, split the input file into multiple parts and classify in sequence
classify("01.tokenized_abstracts.txt", model)
