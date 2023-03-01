from flask import Flask, render_template, request, redirect, url_for
import requests
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)

def recommend(movie_name,flag):
    try :

        if flag==0:
            movie_idx = movies[movies["title"]==movie_name].index[0]
        else:
            movie_idx= movies[movies["id"]==movie_name].index[0]
        movie_list = model[movie_idx]
        #print(movie_idx)
        
        mov_recom=[]
        mov_recom.append(movies.iloc[movie_idx].id)

        for i in movie_list:
            mov_recom.append(movies.iloc[int(i[0])].id)
            #mov_recom.append(int(i[0]))

        return mov_recom
    except :
        return

def tmdbapi(onj):
    data=[]
    for i in onj:
        url="https://api.themoviedb.org/3/movie/"+str(i)+"?api_key=d1f17d65abb96cbc59efe93c7ccba1be&append_to_response=videos"
        uri="https://api.themoviedb.org/3/movie/"+str(i)+"/credits?api_key=d1f17d65abb96cbc59efe93c7ccba1be"
        data_dic = requests.get(url).json()
        credits = requests.get(uri).json()

        data_dic["tmdbid"]=i

        actors = []
        directors = []
        writer =[]
        for i in credits["cast"]:
            actors.append({'name' : i['name'], 'profile' : i["profile_path"], 'character_name' : i["character"] })
            if len(actors) ==5:
                break
        for i in credits["crew"]:
            if i["department"] == "Writing" and len(writer) < 3 :
                writer.append({'name' : i['name'], 'profile' : i["profile_path"] })
            if i["job"] == "Director":
                directors.append({'name' : i['name'], 'profile' : i["profile_path"] })
        data_dic["actors"] = actors
        data_dic["directors"] = directors
        data_dic["writer"] = writer 
  
        data.append(data_dic)
    return data


movies = pickle.load(open('movie_light_data','rb'))
movie_names = movies['title'].values

model = pickle.load(open('fast_sim_model','rb'))
#print(movies.head())


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        m_name = request.form.get('movieSearchInput')
        if m_name == "other":
            return render_template("google.html",items=movie_names,flag=1)
        elif m_name == "other1":
            return render_template("google.html",items=movie_names,flag=2)
        elif m_name == "other2":
            return render_template("google.html",items=movie_names,flag=3)
        elif m_name == "other3":
            return render_template("google.html",items=movie_names,flag=4)

        elif m_name == "prev1":
            return render_template("google.html",items=movie_names,flag=5)
        elif m_name == "prev2":
            return render_template("google.html",items=movie_names,flag=1)
        elif m_name == "prev3":
            return render_template("google.html",items=movie_names,flag=2)
        elif m_name == "prev4":
            return render_template("google.html",items=movie_names,flag=3)

        else:
            #print(m_name)
            mov_l = recommend(m_name,flag=0)
            dat = tmdbapi(mov_l)

            color = list(np.random.choice(range(256), size=3))
            return render_template("tmdb.html",dat=dat, color=color)

    else:    
        return render_template("google.html",items=movie_names)

@app.route("/imdb/<int:s>")
@app.route("/tmdb", methods=['GET','POST'])
def subpage(s):
    mov_l = recommend(int(s),flag=1)
    if mov_l != None:
        dat = tmdbapi(mov_l)

        color = list(np.random.choice(range(256), size=3))
        return render_template("tmdb.html",dat=dat,color=color)
    else:
        return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



if __name__ == '__main__':
    app.run(debug=True)