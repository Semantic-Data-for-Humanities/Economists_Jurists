
### sparql_functions : some useful functions using SPARQLwrapper

from SPARQLWrapper import SPARQLWrapper, SPARQLWrapper2, JSON, TURTLE, XML, RDFXML




## Fonction qui exécute la requête et renvoit le résultat

def get_json_sparql_result(endpoint,query):
    
    try:
        sparql = SPARQLWrapper(endpoint)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        sparql.setMethod('POST')
        rc = sparql.queryAndConvert()
        print(type(rc))
    except Exception as e:
        print(e)
    else:
        return rc
    
    
    
## Fonction générique permettant de transformer en liste les résultats d'une requête    
# NB : la fonction récupère directement le nom des variables du résultat
# NB2: cette fonction et le suivantes présupposent une structure homogène du résultat JSON
    
def sparql_result_to_list (result):
    
    i = 0
    variables = result['head']['vars']
    result_l = []
    
    for l in result['results']['bindings']:
        l_line = []
        for v in variables:
            try:                
                l_line.append(l[v]['value'])            
            except Exception as e:
                l_line.append('')   
                pass
        result_l.append(l_line)
                
    return result_l        
    
    
## Fonction générique permettant de transformer en liste les résultats d'une requête
# avec déclaration manuelle des variables
# insérer les variables sous cette forme : ' ?p ?name  ?birthDate '   
# les espaces ne sont pas pris en compte

def sparql_result_to_list_vars (result, variables):
    
    i = 0
    rs = []
    for v in variables.split():        
        rs.append(v.replace('?', '').strip())
        
    result_l = []
    for l in result['results']['bindings']:
        l_line = []
        for v in rs:
            try:                
                l_line.append(l[v]['value'])            
            except Exception as e:
                l_line.append('')   
                pass
        result_l.append(l_line)
                
    return result_l    






## list to dash separated text

def list_to_dash_separated_values (list):
    

    dashedValuesList = []

    try:
        for l in list:
            dashedValues = ''
            n = 1
            for e in l:
                if n < len(l):
                    dashedValues += (e + ' – ')
                else:
                    dashedValues += (e)                
                n += 1      
            dashedValuesList.append(dashedValues)   
    except Exception as e:
        print(e)
    else:        
        return '\n'.join(dashedValuesList)

