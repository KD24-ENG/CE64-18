from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import folium
import datetime
import json
import requests
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resource={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET", "POST"])
def base():
    # this is base map
    map = folium.Map(
        location=[13.756331, 100.501762],
        zoom_start=15
    )
    
    #folium.Polyline(
    #    location=[13.81226, 100.56266],
    #    color="red",
    #    weight=4).add_to(map)

    folium.Marker(
        location=[13.756331, 100.501762],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)
    
    return map._repr_html_()

@app.route("/test", methods=["GET", "POST"])
def test():
    return "test test"

if __name__ == "__main__":
    app.run(debug=True)
