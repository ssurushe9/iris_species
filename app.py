from flask import Flask,request,render_template
from utils import get_flower_species
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/species_prediction",methods =["GET","POST"])
def strength():
    if request.method == "GET":
        data = request.args.get

        SepalLengthCm = data("SepalLengthCm")
        SepalWidthCm  = data("SepalWidthCm")
        PetalLengthCm = data("PetalLengthCm")
        PetalWidthCm  = data("PetalWidthCm")
        

        flower_species = get_flower_species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

        if flower_species == 0:
            iris_value = "SETOSA"
        if flower_species == 1:
            iris_value = "VERSICOLOR"
        if flower_species == 2:
            iris_value = "VIRGINICA"
        


        return render_template("index.html",Predicted_Flower_Species = iris_value)
    

    elif request.method == "POST":
        data = request.form

        SepalLengthCm = data["SepalLengthCm"]
        SepalWidthCm  = data["SepalWidthCm"]
        PetalLengthCm = data["PetalLengthCm"]
        PetalWidthCm  = data["PetalWidthCm"]
        

        flower_species = get_flower_species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

        if flower_species == 0:
            iris_value = "SETOSA"
        if flower_species == 1:
            iris_value = "VERSICOLOR"
        if flower_species == 2:
            iris_value = "VIRGINICA"

        return render_template("index.html",Predicted_Flower_Species = iris_value)


if __name__ == "__main__":
    app.run(host = config.HOST_NUMBER,port = config.PORT_NUMBER,debug=True)