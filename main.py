from flask import Flask, render_template, request
import pickle
import pandas as pd
import recommend

with open('movies2.pkl', 'rb') as f:
    movie_list = pickle.load(f)


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    name = request.form.get("movie")
    res = recommend.recommend('Avatar')
    if request.method=="POST":
        res = recommend.recommend(name)
        return render_template("index.html", movies_list=movie_list['title'].values, n1=res[0][0], r1=res[1][0],
                               n2=res[0][1], r2=res[1][1], n3=res[0][2], r3=res[1][2], n4=res[0][3], r4=res[1][3],
                               n5=res[0][4], r5=res[1][4], n6=res[0][5], r6=res[1][5])

    return render_template("index.html",movies_list=movie_list['title'].values,n1=res[0][0],r1=res[1][0],n2=res[0][1],r2=res[1][1],n3=res[0][2],r3=res[1][2],n4=res[0][3],r4=res[1][3],n5=res[0][4],r5=res[1][4],n6=res[0][5],r6=res[1][5])

if  __name__ == '__main__':
    app.run(debug=True)
