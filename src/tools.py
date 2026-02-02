import os
from exa_py import Exa
from langchain import tool 

class ExaSearchToolset():
    @tool
    def search(query: str):
        """Search for a webpage based on the query"""
        return ExaSearchToolset._exa.search(f"{query}", use_autoprompt=True, num_result=3)
    
    @tool
    def find_similar(url: str):
        """ Search for webpage similar to given url. The url passed in should be URL returned from 'search'. """
        return ExaSearchToolset._exa.find_similar(url, num_result=3)
    
    @tool
    def get_content(ids: str):
        """ Get the contents of a webpage. The ids must be passed in a list, 
        list of ids reteurned from 'search'. """

        ids=eval(ids)

        contents=str(ExaSearchToolset._exa().get_contents(ids))
        print(contents)
        contents=contents.split("URL:")
        contents=[content[:1000] for content in contents]
        return "\n\n".join(contents)
    
    def tools():
        return [
            ExaSearchToolset.search,
            ExaSearchToolset.find_similar,
            ExaSearchToolset.get_content
               ]
    
    
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))