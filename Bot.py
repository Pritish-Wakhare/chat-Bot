import wolframalpha

client = wolframalpha.Client('TLAGAL-T685ELP6XR')
while True:
    query = str(input('Query:  '))
    res = client.query(query)
    output = next(res.results).text
    print(output)
    
