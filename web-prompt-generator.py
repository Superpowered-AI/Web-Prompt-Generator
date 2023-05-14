from duckpy import Client
client = Client()
while True:
    try:
        prompt = input("Main prompt:")
        if prompt == '':
            continue
        results = client.search(str(prompt))
        testlist = str("[result 0] "+results[0].description)+"[result 1] "+str(results[1].description)+"[result 2] "+str(results[2].description)
        print(str(testlist))
        forcedprompt="Search results"+str(testlist)+"Instructions: Using the provided web search results, write a comprehensive reply to the given query. Query: "+prompt
        print("Prompt with search:/n"+str(forcedprompt))
        print()
    except KeyboardInterrupt:
        break
