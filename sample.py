import web
import pandas as pd
import numpy as np


urls = (
    '/response', 'QuestionAnswering',
)

app = web.application(urls, globals())


class QuestionAnswering:

    
    def GET(self):


        web.header('Content-Type', 'application/json')
        user_data = web.input()
        query = user_data.query
        return query
		
        
if __name__ == "__main__":
    app.run()




