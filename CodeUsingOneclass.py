#Using one class

import web


#Defining urls

urls = (
    '/response','TextProcessing',
)
app = web.application(urls, globals())

#if we write - http://localhost:8080/response - TextProcessing (tokenization,stemming,stopwords_removal,spell correction) is performed 


#Defining Class for textprocessing

class TextProcessing:
    
    #Defining Function
    
    def GET(self):

        #importing another python file which contains all the functions.
        
        import app  
        

        #Sentences
        
        raw_dirty_sen = ["here! <><>?//||are$ some# very *simple basic? @sentences.",
                         "they% wont be# very #complex, i'm #sure.",
                          "the +point_ of% these) _examples is= *to learn\\ how% basic* (text_ cleaning+ works_ on *very simple* data."]

        sent = [" i am working on very simple project but i am learning a lot"]
        
        example_words = ["python","pythoner","pythoning","pythoned","pythonly"]


        #calling functions which were there in another python file and returning values
             
        return "TOKENIZATION :-" , app.clean_and_tokenizing(raw_dirty_sen),"STOPWORDS REMOVAL :-" , app.stopwords_removal(sent), "STEMMING :-" , app.stemmingfunc(example_words),"SPELL CORRECTOR :-" , app.correct('hte'),app.correct('heatlh'),app.known(app.edits1('hav')),app.known_edits2('an'),app.Prob('health'),app.Prob('policy')



if __name__ == "__main__":
    app.run()
