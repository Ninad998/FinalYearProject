#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FinalYearProject.settings")

import django
django.setup()


from deep_stylo.models import Result

def getDataFromDB():
    results = Result.objects.filter(status__lt = 1).order_by('upload_date')
    return results

def markRunning(result):
    result.running()
    
def markCompleted(result, predicted_author, train_accuracy, validation_accuracy, test_accuracy, test_binary):
    result.complete(predicted_author, train_accuracy, validation_accuracy, test_accuracy, test_binary)

    
while (True):
    results = getDataFromDB()
    
    if results.exists():
        result = results.first()
        
        doc_id = int(result.doc_id)
        
        import ast
        authorList = ast.literal_eval(result.authorList)
        
        markRunning(result)
        
        import PythonScripts.StyloNeuralLSTM as Stylo
        (labels_index, history, train_acc, val_acc, samples) = Stylo.getResults(
                doc_id = doc_id, authorList = authorList[:], glove = '../glove/' )
        
        (predYList, predY, testY) = Stylo.getTestResults(
            doc_id = doc_id, authorList = authorList[:], glove = '../glove/' )
        
        loc = testY
        
        test_accuracy = predY[loc]
        
        test_binary = 0.0
        
        if(predY.tolist().index(max(predY)) == testY):
            test_binary = 1.0
            
        del Stylo
        
        predicted_author = labels_index[predY.tolist().index(max(predY))]
        
        markCompleted(result, predicted_author, train_accuracy, validation_accuracy,
                      test_accuracy, test_binary)
        
    else:
        import time
        time.sleep(600)