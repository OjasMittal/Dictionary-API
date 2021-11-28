import definition
import justpy as jp
import json

class Api:

    @classmethod
    def serve(cls,req):
        wp=jp.WebPage()
        word=req.query_params.get('w')
        defined= definition.Definition(word).get()
        response={ "word":word,"definition":defined }
        wp.html=json.dumps(response)
        return wp
