import csv
import os
import math
import pprint


#-----------------------------------------------------------------------------

def partition(data, attribute):
    
    values = {}

    for row in data:

        if not(values.has_key(row[attribute])):
            values[row[attribute]] = []

        values[row[attribute]].append(row)

    return values

#-----------------------------------------------------------------------------

def entropy(data, targetAttribute, values=['Yes','No']):
    '''
    Calculates data entropy based on boolean target attribute 
    '''

    P = [x for x in data if x[targetAttribute] == values[0]]

    p = float(len(P)) / float(len(data))
  
    if(p == 1):
        return 0

    if(p == 0):
        return 1

    n = 1.0 - p
   
    return ( -p * math.log(p,2) ) - ( n * math.log(n,2) )

    
#-----------------------------------------------------------------------------

def csv2data(fstream):
    '''
    Read in a table of data from CSV to a list of python dicts

    '''
    csvreader = csv.reader(csvfile)
    
    data = []   
    headings = []

    for i,row in enumerate(csvreader):
        
        if( i == 0):
            headings = row
        else:
            rowdata = {}
            for i in range(0, len(row)):
                rowdata[ headings[i] ] = row[i]

            data.append(rowdata)

    return data

#-----------------------------------------------------------------------------

def dtree( data, targetAttribute, ignore=[]):
    '''Build a decision tree based on the information gain 
     from different attributes
    '''

    attributes = data[0].keys()
    #make sure we are not calculating for target attribute
    attributes.remove(targetAttribute)

    #ignore the attributes on the ignore list
    for i in ignore:
        attributes.remove(i)
    
    return branch(data, attributes, targetAttribute) 

#----------------------------------------------------------------------------

def branch(data, attributes, targetAttribute, level=0):
   
    if(len(data) < 2):
        return data[0][targetAttribute]

    best_A,rank = best_attribute(data, attributes, targetAttribute)

    new_data = partition(data, best_A)

    node = {}

    attrs = list(attributes)
    attrs.remove(best_A)

    print "Splitting on attribute %s values %s" % (best_A, new_data.keys())

    for k in new_data.keys():
        node[k] = branch( new_data[k], attrs, targetAttribute, level+1)

    return { best_A : node }
#-----------------------------------------------------------------------------

def best_attribute(data, attributes, targetAttribute):
    ''' Find the best attribute for information gain on dataset
    '''

    #calculate entropy for whole data set 
    e_D = entropy(data, targetAttribute)

    attr_rank = []

    for A in attributes:
        #partition the data with attribute
        sets = partition(data, A)
       
        total_ent = 0
        for v in sets.keys():
            total_ent +=  entropy( sets[v], targetAttribute) * float(len(sets[v])) / float(len(data)) 

        attr_rank.append( ( A, e_D - total_ent) )

    return sorted( attr_rank, key=lambda x: x[1], reverse=True)[0]

#-----------------------------------------------------------------------------
        


#-----------------------------------------------------------------------------


if __name__ == "__main__":

    with file("apartments.csv","rb") as csvfile:
        data = csv2data(csvfile)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint( dtree(data, "Acceptable", ignore=['Apartment']) )
