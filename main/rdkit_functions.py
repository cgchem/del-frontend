from rdkit import Chem
from rdkit.Chem import Draw  # todo sort out import to access directly from the Chem import?
from io import BytesIO
from base64 import b64decode


def smiles_to_bytesio(smi):

    """Generates the PNG image and returns it in a stringIO, to serve without writing to disk
    We need to use a base64-encoded SMILES because it's in the URL"""

    dat = b64decode(smi)
    smiles_str = dat.decode("UTF-8")
    mol = Chem.MolFromSmiles(smiles_str)
    out = BytesIO()
    img = Draw.MolToImage(mol, size=(200, 200))  # a PIL image
    img.save(out, "PNG")  # write the image data into the BytesIO
    out.seek(0)  # seek back to start so that the BytesIO can be read later
    return out
