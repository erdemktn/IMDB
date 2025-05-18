import requests
import tkinter as tk
from PIL import Image, ImageTk

url = "https://imdb236.p.rapidapi.com/imdb/lowest-rated-movies"

headers = {
	"x-rapidapi-key": "819f7c2075msh2ba0de75f4e25a9p148b09jsne6200c3daa3c",
	"x-rapidapi-host": "imdb236.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
result = response.json()

try:
    randm = None
    def movieChoise():
        global randm
        #Movies are append list
        movies = []
        for t in result:
            movies.append(t["title"])

        #Random Choice
        randm = random.choice(movies)
        movie_name_label.config(text=f"{randm}")


    def moviePredict():
        global randm
        ımdb_score = ımdb_entry.get()
        ımdb_point = None
        for i in result:
            if randm==i["title"]:
                ımdb_point=i["rating"]
        if ımdb_score==ımdb_point:
            result_label.config(text="Congrulatıons..")
        else:
            result_label.config(text="Opps Try Again...")


    window = tk.Tk()
    window.geometry("500x400")
    FONT = ("Calibri",20,"bold")

    # Background Image 
    background_image = Image.open("2.jpg")
    background_image = background_image.resize((500, 400), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)

    # Background with Canvas maker
    canvas = tk.Canvas(window, width=500, height=400)  
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw") 


    title = tk.Label(text="IMDB SCORE PREDICT",font=FONT)
    title.place(x=120,y=10)

    movie_label = tk.Label(text="Movie Name: ",font=FONT,fg="white",bg="black",bd=0)
    movie_label.place(x=10,y=90)

    movie_name_label = tk.Label(text="",font=FONT,fg="#bf0000",bg="black")
    movie_name_label.place(x=170,y=90)

    ımdb_label = tk.Label(text="IMDB Point: ",font=FONT,fg="white",bg="black",bd=0)
    ımdb_label.place(x=10,y=150)

    ımdb_entry = tk.Entry()
    ımdb_entry.place(x=160,y=160)

    result_label = tk.Label(text="",font=FONT,fg="#00ff00",bg="black")
    result_label.place(x=120,y=300)

    movie_button = tk.Button(text="MOVIE",font=FONT,fg="white",bg="black",command=movieChoise)
    movie_button.place(x=80,y=200)

    predict_button = tk.Button(text="PREDICT",font=FONT,fg="white",bg="black",command=moviePredict)
    predict_button.place(x=300,y=200)

    window.mainloop()
except Exception as e:
    print(f"Error: {e}")





