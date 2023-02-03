from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, make_response
from .rdkit_functions import smiles_to_bytesio
from main.db import get_db

bp = Blueprint('lookup_page', __name__, url_prefix='')


@bp.route("/", methods=["GET"])
def main():

    return render_template("main_page/main.html")


@bp.route("/smi2png/<smiles>", methods=["GET"])
def smiles_to_png(smiles):

    """Returns a PNG object response from a smiles string, to get a mol image from RDkit."""

    byts = smiles_to_bytesio(smiles)
    resp = make_response(byts.read())
    resp.content_type = "image/png"
    return resp


@bp.route("/substruct", methods=["POST"])
def substructure_search():

    smiles = request.json["SMILES"]
    db = get_db()
    cur = db.cursor()
    cur.execute("""SELECT 
            molecules.id, 
            molecules.structure, 
            raw_data.sample, 
            raw_data.hitcounts, 
            raw_data.zscore FROM molecules 
            INNER JOIN raw_data
            ON molecules.id = raw_data.id
            WHERE structure@> %s LIMIT 20""", (smiles,))

    return jsonify(cur.fetchall())
