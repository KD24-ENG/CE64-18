from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import folium
import datetime
import json
import requests
import numpy as np

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resource={r"/*": {"origins": "*"}})

with open("road.json", encoding="utf-8") as f:
    d = json.load(f)


@app.route("/")
def base():
    # this is base map
    map = folium.Map(
        location=[13.756331, 100.501762],
        zoom_start=15
    )
    folium.Marker(
        location=[13.756331, 100.501762],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(map)
    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)
