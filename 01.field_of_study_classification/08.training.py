import pandas as pd
from simpletransformers.classification import ClassificationModel
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score, classification_report
import os
import pickle
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def f1_multiclass(labels, preds):
    return f1_score(labels, preds, average='micro')
def report(labels, preds):
    return classification_report(labels, preds)

train_df = pd.read_csv('train.csv', header=None, dtype={"0":str, "1":str})
eval_df = pd.read_csv('eval.csv', header=None, dtype={"0":str, "1":str})

#change the chosen model accordingly
model = ClassificationModel('bert', 'allenai/scibert_scivocab_uncased', num_labels=19, use_cuda=True, args={"fp16": False, "n_gpu": 4, "num_train_epochs": 2, "evaluate_during_training": True})

model.train_model(train_df, eval_df=eval_df)

result, model_outputs, wrong_predictions = model.eval_model(eval_df, f1=f1_multiclass, acc=accuracy_score, classification_report=report)

with open("results.txt", "w") as f:
    f.write(str(result))
with open("model_outputs.txt", "w") as f:
    f.write(str(model_outputs))
with open("wrong_predictions.txt", "w") as f:
    f.write(str(wrong_predictions))

model_name = "bert_model.sav"
pickle.dump(model, open(model_name, "wb"))

