""" This project is for the geometry element extraction, and then testify the results of it."""
##### coarse description of steps
### 1. import question text
### 2. start processing text
### 3. start compare the result and testify the program
##### step start below
import string
from text_extract import *
# define the dict for rule
"""
geo_dict = {
    pointType: ['point','center','midpoint'],
    angleType: ['angle'],
    arcType: ['arc'],
    lineType: ['line', 'diameter', 'chord', 'median', 'altitude','secant','hypothenuse',
             'transversal','diagonal','bisector','ray'],
    polygonType:['triangle', 'rectangle', 'square', 'rhombus', 'base','quadrilateral','hexagon'],
    circleType:['circle','circles']
    
    }
"""
pointType = ('point','center','midpoint')
angleType = ('angle')
arcType = ('arc','arcs')
triType = ('triangle','angle')
lineType = ('line', 'diameter', 'chord', 'median', 'altitude','secant','hypothenuse',
             'transversal','diagonal','bisector','ray')
polygonType = ('triangle', 'rectangle', 'square', 'rhombus', 'base','quadrilateral','hexagon')
circleType = ('circle','circles')

## define process functions for step two
# 


### step one: import quesion text from json file and write into a txt
QuestionFilePath = "questions.json"
LabelFilePath = "labels.json"
#textstr = extractValidTexts(QuestionFilePath,True)

# get the list of the question text, each item in the list is a string for a question
textstrlist = extractLabeledText(QuestionFilePath,LabelFilePath,False)
geoLabels =[]
# get the result of label and type for each question using our parsing rule
for t_item in textstrlist:
    # handle the text separately for each question
    #t_item = str(t_item)
    #t_item = t_item.translate(None,string.punctuation)
    geoElements=[]
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    t_item = t_item.translate(remove_punctuation_map)
    words = t_item.split()
    #words_len = [len(word) for word in words]
    #upper_words = [word for word in words if word.isupper()]
    #upper_words_len = [len(word) for word in words]

    for i, w in enumerate(words):
        tempGeoElement={'label':'default','type':'default'}
        if w.isupper():
            pre_w = (words[i-1]).lower()
            tempGeoElement['label'] = w
            if len(w) == 1:
                if pre_w in circleType:
                    tempGeoElement['type'] = 'circle'
                elif pre_w in angleType:
                    tempGeoElement['type'] = 'angle'
                elif pre_w in lineType:
                    tempGeoElement['type'] = 'line'
                else:
                    tempGeoElement['type'] = 'point'
            elif len(w) == 2:
                if pre_w in arcType:
                    tempGeoElement['type'] = 'arc'
                else:
                    tempGeoElement['type'] = 'line'
            elif len(w) == 3:
                if pre_w in triType:
                    tempGeoElement['type'] = pre_w
            elif len(w) == 4:
                tempGeoElement['type'] = 'quad'
            elif len(w) == 6:
                tempGeoElement['type'] = 'hexagon'
            else:
                tempGeoElement['type'] = 'polygon'
            geoElements.append(tempGeoElement)
    geoLabels.append(geoElements)
        
# write the result into a txt (optional)
with open('r_label.txt','w') as fun:
    for r_item in geoLabels:
        fun.write(str(r_item))
        fun.write('\n')
# get the label and type from original data label


                
            

            





### step two: start processing text
# 
# create a txt file to store the results