import pandas
import pickle
import requests



def fetchImage(id_list):
    ImageLink_list = []
    for i in id_list:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=a8bd63668e0f79e16bead18c1098b447&language=en-US/jRXYjXNq0Cs2TcJjLkki24MLp7u.jpg".format(i)
        res = requests.get(url)
        data = res.json()
        image_link = data['poster_path']
        url2 = "https://image.tmdb.org/t/p/w500/{}".format(image_link)
        ImageLink_list.append(url2)
    return ImageLink_list



def recommend(movie):
    with open('new_df2.pkl', 'rb') as f:
        new_df = pickle.load(f)

    with open('similarity2.pkl', 'rb') as f:
        similarity = pickle.load(f)

    with open('movies2.pkl', 'rb') as f:
        movie_list = pickle.load(f)
  #taking index of movie what we receive
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    movie_name=[]
    movie_id=[]
    for i in movies_list:
        movie_name.append(new_df.iloc[i[0]].title)
        movie_id.append(new_df.iloc[i[0]].movie_id)
  #  print(movie_id)
  #  print(movie_name)
    image_link=fetchImage(movie_id)
    Res = []
    Res.append(movie_name)
    Res.append(image_link)
    return Res

