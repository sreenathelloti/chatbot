#Using separateclasses 

import web

#Url mappings

urls = (
    '/tok', 'clean_and_tokenization',
    '/stop', 'stopwords',
    '/stem', 'stemming',
    '/spell', 'spellcorrector',
)
app = web.application(urls, globals())


#Class for cleaning and tokenizing the text

#if we write - http://localhost:8080/tok - tokenization is performed

class clean_and_tokenization:

    def GET(self):
        
        # Create  another file.
        # Import that file
        # call method from here.
        dirty_sen = ["here! <><>?//||are$ some# very *simple basic? @sentences.","they% wont be# very #complex, i'm #sure.","the +point_ of% these) _examples is= *to learn\\ how% basic* (text_ cleaning+ works_ on *very simple* data."]
        import app
        return "CLEANING AND TOKENIZATION :-", app.clean_and_tokenizing(dirty_sen)



#Class for Removing the stopwords
    
#if we write - http://localhost:8080/stop - stopwords removal is performed        

class stopwords:

    def GET(self):
        sent = [" i am working on very simple project but i am learning a lot"]
        import app
        return "STOPWORDS REMOVAL:-", app.stopwords_removal(sent)



#Class for Performing Stemming

#if we write - http://localhost:8080/stem - stemming is performed     

class stemming:

    def GET(self):
        example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

        import app
        return "STEMMING:-" , app.stemmingfunc(example_words)
    



#Class for performing spell correction
    
#if we write - http://localhost:8080/spell - spell correction is performed  

class spellcorrector:

    def GET(self):
        import spellcorrector2
       
        return "SPELL CORRECTOR:-" , spellcorrector2.correct('hte'),spellcorrector2.correct('heatlh'),spellcorrector2.known(spellcorrector2.edits1('hav')),spellcorrector2.known_edits2('an'),spellcorrector2.Prob('health'),spellcorrector2.Prob('policy')
     
    

#Running the Application
    
if __name__ == "__main__":
    app.run()
