from ply.lex import lex
from ply.yacc import yacc
import codecs

def alpha(movie_link):

    tokens=('PRETITLE','POSTTITLE','PREDIRECTOR','PREPRODUCER','PREWRITER','PREBOXOFFICE','PRERUNTIME'
            ,'PRESTORYLINE','STRING','COST','HEAD','AEND','AEND2','POSTRUNTIME','PRELANGUAGE')


    def t_PRETITLE(t):
        r'<title>'
        return t

    def t_POSTTITLE(t):
        r'-[\s]Rotten[\s]Tomatoes<\/title>'
        return t

    def t_PREDIRECTOR(t):
        r'Director:<\/div>[*\s]+<div[\sa-zA-Z0-9=\:\-_\"]+>[*\s]+'
        return t

    def t_PREPRODUCER(t):
        r'Producer:<\/div>[*\s]+<div[\sa-zA-Z0-9=\:\-_\"]+>[*\s]+'
        return t

    def t_PREWRITER(t):
        r'Writer:<\/div>[*\s]+<div[\sa-zA-Z0-9=\:\-_\"]+>[*\s]+'
        return t

    def t_PREBOXOFFICE(t):
        r'Box[\s]Office[\s\](Gross[\]USA):<\/div>[\s]*<div[\s]class="meta-value"[\s]data-qa="movie-info-item-value">'
        return t

    def t_PRESTORYLINE(t):
        r'<div[\s]id="movieSynopsis"[\sa-zA-Z0-9=\:\-_\"]+>[*\s]+'
        return t

    def t_PRERUNTIME(t):
        r'Runtime:<\/div>[*\s]+<div[\sa-zA-Z0-9=\:\-_\"]+>[*\s]+<time[\sa-zA-Z0-9=\"]+>'
        return t

    def t_POSTRUNTIME(t):
        r'[\s]*<\/time>'
        return t

    def t_PRELANGUAGE(t):
        r'Original[\s]Language:<\/div>[\s]*<div[\s]class="meta-value"[\s]data-qa="movie-info-item-value">'
        return t
        
    def t_HEAD(t):
        r'<a[\s]href[a-zA-Z0-9 =\/"_-]*>'
        return t

    def t_STRING(t):
        r'[a-zA-Z0-9().,ÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ ]+'
        return t

    def t_COST(t):
        r'[a-zA-Z0-9$. ]+'
        return t


    def t_AEND2(t):
        r'<\/a>,[\n\s]*'
        return t

    def t_AEND(t):
        r'<\/a>[\n\s]*'
        return t

    def t_error(t):
        t.lexer.skip(1)

    

    def p_start(t):
        '''start : director 
                    | title
                    | producer
                    | writer
                    | boxoffice
                    | runtime
                    | storyline
                    | language
        '''

    def p_director(t):
        'director : PREDIRECTOR name'
        movie_info['Director']=t[2].strip()

    def p_title(t):
        'title : PRETITLE STRING POSTTITLE'
        movie_info['Movie Name'] = t[2].strip()

    def p_producer(t):
        ' producer : PREPRODUCER name'
        movie_info['Producer']=t[2].strip()
        
    def p_writer(t):
        'writer : PREWRITER name'
        movie_info['Writer']=t[2].strip()

    def p_storyline(t):
        'storyline : PRESTORYLINE STRING'
        movie_info['Story line'] = t[2].strip()
        
    def p_boxoffice(t):
        'boxoffice : PREBOXOFFICE COST'
        movie_info['Box Office Collection']=t[2].strip()    
        
    def p_language(t):
        'language : PRELANGUAGE STRING'
        movie_info['Language']=t[2].strip()    
        
    def p_runtime(t):
        'runtime : PRERUNTIME STRING POSTRUNTIME'
        movie_info['Runtime']=t[2].strip()

    def p_name(t):
        'name : HEAD STRING AEND'
        t[0]=t[2]
        
    def p_names(t):
        'name : HEAD STRING AEND2 name'
        t[0]=t[2]+","+t[4]

    def p_error(t):
        pass


    page_info= codecs.open(movie_link, "r", "utf-8")

    lexer=lex()
    data=page_info.read()

    movie_info={}

    parser = yacc()

    parser.parse(data)
    print(movie_info)

if __name__ == '__main__':

    movie_link = "movie.html"

    alpha(movie_link)