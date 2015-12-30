""" this is for extracting the to_test question from json file, and you can decide whether to store the result in a txt"""
import json
def extractValidTexts(qFilePath, storepath = False):
    """find the json file and extract the valid question text and store it if you like"""
    # import the json file
    q_file = file(qFilePath)
    file_q = json.load(q_file)
    tempstrlist=[]
    # filtering
    for item in file_q:
        if len(item['fields']) == 6:
            if item['fields']['valid'] == True:
                tempstr = item['fields']['text']
                tempstr = str(item['pk']) + ' ' + tempstr
                tempstrlist.append(tempstr)
     


    # print len(tempstrlist)
    # result storing block(selectable)
    if storepath:
        with open('valid_text_file.txt','w') as f:
            for tempstr in tempstrlist:
                f.write(tempstr)
                f.write('\n')
    # return a list 
    return tempstrlist

def extractLabeledText(qFilePath, lFilePath, storepath = False):
    """extract the text which is labled and store it if you like."""
    q_file = file(qFilePath)
    file_q = json.load(q_file)    
    l_file = file(lFilePath)
    file_l = json.load(l_file)
    idxList = []
    tempstrlist=[]
    # extract the labeled index from labels.json
    for l_item in file_l:
        q_idx = l_item['fields']['question']
        idxList.append(q_idx)
    
    # extract the labeled text 
    for q_item in file_q:
        if len(q_item['fields']) == 6:
            if q_item['fields']['valid'] == True:
                if q_item['pk'] in idxList:
                    tempstr =   q_item['fields']['text']
                    # for idx inspection test
                    #tempstr = str(q_item['pk']) + ' ' + tempstr
                    tempstrlist.append(tempstr)
    if storepath:
        with open('labeled_text_file.txt','w') as f:
            for tempstr in tempstrlist:
                f.write(tempstr)
                f.write('\n')
    # return a list 
    return tempstrlist


        
        
        
        
    

    
