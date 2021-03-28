import re
import sys
import requests

def read_genre():
    file=open('rottentomatoes movie genre link.txt','r')
    genre_links={}
    count=0

    for line in file:
        if count > 0 :
            line=line.strip()
            if count%2 == 0 :
                genre_links[genre_types]=line
            else:
                genre_types = line[2:-1]
                genre_types = genre_types.strip()
            
        count += 1

    return genre_links


def select_genre(genre_links):

    found = True

    while found :
        genre_name= input("Enter genre: ")

        for i in genre_links:
            if i != genre_name :
                continue
            url=genre_links[i]
            html_request= requests.get(url, allow_redirects=True)
            html_file=open('rottentomatoes_genre.html','wb')
            html_file.write(html_request.content)
            return

        print("Genre name not found.")

def extract_movies():
    html_file=open('rottentomatoes_genre.html','r').read()
    regex='(<td>\n*.*\n*\s*.*<\/a>)'
    genre_list=re.findall(regex,html_file)
    #print(genre_list)
    movies_list={}
    for html_lines in genre_list:
            movie_name=html_lines.split('\n')
            movie_name=(movie_name[2])[:-4].strip()
            #print(movie_name)
            link=re.search("/[a-z/_(0-9)-]*",html_lines)
            full_url="https://www.rottentomatoes.com"+link.group()
            movies_list[movie_name]=full_url
    # print(movies_list)

    return movies_list


def select_movie(movies_list):

    found = True

    while found :
        movie_name= input("Enter movie name with year : ")

        for i in movies_list:
            if i != movie_name:
                continue

            link = movies_list[i]
            html_request= requests.get(link, allow_redirects=True)
            file_name="movie.html"
            html_file=open(file_name,'wb')
            html_file.write(html_request.content)
            print("Your HTML file is sucessfully generated")
            return

        print("Movie name not found. Try again.")
        

# Main Function
if __name__ == "__main__":

    genre_links = read_genre()

    result = select_genre(genre_links)

    movies_list = extract_movies()
    
    select_movie(movies_list)

    