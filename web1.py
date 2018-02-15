import web
import numpy as np
import UsefulFunctions
import Training
from sklearn.metrics.pairwise import cosine_similarity

# Defining urls

urls = (
    '/response', 'QuestionAnswering',
)

app = web.application(urls, globals())



# if we write -  http://localhost:8080/response?query=hello or anyinput - proper response is given out


# Defining Class for QuestionAnswering

class QuestionAnswering:

    def GET(self):
        web.header('Content-Type', 'application/json')
        user_data = web.input()
        query = user_data.query
        #Start with an empty list.
        inputques = []
        #Add the input query to our list.
        inputques.append(query)
        inputques = UsefulFunctions.tokenization_spellcheck(inputques)
        im = UsefulFunctions.createTfidfVectorizer_Instance(inputques)
        #Loading the tfidf matrix from disk
        qm = np.load(Training.save_matrix_path)
        coslist = cosine_similarity(qm, im).flatten()
        maxsim = np.argmax(coslist)
        response = Training.response[maxsim]
        #returning response
        return response

            


if __name__ == "__main__":
    app.run()
